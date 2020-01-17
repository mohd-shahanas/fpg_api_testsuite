import pymysql
import paramiko
from sshtunnel import SSHTunnelForwarder
import pandas as pd
from dynaconf import settings as conf


class FpgDB:
    def __init__(self):
        self.mypkey = paramiko.RSAKey.from_private_key_file(conf.PRIVATE_KEY_PATH)
        self.sql_hostname = conf.SQL_HOSTNAME
        self.sql_username = conf.SQL_USERNAME
        self.sql_password = conf.SQL_PASSWORD
        self.sql_main_database = conf.SQL_MAIN_DATABASE
        self.sql_port = conf.SQL_PORT
        self.ssh_host = conf.SSH_HOST
        self.ssh_user = conf.SSH_USER
        self.ssh_port = conf.SSH_PORT
        self.conn = None
        self.tunnel = None
        self.establish_db_connection()

    def establish_db_connection(self):
        self.tunnel = SSHTunnelForwarder((self.ssh_host, self.ssh_port),
                                         ssh_username=self.ssh_user,
                                         ssh_pkey=self.mypkey,
                                         remote_bind_address=(self.sql_hostname, self.sql_port))
        self.tunnel.start()
        self.conn = pymysql.connect(host='127.0.0.1', user=self.sql_username,
                                    passwd=self.sql_password, db=self.sql_main_database,
                                    port=self.tunnel.local_bind_port)

    def drop_db_connection(self):
        self.tunnel.close()
        self.conn.close()

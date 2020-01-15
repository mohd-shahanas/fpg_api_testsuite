import requests
from dynaconf import settings as conf


class FpgClient:

    def __init__(self):
        print("In fpg_client_init")
        auth = FpgAuth(conf.BEARER_TOKEN)
        self.session = requests.Session()
        self.session.auth = auth

    def get(self, url):
        """GET Request."""
        return self.session.get(url)

    def post(self, url, data):
        """POST Request."""
        return self.session.post(url, json=data)


class FpgAuth(requests.auth.AuthBase):
    """Fpg Authentication interface."""

    def __init__(self,token):
        self.bearer_token = token

    def __call__(self, r):
        r.headers["Content-Type"] = "application/json"
        r.headers['IndustryId'] = conf.INDUSTRY_ID
        r.headers["Authorization"] = "Bearer " + self.bearer_token
        return r


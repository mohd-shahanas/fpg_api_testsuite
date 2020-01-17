"""Base conftest.py."""
import pytest

from fpg.library.fpg_client import FpgClient
from fpg.library.fpg_db import FpgDB


@pytest.fixture(scope="session")
def fpg_client_fix():
    """
    Client fixture for FPG.

    The scope of the fixture is for the entire session of a test run.
    """
    return FpgClient()


@pytest.fixture(scope="session")
def fpg_db_fix():
    """
    Database fixture for FPG.

    The scope of the fixture is for the entire session of a test run.
    """
    print("Establishing DB connection")
    fpg_db = FpgDB()
    yield fpg_db
    print("Dropping the DB ")
    fpg_db.drop_db_connection()



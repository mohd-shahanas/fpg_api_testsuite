import pytest
import requests
import pandas as pd

from dynaconf import settings as conf

from fpg.common import assertions
from fpg.library import fpg_payloads


@pytest.mark.regression
@pytest.mark.parametrize(
    "country_id",
    [1, 3452, 2658],
)
def test_get_quote_currency(fpg_client_fix, fpg_db_fix, country_id):
    print(f"Testing with country_id -> {country_id}")

    # Response Validation
    exp_resp_status_code = 200
    url = conf.BASE_URL + 'region/secure/getCommonUsedCurrencyForPortfolio/1?regionId='+ str(country_id)
    response = fpg_client_fix.get(url=url)
    assertions.assert_equal(response.status_code,exp_resp_status_code)

    # response_body = response.json()
    # response_data = response_body["data"]

    # # DB validation
    #
    # query = f'''select currency from in_gauge_2018_1710_hotel.region where id={country_id};'''
    # data = pd.read_sql_query(query, fpg_db_fix.conn)
    # print(f"Querying DB")
    # print(data["currency"])
    # #assertions.assert_equal(200,200)





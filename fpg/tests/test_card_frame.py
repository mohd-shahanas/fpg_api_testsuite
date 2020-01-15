import pytest
import requests

from dynaconf import settings as conf
from pytest_testrail.plugin import pytestrail

from fpg.common import assertions
from fpg.library import fpg_payloads


@pytest.mark.parametrize(
    ("rating", "platform", "exp_status_code"),
    [
        pytest.param(1, 1, requests.codes.ok, marks=[pytest.mark.smoke, pytest.mark.testrail(ids=('3',))]),
        pytest.param(5, 3, requests.codes.internal_server_error, marks=[pytest.mark.regression, pytest.mark.testrail(ids=('4',))]),
        pytest.param(7, 1, requests.codes.internal_server_error,marks=[pytest.mark.regression, pytest.mark.testrail(ids=('5',))]),
    ],
    ids=[
        "with_valid_rating_and_platform",
        "with_valid_rating_and_invalid_platform",
        "with_invalid_rating_and_valid_platform",
    ],
)
def test_is_card_useful(fpg_client_fix,rating,platform,exp_status_code):
    url = conf.BASE_URL + 'cardUsefulSuggestion/secure'

    payload = fpg_payloads.get_card_useful_payload(rating=rating,platform=platform)

    response = fpg_client_fix.post(url=url,data=payload)
    assertions.assert_equal(response.status_code,exp_status_code)

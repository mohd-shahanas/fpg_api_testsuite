import requests
import logging
from dynaconf import settings as conf

log = logging.getLogger(__name__)
logging.basicConfig(format="%(asctime)s %(levelname)s %(message)s")


class FpgClient:

    def __init__(self):
        auth = FpgAuth(conf.BEARER_TOKEN)
        self.session = requests.Session()
        self.session.auth = auth

        adapters = [LoggingHTTPAdapter()]
        for adapter in adapters:
            self.session.mount("http://", adapter)
            self.session.mount("https://", adapter)

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


class LoggingHTTPAdapter(requests.adapters.HTTPAdapter):
    """Adapter to log request and response."""

    def send(self, request, *args, **kwargs):
        log.info(f"Request: {request.method} {request.url}")
        log.info(f"Request headers: {request.headers}")
        log.info(f"Request body: {request.body}")

        resp = super().send(request, *args, **kwargs)

        log.info(f"Response: {resp.status_code} {resp.reason}")
        log.info(f"Response headers: {resp.headers}")
        log.info(f"Response body: {resp.content}")

        return resp

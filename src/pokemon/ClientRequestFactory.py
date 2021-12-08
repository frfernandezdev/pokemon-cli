import requests


class ClientRequestFactory:
    def request(self, method, url, **params):
        try:
            client = getattr(requests, method)
            response = client(url, params)
            return response.json()
        except requests.exceptions.RequestException as e:
            print("Fail in load pokemon %s" % str(e))

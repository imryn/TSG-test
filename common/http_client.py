import requests
import json
from common.headers import Headers

class HttpClient(Headers):

    @staticmethod
    def __get_api_details(response):
        try:
            message = {
                "url": response.url,
                "timeout": response.elapsed.total_seconds(),
                "statusCode": response.status_code
            }
            try:
                message["response"] = json.loads(response.content)

            except ValueError:
                message["response"] = response.content.decode("utf-8")

            if 'RequestID' in response.headers:
                message["request_id"] = response.headers.get("RequestID")

            payload = response.request.body

            try:
                if payload is not None:
                    message["payload"] = json.loads(payload)

            except (ValueError, TypeError):
                message["payload"] = payload

            return message
        except (ValueError, KeyError) as Error:
            error_text = f"we got status {response.status_code} from the server on url - {response.url}, \n " \
                         f"with error {error}"

            if "RequestID" in response.headers.keys():
                exception_text = error_text + f" request id is {response.headers['RequestID']}"
                print(exception_text)
            else:
                print(error_text)

    def __get_headers(self, json_request, data_request, params, headers, Authorization):
        return self.get_headers_by_request_type(json_request, data_request, params, headers, Authorization)

    def get(self, url, params=None, headers=None, json_request=None, data_request=None, Authorization=None):
        request_headers = self.__get_headers(json_request, data_request, params, headers, Authorization)
        response = requests.request(method='GET', url=url, params=params, headers=request_headers, json=json_request)
        return self.__get_api_details(response)

    def post(self, url, json_request=None, data_request=None, headers=None, Authorization=None):
        request_headers = self.__get_headers(json_request, data_request, headers, Authorization)
        response = requests.request(method='POST', url=url, json=json_request, data=data_request,
                                    headers=request_headers)
        return self.__get_api_details(response)

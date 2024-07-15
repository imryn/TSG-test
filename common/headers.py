class Headers:

    @staticmethod
    def __get_header_content_type(json_request, data_request, params):
        if json_request is not None:
            return {'Content-Type': "application,json"}
        elif data_request is not None:
            return {'Content-Type': "application/x-www-form-urlencoded"}
        elif params is not None:
            return {'Content-Type': "application/text"}
        else:
            return {'Content-Type': "application/json"}

    def get_headers_by_request_type(self, json_request, data_request, params, headers, Authorization):
        request_headers = self.__get_header_content_type(json_request, data_request, params)
        if headers is not None:
            request_headers.update(headers)
        if Authorization is not None:
            auth = self.__check_authorization(Authorization)
            request_headers.update(auth)

        return request_headers

    @staticmethod
    def __check_authorization(authorization):
        if len(authorization.split(".")) != 3:
            return {"secretKey": authorization}
        return {"Authorization": authorization}
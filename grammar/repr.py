import json


class FormLogProcessReport():
    def __init__(
            self, is_success: bool, is_parse_error: bool, is_http_error: bool,
            error_msg: str, request_body: dict
    ):
        self.is_success = is_success
        self.is_parse_error = is_parse_error
        self.is_http_error = is_http_error
        self.error_msg = error_msg
        self.request_body = request_body

    def __repr__(self):
    # def __str__(self):
        json_log = {}
        json_log["is_success"] = self.is_success
        json_log["is_parse_error"] = self.is_parse_error
        json_log["is_http_error"] = self.is_http_error
        json_log["error_msg"] = self.error_msg
        json_log["request_body"] = self.request_body
        return json.dumps(json_log)


l = FormLogProcessReport(True, False, False, "", {})
print(l)
l = FormLogProcessReport(False, True, False, "PARSE ERROR", None)
print(l)

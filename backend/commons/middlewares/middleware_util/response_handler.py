from typing import Any, Dict
from django.http import HttpRequest, HttpResponse
from .convert_body import convert_body


class ResponseBodyHandler:
    def __init__(self, request: HttpRequest, MAX_LENGTH: int):
        self.is_json = 'application/json' in request.headers.get('Content-Type', '')
        self.MAX_LENGTH = MAX_LENGTH

    def process(self, request: HttpRequest, response: HttpResponse) -> Dict[str, Any]:
        res = self.get_base(request, response)
        res['body'] = self.get_body(request)
        return res

    def get_base(self, request: HttpRequest, response: HttpResponse) -> Dict[str, Any]:
        return {
            'method': request.method,
            'domain': request.get_host(),
            'path': request.get_full_path(),
            'status': response.status_code,
            'content_type': response.get('Content-Type', ''),
            'remote_addr': request.META.get('REMOTE_ADDR', ''),
        }

    def get_body(self, response: HttpResponse) -> str:
        try:
            if self.is_json:
                return self._get_body_json(response)
        except Exception:
            pass
        return ""

    def _get_body_json(self, response: HttpResponse) -> str:
        content_length = int(response.headers.get('Content-Length', 0))
        return convert_body(response.body, content_length, self.MAX_LENGTH)

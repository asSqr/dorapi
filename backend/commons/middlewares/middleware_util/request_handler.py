from typing import Any, Dict
from django.http import HttpRequest
from .convert_body import convert_body


class RequestBodyHandler:
    def __init__(self, request: HttpRequest, MAX_LENGTH: int):
        self.is_json = 'application/json' in request.headers.get('Content-Type', '')
        self.is_urlencoded = 'application/x-www-form-urlencoded' in request.headers.get('Content-Type', '')
        self.MAX_LENGTH = MAX_LENGTH

    def process(self, request: HttpRequest) -> Dict[str, Any]:
        req = self.get_base(request)
        req['body'] = self.get_body(request)
        return req

    def get_base(self, request: HttpRequest) -> Dict[str, Any]:
        return {
            'method': request.method,
            'domain': request.get_host(),
            'path': request.get_full_path(),
            'content_type': request.headers.get('Content-Type', ''),
            'content_length': request.headers.get('Content-Length', ''),
            'remote_addr': request.META.get('REMOTE_ADDR', ''),
        }

    def get_body(self, request: HttpRequest) -> str:
        try:
            if self.is_json:
                return self._get_body_json(request)
            elif self.is_urlencoded:
                return self._get_body_urlencoded(request)
        except Exception:
            pass
        return ""

    def _get_body_json(self, request: HttpRequest) -> str:
        content_length = int(request.headers.get('Content-Length', ''))
        return convert_body(request.body, content_length, self.MAX_LENGTH)

    def _get_body_urlencoded(self, request: HttpRequest) -> str:
        return request.body.decode('utf-8')[:self.MAX_LENGTH]

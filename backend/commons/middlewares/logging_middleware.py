import logging
from django.http import HttpRequest, HttpResponse
from .middleware_util import RequestBodyHandler, ResponseBodyHandler

logger = logging.getLogger(__name__)

class LoggerMiddleware:
    MAX_LENGTH = 1024

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request: HttpRequest):

        health_check = 'health_check' in request.path
        if health_check:
            return self.get_response(request)

        req = self.handle_request(request)

        logger.info('[>>django] request: %s', req)

        response: HttpResponse = self.get_response(request)

        res = self.handle_response(request, response)

        logger.info('[<<django] response: %s / request_body: %s', res, req.get('body', None))

        return response

    def handle_request(self, request: HttpRequest):
        handler = RequestBodyHandler(request, self.MAX_LENGTH)
        req = handler.process(request)
        return req

    def handle_response(self, request: HttpRequest, response: HttpResponse):
        handler = ResponseBodyHandler(request, self.MAX_LENGTH)
        res = handler.process(request, response)
        return res

import logging
from typing import Optional
from django.utils.deprecation import MiddlewareMixin
from django.utils.functional import SimpleLazyObject
from dorapi.models import MUser


logger = logging.getLogger(__name__)


class MUserMiddleware(MiddlewareMixin):

    muser_model = MUser

    def process_request(self, request):
        
        logger.debug('muser_middleware')
        
        request.muser = SimpleLazyObject(lambda: self.get_muser(request))

    def get_muser(self, request) -> Optional[MUser]:
        
        if not hasattr(request, '_cached_muser'):
            self._get_muser(request)

        return request._cached_muser

    def _get_muser(self, request):
  
        request._cached_muser = request.user

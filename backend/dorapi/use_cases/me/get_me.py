from commons.use_case import BaseUseCase
from dorapi.models import MUser


class GetMe(BaseUseCase):

    muser_class = MUser

    def execute(self, muser: MUser):

        return muser

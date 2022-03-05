from commons.use_case import BaseUseCase
from dorapi.models import MUser, MGadget
from dorapi.logics.mgadget import MGadgetProcess
from typing import Dict, Any


class ListMGadget(BaseUseCase):

    mgadget_class = MGadget

    def execute(self, muser: MUser, filterset_data: Dict[str, Any]):
    
        page = filterset_data.get('page')
        page_size = filterset_data.get('page_size')
        keyword = filterset_data.get('keyword')
        sort_key = filterset_data.get('sort_key')
        sort_order = filterset_data.get('sort_order')

        mgadget_queryset = (
            self.mgadget_class.objects
                .all()
        )

        mgadget_process = MGadgetProcess(mgadget_queryset)
        mgadget_process.filter_or_query_param(keyword)
        mgadget_process.sort_by_query_param(sort_key, sort_order)
        mgadget_process.paginate(page_size, page)
        mgadget_process.distinct()

        mgadget_queryset = mgadget_process.mgadget_queryset
        
        count = len(list(mgadget_queryset))

        return mgadget_queryset, {'count': count}

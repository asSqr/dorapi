from typing import Dict, Any
from functools import reduce


def generate_query(query_dict: Dict[str, Any]) -> str:
    def reducer(acc, key):
        prefix = '&' if len(acc) > 0 else ''
        value = query_dict[key]
        
        acc += f'{prefix}{key}={value}'
        
        return acc
    
    query_str = reduce(reducer, query_dict.keys(), '')
    
    return query_str

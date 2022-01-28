import json


def convert_body(body, content_length: int, max_length: int):
    result = None
    try:
        if max_length <= content_length:
            result = body.decode('utf-8')[:max_length]
        else:
            result = json.loads(body)
    except Exception:
        result = str(body)[:max_length]

    return result

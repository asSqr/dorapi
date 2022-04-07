class GoogleAPIConfig:
    GOOGLE_BASE_URL = 'https://www.googleapis.com'
    GOOGLE_CUSTOM_SEARCH_PATH = '/customsearch/v1'
    GOOGLE_CUSTOM_DORA_SUFFIX = ' ドラえもん コミック'
    WAIT_SECONDS = 0.2


class RequestConfig:
    FAIL_POST_RETRIES = 5
    POST_INTERVAL = 3
    FAIL_POST_INTERVAL = 1

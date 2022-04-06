import asyncio
import aiohttp
from simplejson import JSONDecodeError
from .config import RequestConfig


async def retries(func, args, kwargs):
    error = Exception()
    for _ in range(RequestConfig.FAIL_POST_RETRIES):
        try:
            res = await func(*args, **kwargs)
            await asyncio.sleep(RequestConfig.POST_INTERVAL)
            return res
        except Exception as e:
            await asyncio.sleep(RequestConfig.FAIL_POST_INTERVAL)
            error = e
    raise error


async def jsonize(resp):
    try:
        return await resp.json()
    except JSONDecodeError:
        msg = await resp.read()
        print(msg)
        raise JSONDecodeError(msg)


async def _get(*args, **kwargs):
    async with aiohttp.ClientSession(trust_env=True) as session:
        async with session.get(*args, **kwargs) as resp:
            return await jsonize(resp)


async def _post(*args, **kwargs):
    async with aiohttp.ClientSession(trust_env=True) as session:
        async with session.post(*args, **kwargs) as resp:
            return await jsonize(resp)


async def _put(*args, **kwargs):
    async with aiohttp.ClientSession(trust_env=True) as session:
        async with session.put(*args, **kwargs) as resp:
            return await jsonize(resp)


async def _patch(*args, **kwargs):
    async with aiohttp.ClientSession(trust_env=True) as session:
        async with session.patch(*args, **kwargs) as resp:
            return await jsonize(resp)


async def get(*args, **kwargs):
    return await retries(_get, args, kwargs)


async def post(*args, **kwargs):
    return await retries(_post, args, kwargs)


async def put(*args, **kwargs):
    return await retries(_put, args, kwargs)


async def patch(*args, **kwargs):
    return await retries(_patch, args, kwargs)

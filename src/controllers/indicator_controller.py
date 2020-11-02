import aiohttp
import os

urlEnv = os.getenv('URLENVINDICATOR')


async def fetch(session, url, data=None):
    header = {
        'Accept': 'application/json'
    }
    async with session.post(
        url,
        json=data,
        headers=header
    ) as response:
        return await response.json(), response.status


async def post_indicator(indicator):
    response = dict()
    status = 404

    async with aiohttp.ClientSession() as session:
        response, status = await fetch(
            session,
            urlEnv,
            indicator
        )

    return response, status

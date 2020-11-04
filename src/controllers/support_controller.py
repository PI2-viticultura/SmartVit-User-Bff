import aiohttp
import os

urlEnv = os.getenv(
    'URLENVSUPPORT',
    'https://smartvit-support-dev.herokuapp.com/support'
)


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


async def post_support(support):
    response = dict()
    status = 404

    async with aiohttp.ClientSession() as session:
        response, status = await fetch(
            session,
            urlEnv,
            support
        )

    return response, status

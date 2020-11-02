import aiohttp
import json
import os

urlEnv = os.getenv(
    'URLENVPEST',
    'https://smartvit-pest-dev.herokuapp.com/pest'
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
        return await response.text(), response.status


async def post_pest(pest):
    response = dict()
    status = 404

    async with aiohttp.ClientSession() as session:
        response, status = await fetch(
            session,
            urlEnv,
            pest
        )

    return json.loads(response), status

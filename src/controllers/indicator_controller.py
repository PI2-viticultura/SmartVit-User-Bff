import aiohttp
import json
import os

urlEnv = os.getenv('URLENVINDICATOR', 'http://localhost:8000/indicators')


async def retrieve(session, url, data=None):
    header = {
        'Accept': 'application/json'
    }
    async with session.get(
        url,
        headers=header
    ) as response:
        return await response.text(), response.status


async def retrieve_indicator(winery_id):
    response = dict()
    status = 404

    async with aiohttp.ClientSession() as session:
        response, status = await retrieve(
            session,
            urlEnv + '/' + winery_id,
        )
    try:
        return json.loads(response), status
    except Exception as e:
        print(e)
        return response, status

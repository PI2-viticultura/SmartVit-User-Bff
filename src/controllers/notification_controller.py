import aiohttp
import json
import os

urlEnv = os.getenv(
    'URLENVNOTIFICATION',
    'https://smartvit-notification-dev.herokuapp.com/notification'
)


async def retrieve(session, url, data=None):
    header = {
        'Accept': 'application/json'
    }
    async with session.get(
        url,
        headers=header
    ) as response:
        return await response.text(), response.status


async def get_notification(user_id):
    response = dict()
    status = 404

    async with aiohttp.ClientSession() as session:
        response, status = await retrieve(
            session,
            urlEnv + '/' + user_id
        )

    return json.loads(response), status

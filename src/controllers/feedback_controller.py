import aiohttp
import requests
import json


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


async def post_feedback(feedback):
    response = dict()
    status = 404

    async with aiohttp.ClientSession() as session:
        response, status = await fetch(
            session,
            'http://localhost:8000/feedback',
            feedback
        )

    return response, status
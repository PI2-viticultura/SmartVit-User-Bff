# import aiohttp
import requests


# async def fetch(session, url, key=None):
#     async with session.get(url) as response:
#         return await response.json(), response.status


async def get_git():
    response = dict()
    status = 404

    r = requests.get('https://api.github.com/users/Lucas362/repos')
    status = r.status_code
    if status == 200:
        return r.json(), status

    # async with aiohttp.ClientSession() as session:
    #     response, status = await fetch(
    #         session,
    #         'https://api.github.com/users/Lucas362/repos'
    #     )

    return response, status

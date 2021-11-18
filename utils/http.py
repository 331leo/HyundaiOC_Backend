import aiohttp
from enum import Enum

from models.user import User
class REQ_TYPE(str, Enum):
    GET = "GET"
    POST = "POST"


async def request(type: REQ_TYPE, **kwargs) -> dict:
    async with aiohttp.ClientSession() as session:
        async with session.request(type, **kwargs) as resp:
            return await resp.json()

async def get_user_data(token: str) -> User:
    data = (
        await request(
            REQ_TYPE.GET,
            url=f"https://id.hyundaicpu.com/v1/users/@me",
            headers={
                "Authorization": "Bearer " + token,
            },
        )
    )   
    print(token)
    print(data)
    return User.parse_obj(data)
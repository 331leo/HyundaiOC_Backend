from fastapi import APIRouter, Request
from starlette.responses import RedirectResponse
from utils.http import request, REQ_TYPE
from utils.etc import get_basic_auth_token
from os import getenv

login_router = APIRouter()

@login_router.get("/", response_class=RedirectResponse)
async def get_link():
    return RedirectResponse(f"{getenv('OAUTH_HOST')}/v1/login?redirect_uri={getenv('WEB')}/callback")

@login_router.post("/token")
async def post_token(req:Request):
    code = (await req.json()).get("code")
    token = (
        await request(
            REQ_TYPE.POST,
            url=f"https://id.hyundaicpu.com/v1/oauth2/token",
            data={"code": code},
            headers={
                "Authorization": get_basic_auth_token(
                    getenv("OAUTH_ID"), getenv("OAUTH_SECRET")
                )
            },
        )
    ).get("access_token")    
    return {"token": token}


from fastapi import APIRouter, HTTPException, Security
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from models.user import User
from models.class_ import Class
from utils.http import get_user_data
from utils.db import get_class_info
users_router = APIRouter()

@users_router.get("/class", response_model=Class)
async def get_users_data(credentials: HTTPAuthorizationCredentials = Security(HTTPBearer())):
    try:
        userData: User = await get_user_data(credentials.credentials)
    except Exception as e:
        raise HTTPException(status_code=401, detail=str(e))
    return Class.parse_obj({**get_class_info(userData.grade, userData.classnum), "student":userData.dict()})
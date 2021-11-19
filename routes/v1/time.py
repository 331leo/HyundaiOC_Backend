from fastapi import APIRouter, HTTPException, Security
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from models.user import User
from models.class_ import NowData
from utils.http import get_user_data
from utils.db import get_class_info
from utils.time import now_weekday, get_date_string, current_school_time
time_router = APIRouter()

@time_router.get("/", response_model=NowData)
async def current_data(credentials: HTTPAuthorizationCredentials = Security(HTTPBearer())):
    try:
        userData: User = await get_user_data(credentials.credentials)
    except Exception as e:
        raise HTTPException(status_code=401, detail=str(e))
    nowsubject = get_class_info(userData.grade, userData.classnum).get("classes").get(now_weekday())[current_school_time()] if current_school_time() >= 0 else None
    return {
        "date": get_date_string(),
        "period": current_school_time(),
        "weekday": now_weekday(),
        "subject": nowsubject
    }
    


from redis import Redis
from os import getenv
from dotenv import load_dotenv
from json import loads
load_dotenv()
class_db = Redis(host=getenv("REDIS_HOST"), port=int(getenv("REDIS_PORT")), db=0)

def get_class_info(grade, classnum) -> dict:
    return loads(class_db.get(f"{grade}-{classnum}").decode())
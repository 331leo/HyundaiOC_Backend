import uvicorn
from dotenv import load_dotenv

load_dotenv()
from os import getenv

uvicorn.run("app:app", host="0.0.0.0", port=int(getenv("PORT")), reload=True)
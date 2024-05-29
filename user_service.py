from fastapi import FastAPI
from hashlib import md5
from datetime import datetime
import logging
import platform

app = FastAPI()

logger = logging.getLogger('user-service')
logger.setLevel(logging.DEBUG)

file_handler = logging.FileHandler('user_service.log')
file_handler.setLevel(logging.DEBUG)

console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)

formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
file_handler.setFormatter(formatter)
console_handler.setFormatter(formatter)
logger.addHandler(file_handler)
logger.addHandler(console_handler)

common_file_handler = logging.FileHandler('common.log')
common_file_handler.setLevel(logging.DEBUG)
common_file_handler.setFormatter(formatter)
logger.addHandler(common_file_handler)

@app.get("/register")
async def register_user():
    user_id = generate_user_id()
    logger.info(f"Registered new user with ID: {user_id}")
    return {"user_id": user_id}

def generate_user_id():
    time_str = str(datetime.now())
    return md5(time_str.encode()).hexdigest()

@app.get("/health")
async def health_check():
    logger.info("Health check performed")
    return {"status": "ok"}

@app.get("/info")
async def info():
    info = {
        "platform": platform.platform(),
        "python_version": platform.python_version()
    }
    logger.info("Info requested")
    return info
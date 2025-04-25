from fastapi import FastAPI
from routes.route import router

app = FastAPI()

app.include_router(router)

#To run this create a .env and inside that MONGODB_URI = Mongo_db connection uri (or) goto config/database.py and change the uri there
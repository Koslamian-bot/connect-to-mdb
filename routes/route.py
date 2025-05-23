from fastapi import APIRouter
from models.samples import sample
from config.database import collection_name
from schema.schemas import list_all
from bson import ObjectId

router = APIRouter()

#Get req
@router.get("/")
async def get_samples():
    samples = list_all(collection_name.find())
    return samples

@router.post("/")
async def post_sample(sample:sample):
    collection_name.insert_one(dict(sample))

@router.put("/{id}")
async def put_sample(id : str , sample : sample):
    collection_name.find_one_and_update({"_id":ObjectId(id)}, {"$set":dict(sample)})
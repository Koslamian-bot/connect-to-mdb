from pydantic import BaseModel

class sample(BaseModel):
    name : str
    audio_id : str
    desc : str
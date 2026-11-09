
# python -m uvicorn ft:app

from fastapi import FastAPI
from pydantic import BaseModel

offices = {
    1: {"name": "Headquarters", "address": "New York", "phone": "123-456-7890"},
    2: {"name": "Branch Office", "address": "Los Angeles", "phone": "987-654-3210"}
}

id = 2
def gen_id():
    global id
    id += 1
    return id


app = FastAPI()

class Office(BaseModel):
    name: str
    address: str
    phone: str


@app.get("/")
async def home():
    return {"message": "Welcome"}

@app.post("/offices")
async def create_office(office: Office):
    new_id = gen_id()
    offices[new_id] = office.model_dump()
    return {"message": "Office created successfully", "office_id": new_id}

@app.get("/offices/{office_id}")
async def get_office(office_id: int):
    if office_id in offices:
        return {"office": offices[office_id]}
    else:
        return {"message": "Office not found"}
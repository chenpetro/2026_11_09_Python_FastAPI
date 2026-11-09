from ft import FastAPI, Path, status

status.HTTP_201_CREATED

app = FastAPI()

@app.get("/")
def get_request():
    return {"message": "Get request received"}

@app.post("/")
def post_request():
    return {"message": "Post request received"}


@app.get("/users/{username}/{age}")
def path_request(
    username: str = Path(..., max_length=10, min_length=3),
    age: int = Path(..., gt=18, lt=60)
    ):
    return {"your_name": username, "your_age": age}
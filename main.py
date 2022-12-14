from fastapi import FastAPI

app = FastAPI()


@app.get("/profile")
async def read_root():
    return {"Hello": "World"}
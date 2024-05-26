from fastapi import FastAPI

app=FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello Nosir"}

#Path Parameters: Get an Item by ID
@app.get("/items/{item_id}")
async def read_item(item_id: int):
    return {"item_id":item_id}
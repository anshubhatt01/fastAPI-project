from fastapi import FastAPI
app = FastAPI()
@app.get("/")
def read_root():
    return {"Hello": "World from fastapi!"}

@app.get("/ping")
def ping():
    return{'status': 'ok'}
from  fastapi import FastAPI

app = FastAPI()

@app.get('/')
def defaultRoot():
    return "hello to fastapi app"


from fastapi import FastAPI
import uvicorn
from app.routers import users, health_records

app = FastAPI()

app.include_router(users.router)
app.include_router(health_records.router)

if __name__ == "__main__":
    uvicorn.run("app.main:app", host="localhost", port=8000, reload=True)
@app.get("/")
def check_api():
    print("Hello World")
    return {"message":"Data Handled"}
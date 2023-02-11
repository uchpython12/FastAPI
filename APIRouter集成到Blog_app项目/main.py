import uvicorn
from fastapi import FastAPI
from routers import users,blog

app = FastAPI(title="Fast API +ORM")
app.include_router(users.router,tags=["User"])
app.include_router(blog.router,tags=["Blog"])

if __name__ == '__main__':
    uvicorn.run("main:app", port=8888, reload=True)

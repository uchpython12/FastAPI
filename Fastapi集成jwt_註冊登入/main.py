import typing
import jwt
from jwt import PyJWTError
import datetime
import uvicorn
from fastapi import FastAPI, Form, HTTPException, status, Depends, Header, Response, Cookie,Request
import hashlib
from schamas import UserOut
from database import get_db
from sqlalchemy.orm import Session
from models import User
from passlib.context import CryptContext
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
app = FastAPI()
crypt = CryptContext(schemes=["bcrypt"], deprecated="auto")
exp = datetime.datetime.now() + datetime.timedelta(days=14)
secrey_key = "2123jdsjl@:Jdj1"

templates = Jinja2Templates(directory="templates")

@app.get("/login", response_class=HTMLResponse)
def read_item(request: Request):
    return templates.TemplateResponse("login.html", {"request": request})
@app.get("/register", response_class=HTMLResponse)
def read_item(request: Request):
    return templates.TemplateResponse("register.html", {"request": request})


@app.post("/register", response_model=UserOut)
def register(
        username: str = Form(default=""),
        password: str = Form(default=""),
        re_password: str = Form(default=""),
        email: str = Form(default=""),
        db: Session = Depends(get_db)
):
    if password != re_password:
        raise HTTPException(detail="兩次密碼輸入不一致", status_code=status.HTTP_400_BAD_REQUEST)

    db_user = db.query(User).filter(User.username == username).first()
    if db_user:
        raise HTTPException(detail="用戶名已存在", status_code=status.HTTP_400_BAD_REQUEST)

    # m = hashlib.md5("鹽sfsja;j;3j".encode("utf8"))
    # m.update(password.encode("utf8"))
    # hashed_password = m.hexdigest()  # 加密過後的密文

    user = User(
        username=username,
        password=crypt.hash(password),
        email=email,
    )
    db.add(user)
    db.commit()
    db.refresh(user)
    return user


@app.post("/login", response_model=UserOut)
def login(response: Response, username: str = Form(None), password: str = Form(None), db: Session = Depends(get_db)):
    db_user: User = db.query(User).filter_by(username=username).first()
    if not db_user:
        raise HTTPException(detail="用戶名不存在", status_code=400)
    if not crypt.verify(password, db_user.password):
        raise HTTPException(detail="用戶名或密碼輸入錯誤", status_code=400)
    payload = {"username": db_user.username, "exp": exp}
    # 簽發 jwt token
    jwttoken = jwt.encode(payload=payload, key=secrey_key)
    response.set_cookie("jwttoken", jwttoken)

    return db_user


@app.get("/books")
def books(jwttoken: typing.Optional[str] = Cookie(default=None), db: Session = Depends(get_db)):
    # jwt token 解析
    try:
        user_info = jwt.decode(jwttoken, key=secrey_key, algorithms="HS256")
    except PyJWTError:
        raise HTTPException(detail="Invalid jwt_token", status_code=403)
    username = user_info["username"]
    db_user = db.query(User).filter(User.username == username).first()
    if not db_user:
        raise HTTPException(detail="Invalid x_token", status_code=403)
    return [{"id": i + 1, "title": f"books{i}"} for i in range(10)]


if __name__ == '__main__':
    uvicorn.run("main:app", port=8888, reload=True)

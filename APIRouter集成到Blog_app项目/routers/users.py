from fastapi import APIRouter, Depends
import crud
from database import get_db
from schamas import UserOut, UserIn
from sqlalchemy.orm import Session

router = APIRouter()


@router.get("/users")
def get_users(page: int = 1, size: int = 3, db: Session = Depends(get_db)):
    return crud.get_users(page, size, db)


@router.get("/user/{user_id}", response_model=UserOut)
def get_user_by_id(user_id: int, db: Session = Depends(get_db)):
    return crud.get_user_by_id(user_id, db)


@router.delete("/users/{user_id}")
def delete_user_by_id(user_id: int, db: Session = Depends(get_db)):
    crud.delete_user_by_id(user_id, db)
    return {"code": 200, "msg": "OK"}


@router.post("/user", response_model=UserOut)
def create_user(user: UserIn, db: Session = Depends(get_db)):
    return crud.create_user(user, db)


@router.put("/user/{user_id}")
def update_user_by_id(user_id: int, user: UserIn, db: Session = Depends(get_db)):
    return crud.update_user_by_id(user_id, user, db)

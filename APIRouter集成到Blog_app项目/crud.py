from sqlalchemy.orm import Session
from models import User
from fastapi import HTTPException
from schamas import UserIn


def get_users(page: int, size: int, db: Session):
    users = db.query(User).all()
    print(users[(page - 1) * size: page * size])
    users = users[(page - 1) * size: page * size]
    return [{"id": u.id, "name": u.name} for u in users]


def get_user_by_id(user_id: int, db: Session):
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(detail="Not found", status_code=404)
    return user


def delete_user_by_id(user_id: int, db: Session):
    db.query(User).filter_by(id=user_id).delete()
    db.commit()


def create_user(user: UserIn, db: Session):
    # db.add(User(name=user.name, password=user.password))
    db_user = User(**user.dict())
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return


def update_user_by_id(user_id: int, user: UserIn, db: Session):
    db_user = db.query(User).filter(User.id == user_id).first()
    if not db_user:
        raise HTTPException(detail="Not found", status_code=404)
    db_user.name = user.name
    db_user.password = user.password
    db.commit()
    db.refresh(db_user)
    return db_user

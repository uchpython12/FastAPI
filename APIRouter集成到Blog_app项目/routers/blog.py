from fastapi import APIRouter,Depends
from database import get_db
from sqlalchemy.orm import Session
router = APIRouter()

@router.get("/blogs")
def get_blogs():
    pass

@router.get("/blogs/{blog_id}")
def get_blog_by_id():
    pass

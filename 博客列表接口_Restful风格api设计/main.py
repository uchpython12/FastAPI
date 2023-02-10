import typing

import uvicorn
from fastapi import FastAPI ,HTTPException,status
from pydantic import BaseModel
from fastapi.encoders import jsonable_encoder
app = FastAPI(title="博客 CRUD")

# mock db
blogs={
    1:{
        "id": 1,
        "title":"blog1",
        "body":"this is a blog1",
        "desc": "desc"
    },
    2:{
        "id": 2,
        "title": "blog2",
        "body": "this is a blog2",
        "desc": "desc"
    }
}
class Blog(BaseModel):
    title : typing.Optional[str] =None
    body : typing.Optional[str] =None
    desc : typing.Optional[str] =None

@app.get('/blogs',tags=["查詢"])
def get_books(page: int =1 , size: int = 10):
    blogs_list = list(blogs.values())
    return blogs_list[(page-1)*size:page*size]

@app.get('/blogs',tags=["查詢"])
def get_blogs_id(blogs_id:int):
    blog = blogs.get(blogs_id)
    if not blog:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"BLOG WITH ID: {blogs_id}"
        )
    return blog

@app.post('/blog',tags=["查詢"])
def create_blog(blog : Blog):
    blog_id = len(blogs)+1
    blogs[blog_id]= {
        "id":blog_id, **jsonable_encoder(blog)}
    return blogs[blog_id]

@app.put("/blog",tags=["查詢"])
def update_blog(blog_id :int ,blog : Blog):
    to_update_blog = blogs.get(blog_id)
    if not to_update_blog:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"BLOG WITH ID: {blog_id}"
        )
    to_update_blog.update(jsonable_encoder(blog))
    blogs[blog_id] = jsonable_encoder(blog)
    return to_update_blog

@app.patch("/blog",tags=["查詢"])
def update_blog2(blog_id :int ,blog : Blog):
    to_update_blog = blogs.get(blog_id)
    if not to_update_blog:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"BLOG WITH ID: {blog_id}"
        )
    to_update_blog.update(** jsonable_encoder(blog,exclude_unset=True))
    blogs[blog_id] = jsonable_encoder(blog)
    return to_update_blog

@app.delete("/blog",tags=["查詢"])
def delete_blog(blog_id: int):
    if not blogs.get(blog_id):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail = f"BLOG WITH ID: {blog_id}"
        )
    return blogs.pop(blog_id,None)

if __name__ == '__main__':
    uvicorn.run("main:app",port=8888,reload=True)
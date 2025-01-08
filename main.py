'''Модуль main'''
from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from database import Session
import crud
from models.user import User
from models.post import Post

app = FastAPI()

def get_db():
    '''Создание сессии'''
    db = Session()
    try:
        yield db
    finally:
        db.close()

@app.post("/users/")
def create_user(username: str, email: str, password: str, db: Session = Depends(get_db)):
    '''Создание пользователя'''
    return crud.create_user(db, username, email, password)

@app.post("/posts/")
def create_post(title: str, content: str, user_id: int, db: Session = Depends(get_db)):
    '''Создание поста'''
    return crud.create_post(db, title, content, user_id)

@app.get("/users/")
def read_users(db: Session = Depends(get_db)):
    '''Вывод пользователей'''
    return crud.get_all_users(db)

@app.get("/posts/")
def read_posts(db: Session = Depends(get_db)):
    '''Вывод поста'''
    return crud.get_all_posts(db)

@app.get("/posts/user/{user_id}")
def read_posts_by_user(user_id: int, db: Session = Depends(get_db)):
    '''Вывод поста по пользователю'''
    return crud.get_posts_by_user(db, user_id)

@app.put("/users/{user_id}/email")
def update_user_email(user_id: int, new_email: str, db: Session = Depends(get_db)):
    '''Обновление посты юзера'''
    return crud.update_user_email(db, user_id, new_email)

@app.put("/posts/{post_id}/content")
def update_post_content(post_id: int, new_content: str, db: Session = Depends(get_db)):
    '''Обновление поста'''
    return crud.update_post_content(db, post_id, new_content)

@app.delete("/posts/{post_id}")
def delete_post(post_id: int, db: Session = Depends(get_db)):
    '''Удаление поста'''
    crud.delete_post(db, post_id)
    return {"message": "Пост удален"}

@app.delete("/users/{user_id}")
def delete_user(user_id: int, db: Session = Depends(get_db)):
    '''Удаление юзера'''
    crud.delete_user(db, user_id)
    return {"message": "Пользователь и его посты удалены"}

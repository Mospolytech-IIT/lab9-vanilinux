'''Операции crud'''
from sqlalchemy.orm import Session
from models.user import User
from models.post import Post

def create_user(db: Session, username: str, email: str, password: str):
    '''Создание пользователя'''
    user = User(username=username, email=email, password=password)
    db.add(user)
    db.commit()
    db.refresh(user)
    return user

def create_post(db: Session, title: str, content: str, user_id: int):
    '''Создание поста'''
    post = Post(title=title, content=content, user_id=user_id)
    db.add(post)
    db.commit()
    db.refresh(post)
    return post

def get_all_users(db: Session):
    '''Получение всех пользователей'''
    return db.query(User).all()

def get_all_posts(db: Session):
    '''Получение постов'''
    return db.query(Post).join(User).all()

def get_posts_by_user(db: Session, user_id: int):
    '''Получение поста по пользователю'''
    return db.query(Post).filter(Post.user_id == user_id).all()

def update_user_email(db: Session, user_id: int, new_email: str):
    '''Обновление почты'''
    user = db.query(User).filter(User.id == user_id).first()
    user.email = new_email
    db.commit()
    return user

def update_post_content(db: Session, post_id: int, new_content: str):
    '''Обновление поста'''
    post = db.query(Post).filter(Post.id == post_id).first()
    post.content = new_content
    db.commit()
    return post

def delete_post(db: Session, post_id: int):
    '''Удаление поста'''
    post = db.query(Post).filter(Post.id == post_id).first()
    db.delete(post)
    db.commit()

def delete_user(db: Session, user_id: int):
    '''Удаление пользователя'''
    user = db.query(User).filter(User.id == user_id).first()
    db.delete(user)
    db.commit()

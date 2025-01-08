'''Подключение к бд'''
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from models.user import User
from models.post import Post

DATABASE_URL = 'mysql+pymysql://root:Basik787@localhost/laba9'

engine = create_engine(DATABASE_URL)
Base = declarative_base()

Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)

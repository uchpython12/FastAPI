import pymysql
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import Session
# 使用pymysql作为MySQLdb
pymysql.install_as_MySQLdb()
# 指定连接的MySQL数据库
DATABASE_URL = "mysql://root:p12345@localhost:3306/db"
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine)


def get_db():
    db :Session= SessionLocal()
    try:
        yield db
    finally:
        db.close()
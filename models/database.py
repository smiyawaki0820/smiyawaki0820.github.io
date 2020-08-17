"""
- ここで生成されたBaseオブジェクトを前述のOnegaiContentクラスの引数に渡す
- DB接続情報とテーブル定義を紐付ける

- DB接続情報（接続先のDB等）を変えたい場合はdatabase.py
- テーブル定義を変えたい場合はmodels.py
"""

import os

from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

from models.models import *


cwd = os.path.abspath(os.path.dirname(__file__))
f_db = os.path.join(cwd, 'onegai.db')

# SQLiteを利用して1.でf_db にDBを構築
engine = create_engine('sqlite:///' + f_db, convert_unicode=True)

# DB接続用インスタンスを生成
db_session = scoped_session(sessionmaker(autocommit=False,autoflush=False,bind=engine))

# Baseオブジェクトを生成
Base = declarative_base()

# そこにDBの情報を流し込む
Base.query = db_session.query_property()


def init_db():
    Base.metadata.create_all(bind=engine)

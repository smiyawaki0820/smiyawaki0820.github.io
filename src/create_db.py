import os
import sys
sys.path.append(os.getcwd())

from models.database import *
from models.models import *


def create_db():
    c1 = OnegaiContent("お願いします","5000兆円ください")
    c2 = OnegaiContent("助けてください","ぽんぽんぺいん")
    c3 = OnegaiContent("許してください","なんでもしますから")
    db_session.add(c1)
    db_session.add(c2)
    db_session.add(c3)
    db_session.commit()


def run():
    init_db()
    create_db()


if __name__ == '__main__':
    run()

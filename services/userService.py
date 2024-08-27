from sqlalchemy.orm import Session
from database import db
from models.user import User

def save(user_data):
    with Session(db.engine) as session:
        with session.begin():
            new_user = User(username=user_data['username'], password=user_data['password'], role=user_data['role'])
            session.add(new_user)
            session.commit()

        session.refresh(new_user)
        return new_user
    
def getAll():
    with Session(db.engine) as session:
        users = session.query(User).all()
        print(users)
        return users
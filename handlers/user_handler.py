from models.user import User
from app import db

def get_users():
    return [user.to_dict() for user in User.query.all()]

def get_user_by_id(user_id):
    user = User.query.get(user_id)
    if user:
        return user.to_dict()
    return None

def create_user(name, email):
    user = User(name=name, email=email)
    db.session.add(user)
    db.session.commit()
    return user.to_dict()

def update_user(user_id, name, email):
    user = User.query.get(user_id)
    if user:
        user.name = name
        user.email = email
        db.session.commit()
        return user.to_dict()
    return None

def delete_user(user_id):
    user = User.query.get(user_id)
    if user:
        db.session.delete(user)
        db.session.commit()
        return True
    return False

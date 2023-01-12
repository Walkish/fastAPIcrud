from sqlalchemy.orm import Session
from models import UserModel
from schemas import UserSchema


async def get_user_by_id(db: Session, user_id: int):
    return db.query(UserModel.User).filter(UserModel.User.user_id == user_id).first()


async def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(UserModel.User).offset(skip).limit(limit).all()

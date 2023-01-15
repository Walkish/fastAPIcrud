from sqlalchemy.orm import Session
from app.models import UserModel
from app.schemas import UserSchema


async def get_user(
    db: Session,
    user_id: int,
):
    return db.query(UserModel.User).filter(UserModel.User.user_id == user_id).first()


async def update_user(
    user_db: UserModel,
    db: Session,
    user: UserSchema.UserIn,
):
    user_db.name = user.name
    user_db.company = user.company
    user_db.address = user.address
    user_db.city = user.city

    db.merge(user_db)
    db.commit()
    db.refresh(user_db)
    return user_db


async def create_user(
    db: Session,
    user: UserSchema.User,
):
    user_db = UserModel.User(
        user_id=user.user_id,
        name=user.name,
        company=user.company,
        address=user.address,
        city=user.city,
    )

    db.add(user_db)
    db.commit()
    db.refresh(user_db)
    return user_db

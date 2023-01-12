from typing import List
from fastapi import Depends, FastAPI
from sqlalchemy.orm import Session

from schemas import UserSchema
from models import UserModel
from services import user_service
from configs.postgres_database import SessionLocal, engine

UserModel.Base.metadata.create_all(bind=engine)

app = FastAPI()


def get_db():
    with SessionLocal() as db:
        return db


@app.get("/v1/user/", response_model=UserSchema.Users)
async def get_user_by_id(user_id: int, db: Session = Depends(get_db)):
    return await user_service.get_user_by_id(db, user_id=user_id)


@app.get("/v1/users/", response_model=List[UserSchema.Users])
async def get_users(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return await user_service.get_users(db, skip=skip, limit=limit)

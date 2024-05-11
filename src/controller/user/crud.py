from sqlalchemy.exc import ArgumentError
from sqlalchemy.orm import Session
from src.db.connection import PostgreSQLConnection
from src.models.user import User


db = PostgreSQLConnection(dbname='postgres', user='myuser', password='mypassword')

async def c_create_user(user: User):
    db.connect()
    db.insert_user(
        id=user.id, 
        name=user.name, 
        area=user.area, 
        job_description=user.job_description, 
        role=user.role,
        salary=user.salary,
        last_evaluation=user.last_evaluation,
        is_active=True
        )
    db.close()
    return user

async def c_get_user(user_id: int):
    db.connect()
    user = db.execute_query(f"Select * from users where id = {user_id}")
    db.close()
    return user


async def c_delete_user(user_id: int):
    db.connect()
    user = db.delete_user(user_id)
    db.close()
    return user


async def c_update_user(user: User):
    db.connect()
    user = db.update_user(user.id, user.name, user.area, user.job_description, user.role, user.salary, user.is_active, user.last_evaluation)
    db.close()
    return user
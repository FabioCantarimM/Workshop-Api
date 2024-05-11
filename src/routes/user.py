from fastapi import FastAPI, HTTPException
from src.models.user import User
from src.controller.user.crud import c_create_user, c_delete_user, c_get_user, c_update_user

app = FastAPI()

db_users = {}

@app.get("/users/{user_id}")
async def get_user(user_id: int):
    db_users = await c_get_user(user_id)
    if user_id is None:
        raise HTTPException(status_code=404, detail="Usuário não encontrado")
    return db_users

@app.post("/users/")
async def create_user(user: User):
    db_users = await c_get_user(user.id)
    if db_users:
        raise HTTPException(status_code=400, detail="O usuário já existe")
    await c_create_user(user)
    return {"message": "Usuário criado com sucesso"}

@app.put("/users/{user_id}")
async def update_user(user_id: int, user: User):
    db_users = await c_get_user(user_id)
    if db_users is None:
        raise HTTPException(status_code=404, detail="Usuário não encontrado")
    await c_update_user(user)
    return {"message": "Usuário atualizado com sucesso"}

@app.delete("/users/{user_id}")
async def delete_user(user_id: int):
    db_users = await c_get_user(user_id)
    if db_users is None:
        raise HTTPException(status_code=404, detail="Usuário não encontrado")
    await c_delete_user(user_id)
    return {"message": "Usuário excluído com sucesso"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)

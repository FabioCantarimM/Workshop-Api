from fastapi import FastAPI, HTTPException
from src.models.user import User

app = FastAPI()

db_users = {}

@app.get("/users/{user_id}")
async def get_user(user_id: int):
    if user_id not in db_users:
        raise HTTPException(status_code=404, detail="Usuário não encontrado")
    return db_users[user_id]

@app.post("/users/")
async def create_user(user: User):
    if user.id in db_users:
        raise HTTPException(status_code=400, detail="O usuário já existe")
    db_users[user.id] = user
    return {"message": "Usuário criado com sucesso"}

@app.put("/users/{user_id}")
async def update_user(user_id: int, user: User):
    if user_id not in db_users:
        raise HTTPException(status_code=404, detail="Usuário não encontrado")
    db_users[user_id] = user
    return {"message": "Usuário atualizado com sucesso"}

@app.delete("/users/{user_id}")
async def delete_user(user_id: int):
    if user_id not in db_users:
        raise HTTPException(status_code=404, detail="Usuário não encontrado")
    del db_users[user_id]
    return {"message": "Usuário excluído com sucesso"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)

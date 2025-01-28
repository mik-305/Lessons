from typing import List, Optional
from fastapi import FastAPI, HTTPException, Path
from pydantic import BaseModel

app = FastAPI()

                # Список всех пользователей
users: List[dict] = []

                # Класс пользователя
class User(BaseModel):
    id: int
    username: str
    age: int

                # Получение списка всех пользователей
@app.get("/users")
async def get_users():
    return {"users": users}

                # Подготовка к  ведению нового пользователя
@app.post("/user")
async def add_user(username: str, age: int):
                # Генерация уникального ID для нового пользователя
    new_id = max([user["id"] for user in users], default=0) + 1

                # Создание нового пользователя
    new_user = {"id": new_id, "username": username, "age": age}
    users.append(new_user)
    return {"message": "Пользователь был создан", "user": new_user}

                # Обновление уже существующего пользователя(если такой имеется)
@app.put("/user/{user_id}")
async def update_user(
    user_id: int,
    username: Optional[str] = None,
    age: Optional[int] = None,
):
                 # Поиск пользователя по ID
    for user in users:
        if user["id"] == user_id:
            if username is not None:
                user["username"] = username
            if age is not None:
                user["age"] = age
            return {"message": "Пользователь был обновлён", "user": user}
    raise HTTPException(status_code=404, detail="Пользователь не найден")

                # Удаление существующего пользователя
@app.delete("/user/{user_id}")
async def delete_user(user_id: int):
                # Ищем пользователя по ID
    for user in users:
        if user["id"] == user_id:
            users.remove(user)
            return {"message": f"Пользователь с ID {user_id} был удалён"}
    raise HTTPException(status_code=404, detail="Пользователь не найден")

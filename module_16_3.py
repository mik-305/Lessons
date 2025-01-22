from fastapi import FastAPI, HTTPException, Path
from typing import Annotated

app = FastAPI()

users = {
    "1": "Имя: Example, возраст: 18"
}

@app.get("/users")
async def get_users():                                    # Получения списка всех пользователей
    return users

@app.post("/user/{username}/{age}")                      # Добавления нового пользователя.
async def add_user(
        username: str,
        age: Annotated[
        int,
        Path(
            title="ВВедите возраст пользователя",
            description="Возраст пользователя, должен быть целым числом между 17 и 100 включительно.",
            ge=17,          # Мин. допустимый возраст
            le=100,         # Макс. допустимый возраст
            example=1
        )
    ]):
    max_key = max(map(int, users.keys())) if users else 0           # Выбираем максимальное значение
    new_key = str(max_key + 1)
    users[new_key] = f"Имя: {username}, возраст: {age}"
    return f"Пользователь c id: {new_key} был создан"

@app.put("/user/{user_id}/{username}/{age}")
async def update_user(user_id: str, username: str, age: int):        # Обновление существующего пользователя
    if user_id not in users:
        raise HTTPException(status_code=404, detail=f"Пользователь с id: {user_id} не найден")
    users[user_id] = f"Имя: {username}, возраст: {age}"
    return f"Пользователь с id: {user_id} был обновлён"

@app.delete("/user/{user_id}")
async def delete_user(user_id: str):                                # Удаление существующего пользователя
    if user_id not in users:
        raise HTTPException(status_code=404, detail=f"Пользователь с id: {user_id} не найден")
    del users[user_id]
    return f"Пользователь с id:  {user_id} был удалён"


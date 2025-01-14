from fastapi import FastAPI, Path
from typing import Annotated

app = FastAPI()  # Создаем экземпляр приложения FastAPI

@app.get("/")
async def get_main_page():
    return "Главная страница"

@app.get("/user/admin")
async def get_admin_page():
    return "Вы вошли как администратор"

@app.get("/user/{user_id}")
async def get_user_info(
    user_id: Annotated[
        int,
        Path(
            title="Enter User ID",
            description="ID пользователя, должен быть целым числом между 1 и 100 включительно.",
            ge=1,
            le=100,
            example=1
        )
    ]
):
    return f"Вы вошли как пользователь № {user_id}"

@app.get("/user/{username}/{age}")
async def read_user_info(
    username: Annotated[
        str,
        Path(
            title="Enter username",
            description="Имя пользователя, должно быть строкой длиной от 5 до 20 символов.",
            min_length=5,
            max_length=20,
            example="Сигизмунд"
        )
    ],
    age: Annotated[
        int,
        Path(
            title="Enter age",
            description="Возраст пользователя, должен быть целым числом от 18 до 120.",
            ge=18,
            le=120,
            example=77
        )
    ]
):
    return f"Информация о пользователе. Имя: {username}, Возраст: {age}"

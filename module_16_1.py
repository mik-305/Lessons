from fastapi import FastAPI

app = FastAPI()         # Создаем экземпляр приложения FastAPI

@app.get("/")
async def get_main_page():
    return {"message": "Главная страница"}

@app.get("/user/admin")
async def get_admin_page():
    return {"message": "Вы вошли как администратор"}

@app.get("/user/{user_id}")
async def get_user_info(user_id: int):
    return {"message": f"Вы вошли как пользователь № {user_id}"}

@app.get("/user")
async def read_user_info(username: str = "Не_указан", age: int = 0):
    return {"message": f"Информация о пользователе. Имя: {username}, Возраст: {age}"}

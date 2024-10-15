from fastapi import FastAPI, Path
from typing import Annotated

app = FastAPI()

# Главная страница
@app.get("/")
def read_root():
    return {"message": "Главная страница"}

# Страница администратора
@app.get("/user/admin")
def read_admin():
    return {"message": "Вы вошли как администратор"}

# Страница пользователя с параметром user_id и валидацией
@app.get("/user/{user_id}")
def read_user(
    user_id: Annotated[int, Path(description="Enter User ID", ge=1, le=100, examples={"example": 1})]
):
    return {"message": f"Вы вошли как пользователь № {user_id}"}

# Страница пользователя с параметрами username и age и валидацией
@app.get("/user/{username}/{age}")
def read_user_info(
    username: Annotated[str, Path(description="Enter username", min_length=5, max_length=20, examples={"example": "UrbanUser"})],
    age: Annotated[int, Path(description="Enter age", ge=18, le=120, examples={"example": 24})]
):
    return {"message": f"Информация о пользователе. Имя: {username}, Возраст: {age}"}

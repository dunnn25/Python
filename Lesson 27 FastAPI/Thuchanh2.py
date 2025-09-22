from fastapi import FastAPI

app = FastAPI()

@app.get("/user/{user_id}") # user_id - sẽ được sử dụng trong hàm bên dưới
def get_user(user_id):
    return {"user_id": user_id}
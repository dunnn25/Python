from fastapi import FastAPI

app = FastAPI()

@app.get("/search")
def search_user(name, age=None): # do tuổi đã có giá trị mặc định là None nên không bắt buộc phải truyền
    return {"name": name, "age": age}

# http://127.0.0.1:8000/search?name=Dung&age=21
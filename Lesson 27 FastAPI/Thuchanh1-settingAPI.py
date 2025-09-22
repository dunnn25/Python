from fastapi import FastAPI

# Taoj API intance
app = FastAPI()

# Đi tạo một API
@app.get("/hello") # /hello - route định tuyến đường dẫn
def read_root():
    return {"Hello": "dWorl"}

# uvicorn <ten_file>:<ten_instance> --reload
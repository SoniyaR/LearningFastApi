from fastapi import FastAPI, Path, Body

app = FastAPI()

students = {
    1 : {
        "name": "mindy",
        "age": 27
    },
    2 : {
        "name": "chloe",
        "age": 24
    }
}

@app.get("/")
def index():
    return {"name":"first data"};

@app.get("/get-student/{id}")
def get_student(id: int):# = Path(None, description = "students id to get details")):
    return students[id];

@app.get("/get-student")
def get_student(name: str = None):
    for sid in students:
        if students[sid]["name"] == name:
            return students[sid]
    return {"data": "not found"}

    
@app.post("/createStudent")
def create_student(payload: dict = Body(...)):
    print(payload)
    return {"data":"Student created!"}
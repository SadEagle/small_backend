from fastapi import APIRouter

app_answers = APIRouter(prefix="/answers")


@app_answers.get("/{id}")
def get_id_answer(id: int):
    pass


@app_answers.delete("/{id}")
def delete_id_answer(id: int):
    pass

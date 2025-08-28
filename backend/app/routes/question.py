from fastapi import APIRouter


app_questions = APIRouter(prefix="/questions")


@app_questions.get("/")
def get_questions():
    pass


@app_questions.get("/{id}")
def get_id_question(id: int):
    pass


@app_questions.post("/{id}")
def create_questions(id: int):
    pass


@app_questions.delete("/{id}")
def delete_id_question(id: int):
    pass


@app_questions.post("/{id}/answers")
def add_answer_id_question(id: int):
    pass

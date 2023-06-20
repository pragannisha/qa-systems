from fastapi import FastAPI
from pydantic import BaseModel
from transformers import BertForQuestionAnswering, BertTokenizer, pipeline

model_name = 'bert-large-uncased-whole-word-masking-finetuned-squad'
models = BertForQuestionAnswering.from_pretrained(model_name)
tokenizer = BertTokenizer.from_pretrained(model_name)
nlp = pipeline("question-answering", model=models, tokenizer=tokenizer)


app = FastAPI()

class QuestionContext(BaseModel):
    question: str
    context: str

class Answer(BaseModel):
    answer: str

@app.post('/predict', response_model=Answer)
def predict_answer(question_context: QuestionContext):
    answer = nlp({'question': question_context.question, 'context': question_context.context})
    return Answer(answer=answer['answer'])


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app:app", host="0.0.0.0", port=8000)

from fastapi import FastAPI

from detoxify import Detoxify

app = FastAPI()

@app.get("/api/v1")
def read_root():
    return {"status": "Success"}

@app.get("/api/v1/health")
def health():
    return {"status": "Success"}


@app.get("/api/v1/analyze")
def analyze(text: str):
    predictions = Detoxify("unbiased-small").predict(text)
    return {
        "status": "Success",
        "predictions": {
            k: float(v) for k, v in predictions.items()
        }
    }
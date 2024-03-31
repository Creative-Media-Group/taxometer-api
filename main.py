import fastapi as fi

app = fi.FastAPI()


@app.get("/")
def taxometer():
    return {"Test": "Test"}

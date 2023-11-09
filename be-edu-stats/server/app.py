from fastapi import FastAPI

app = FastAPI(
    title="Query builder",
    description="Visual query builder API REST",
    version="0.0.1",
)


@app.get("/")
def read_root():
    return {"message": "How's it going?"}

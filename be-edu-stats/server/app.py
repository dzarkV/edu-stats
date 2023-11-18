from fastapi import FastAPI
from routes.indicator import indicator_router

app = FastAPI(
    title="Query colombian education indicators",
    description="Visual query builder API",
    version="0.0.1",
)

app.include_router(indicator_router)


@app.get("/")
def read_root():
    return {"message": "How's it going?"}

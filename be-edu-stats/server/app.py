from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes.indicator import indicator_router

description = """
Visual query builder API. 🚀

## Indicators

You can **read indicators**, specially from Colombian primary and secondary education, 
from world bank international education dataset.

You will be able to:

* **Read indicators**.
* **Save indicators with comments** (_not implemented_yet_).
"""

app = FastAPI(
    title="Query colombian education indicators",
    description=description,
    version="0.0.1"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:9000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(indicator_router)


@app.get("/")
def read_root():
    return {"message": "How's it going?"}

from app.router import predict

from fastapi import FastAPI
import uvicorn

app = FastAPI()

app.include_router(predict.router, prefix="/gfk", tags=["product_group_classification"])

if __name__ == "__main__":
	uvicorn.run(app, host="0.0.0.0", port=8000)
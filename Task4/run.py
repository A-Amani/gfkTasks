from fastapi import FastAPI, Query
from inferenece import run_regressor
import uvicorn

app = FastAPI()

@app.get("/predict")
async def predict(house_size_ft2: float = Query(..., gt=750, st=3125)):

    res = run_regressor(house_size_ft2)[0]

    return {"message": f"The price for house with size {house_size_ft2} ft^2 is {res}k $"}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
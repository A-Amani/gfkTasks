from typing import List, Optional

from fastapi import APIRouter, Query, HTTPException
from loguru import logger
import pandas as pd

from Modelling.Model import Model
from FeatEng.FeatureEngineering import FeatEngineering
from config import *

router = APIRouter()


@router.get("/heartbeat", tags=["product_group_classification"])
async def heartbeat():
    return {"message": "Hello GfK! I'm alive!"}


@router.get("/predict", tags=["product_group_classification"])
async def predict(main_text: str = Query(...),
                  add_text: Optional[str] = "",
                  manufacturer: Optional[str] = ""
                  ):
    try:
        classifier = Model(run_mode="predict")
        data = pd.DataFrame([[main_text, add_text, manufacturer]], columns=config["feature_col"])

        feature_handler = FeatEngineering(run_mode="predict")
        pdf = feature_handler.do_feature_engineering(data)

        res = classifier.run(data=pdf)[0]

        return {"message": f"{res}"}
    except Exception as ex:
        logger.opt(exception=True).error(ex.__traceback__)
        raise HTTPException(status_code=422, detail="internal error occurred while running classification!")

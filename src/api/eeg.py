from fastapi import APIRouter
import pandas as pd

router = APIRouter()

@router.get("/eegdata", tags=["ЭЭГ датасет"], summary="Получить данные из датасета")
async def get_eeg_data():
    df = pd.read_csv('E:\develope\python\pyneiro\src\las.csv', header=None)
    df = df.apply(pd.to_numeric, errors='coerce').dropna()
    signal = df.iloc[:, 1:].values
    
    return {"signal": signal.tolist()}

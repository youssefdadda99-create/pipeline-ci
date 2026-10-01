from fastapi import FastAPI
import pandas as pd



app = FastAPI()

data = pd.read_csv("./not_rusty.csv")

@app.get("/data")
def get_rusty_data():
    return data.to_dict()


@app.get("/")
def health():
    return "server working good"
#!/usr/bin/env python

from fastapi import FastAPI
import uvicorn
from process_data import filter_state

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello, welcome to the covid-19 cases dataset, lets's begin to search covid-19 cases data in US from 2020-1-21 to 2022-5-23!"}

@app.get("/{statename}")
async def query(statename):
    """Execute query from covid-19 cases dataset to search covid-19 cases data in US from 2020-1-21 to 2022-5-23!"""

    result = filter_state(statename)
    string = "Latest Result for {} is: \n {}".format(statename,result)
    return {string}


if __name__ == '__main__':
    uvicorn.run(app, port=8080, host='0.0.0.0')
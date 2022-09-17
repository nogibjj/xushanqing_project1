#!/usr/bin/env python
import pandas as pd
df = pd.read_csv('us-counties.csv')
def filter_state(state):
    if not isinstance(state,str):
        print("Please input a valid state name!")
        return "Please input a valid state name!"
    state_data= df[df['state'] == state]
    if len(state_data) == 0:
        print("Please input a valid state name!")
        return "Please input a valid state name!"
    else:
        return state_data.tail(1)
    
filter_state("Washington")

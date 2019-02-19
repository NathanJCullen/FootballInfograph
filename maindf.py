import pandas as pd
import numpy as np
import datetime
import request as rq

def create_df():
    pd.set_option('display.max_columns', 1000)
    pd.set_option('display.max_colwidth', 1000)
    pd.set_option('display.width', None)

    df = pd.read_csv("E0.csv")

    df = df[['Date', 'HomeTeam', 'AwayTeam', 'FTHG', 'FTAG', 'HTHG', 'HTAG', 'HS', 'AS', 'HST', 'AST', 'HY', 'AY', 'HR', 'AR']]
    df['Date'] = pd.to_datetime(df['Date'], format='%d/%m/%Y')
    df.set_index('Date', inplace=True)
    df = df.sort_values('Date')
    df['goals_scored'] = df['FTHG'] + df['FTAG']
    df['total_yellow'] = df['HY'] + df['AY']
    df['total_red'] = df['HR'] + df['AR']
    df['total_shots'] = df['HS'] + df['AS']
    df['total_shots_target'] = df['HST'] + df['AST']
    return df
# Scripts voor data laden en verwerken
import numpy as np
import pandas as pd


def load_data(file_path: str) -> pd.DataFrame:
    column_names = ['DateTime', 'Open', 'High', 'Low', 'Close', 'Volume']
    data = pd.read_csv(file_path, names=column_names, header=None)

    return data 

def remove_rows_with_missing_values(data: pd.DataFrame) -> pd.DataFrame:
    data = data.dropna()

    return data

def convert_datatime(data: pd.DataFrame) -> pd.DataFrame:
    data['DateTime'] = pd.to_datetime(data['DateTime'])

    return data

def remove_duplicate_rows(data: pd.DataFrame) -> pd.DataFrame:
    data = data.drop_duplicates(keep=False)

    return data

def add_MA50(data: pd.DataFrame) -> pd.DataFrame:
    data['MA50'] = data['Close'].rolling(window=50).mean()

    return data

def add_MA200(data: pd.DataFrame) -> pd.DataFrame:
    data['MA200'] = data['Close'].rolling(window=200).mean()

    return data

def add_technical_indicators(data: pd.DataFrame) -> pd.DataFrame:
    data = add_MA50(data)
    data = add_MA200(data)

    return data


def clean_data(data: pd.DataFrame) -> pd.DataFrame:
    data = remove_rows_with_missing_values(data)
    data = convert_datatime(data)
    data = remove_duplicate_rows(data)
    data = add_technical_indicators(data)


    print("Data na het schoonmaken:")
    print(data.head())

    return data


def get_data(file_path: str) -> pd.DataFrame:
    data = load_data(file_path)
    data = clean_data(data)

    return data


data = get_data("data/raw/eurousd_1h_2008_2024.csv")

import requests
import warnings
import pandas as pd


class Pipeline:
    def __init__(self):
        self.api_status_url = 'https://api.covidtracking.com/v1/status.json'
        self.api_current_url = 'https://api.covidtracking.com/v1/states/current.json'
        self.api_historical_url = 'https://api.covidtracking.com/v1/states/daily.json'
        self.resp = None
        self.df = None

    def retrieve(self, url: str):
        try:
            resp = requests.get(url)
        except Exception as e:
            print(e)

        if resp.status_code == 200:
            self.resp = resp
            self.df = pd.DataFrame(self.resp.json())
        else:
            warnings.warn(f"Response returned with status {resp.status_code}")

    def retrieve_status(self):
        self.retrieve(self.api_current_url)

    def retrieve_current(self):
        self.retrieve(self.api_current_url)

    def retrieve_historical(self):
        self.retrieve(self.api_historical_url)

    def clean_dates(self):
        df = self.df.copy()
        df['dates'] = pd.to_datetime(df['dates'], format='%Y%m%d')
        self.df = df

    def write_csv(self, filename: str):
        self.df.to_csv(filename,
                       index=False)

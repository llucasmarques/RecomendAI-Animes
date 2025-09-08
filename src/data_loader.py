import pandas as pd

class AnimeDataLoader:
    def __init__(self, original_csv:str,processed_csv:str):
        self.original_csv = original_csv
        self.processed_csv = processed_csv

    def process_data(self):
        df = pd.read_csv(self.original_csv, encoding='utf-8', error_bad_lines=False).dropna()
        required_columns = {'name', 'genres', 'overview'}

        missing = required_columns - set(df.columns)
        if missing:
            raise ValueError("Misssing Column in CSV File")

        df['combined'] = (
            "Title: " + df['name'] + " Overview: " + df['overview'] + " Genres: " + df['genres']
        )

        df[['combined_info']].to_csv(self.processed_csv, index=False, encoding='utf-8')

        return self.processed_csv
        
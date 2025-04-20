import os
import pandas as pd

def read_csv_dataset(directory_path):
    csv_files = [f for f in os.listdir(directory_path) if f.endswith('.csv')]
    dataframes = {}

    for file in csv_files:
        full_path = os.path.join(directory_path, file)
        df = pd.read_csv(full_path)

        # فقط توییت و عواطف آن ذخیره شود
        if 'tweet' in df.columns and 'emotion' in df.columns:
            df = df[['tweet', 'emotion']]

        dataframes[file] = df
    
    # تمام دیتا ها را ترکیب و شافل می‌کنیم
    merged_df = pd.concat(dataframes, ignore_index=True)
    shuffled_df = merged_df.sample(frac=1, random_state=20).reset_index(drop=True)
    return shuffled_df


# dataframes = read_csv_dataset("dataset")

# for filename, df in dataframes.items():
#     print(f"\n--- {filename} ---")
#     print(df.head())
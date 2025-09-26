# data_cleaner_script.py - Python Data Cleaner

import pandas as pd
import numpy as np

def clean_data(df):
    """
    Membersihkan missing values dan menyiapkan DataFrame untuk analisis.
    """
    print("Memulai proses pembersihan data...")
    
    # 1. Menghapus baris dengan missing values (NaN)
    df_cleaned = df.dropna()
    
    # 2. Normalisasi Kolom Numerik (Contoh sederhana)
    if 'value' in df_cleaned.columns:
        min_val = df_cleaned['value'].min()
        max_val = df_cleaned['value'].max()
        df_cleaned['value_normalized'] = (df_cleaned['value'] - min_val) / (max_val - min_val)
        print("Kolom 'value' telah dinormalisasi.")

    return df_cleaned

if __name__ == "__main__":
    print("Data Cleaner Script berhasil dimuat.")
    # data = pd.DataFrame({'id': [1, 2], 'value': [10, 20]})
    # cleaned_df = clean_data(data)
    # print(cleaned_df)

"""
Savor Data :: Various pipeline functions
"""

from os import environ
from pathlib import Path

import pandas as pd


def extract_and_concat_airtable_data(records: dict) -> pd.DataFrame:
    """Extracts fields from the airtable data and concatenates them with airtable id.
    Uses pyjanitor to clean up column names.
    """
    # Load and clean/fix names
    df = (
        pd.DataFrame.from_records(records)
        .clean_names()
        .rename_column("id", "airtable_id")
    )
    df2 = pd.concat(  # Extract `fields` and concat to `airtable_id`
        [df["airtable_id"], df["fields"].apply(pd.Series)], axis=1
    )
    return df2


def convert_datetime_cols(data: pd.DataFrame, dt_cols: list) -> pd.DataFrame:
    """If datetime columns exist in dataframe, convert them to datetime.

    :param data (pd.DataFrame) : DataFrame with datetime cols to be converted.
    :param dt_cols (list) : List of potential datetime cols.
    :return (pd.DataFrame) : DataFrame with datetime cols converted.
    """
    data = data.copy()  # Don't change original dataframe
    for col in dt_cols:
        if col in data.columns:  # Make sure column exists
            data[col] = pd.to_datetime(data[col])
    return data

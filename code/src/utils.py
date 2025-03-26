import pandas as pd
import os




def read_excel(file_path):
    """Reads structured test cases from an Excel file."""
    path = os.path.dirname(__file__)
    excel_folder_path = os.path.join(path, "data")
    excel_file_path = os.path.join(excel_folder_path, "sample_test_cases.xlsx")
    df = pd.read_excel(excel_file_path)
    return df
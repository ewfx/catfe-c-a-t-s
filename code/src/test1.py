import os
from generator import convert_to_bdd
from utils import read_excel





def save_bdd_to_file(bdd_text, output_file="output.feature"):
    """Saves generated BDD test scenarios to a .feature file."""
    with open(output_file, "w") as f:
        f.write(bdd_text)
    print(f"BDD scenarios saved to {output_file}")

if __name__ == "__main__":
    input_file = "sample_test_cases.xlsx" 
    path = os.path.dirname(__file__)
    excel_folder_path = os.path.join(path, "Data")
    excel_file_path = os.path.join(excel_folder_path, "sample_test_cases.xlsx")
    if not os.path.exists(input_file):
        print("Input file not found. Please provide a valid Excel file.")
    else:
        test_cases = read_excel(input_file)
        bdd_text = convert_to_bdd(test_cases)
        save_bdd_to_file(bdd_text)

import pandas as pd
import os

def combine_excel_files(file_paths, output_file="combined.xlsx"):
    combined_df = pd.DataFrame()
    
    for file in file_paths:
        try:
            df = pd.read_excel(file, usecols=["Name", "Email"], dtype=str)
            combined_df = pd.concat([combined_df, df], ignore_index=True)
        except Exception as e:
            print(f"Error: something with {file}: {e}")
    
    combined_df.drop_duplicates(inplace=True)
    combined_df.to_excel(output_file, index=False)
    print(f"New combined file: {output_file}")

if __name__ == "__main__":
    import argparse
    
    parser = argparse.ArgumentParser(description="Combine Excel files and extract Name and Email columns.")
    parser.add_argument("files", nargs="+", help="List of Excel files to combine")
    parser.add_argument("-o", "--output", default="combined.xlsx", help="Output file name (default: combined.xlsx)")
    
    args = parser.parse_args()
    combine_excel_files(args.files, args.output)

import pandas as pd
import glob
import os

def combine_csvs(input_folder, output_file):
    # Get all CSV files in the input folder
    csv_files = glob.glob(os.path.join(input_folder, '*.csv'))
    if not csv_files:
        print(f"No CSV files found in {input_folder}.")
        return
    # Load and concatenate all CSVs
    df_list = [pd.read_csv(f) for f in csv_files]
    combined_df = pd.concat(df_list, ignore_index=True)
    # Ensure output directory exists
    os.makedirs(os.path.dirname(output_file), exist_ok=True)
    # Save combined DataFrame
    combined_df.to_csv(output_file, index=False)
    print(f"Combined {len(csv_files)} files. Output: {output_file} (Rows: {combined_df.shape[0]})")

if __name__ == "__main__":
    project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    input_folder = os.path.join(project_root, 'data', 'raw')
    output_file = os.path.join(project_root, 'data', 'processed', 'combined.csv')
    combine_csvs(input_folder, output_file)

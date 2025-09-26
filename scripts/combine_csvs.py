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
    df_list = []
    for f in csv_files:
        try:
            df_list.append(pd.read_csv(f))
        except Exception as e:
            print(f"Error reading {f}: {e}")
    if not df_list:
        print("No CSVs could be loaded.")
        return
    combined_df = pd.concat(df_list, ignore_index=True)
    # Ensure output directory exists
    os.makedirs(os.path.dirname(output_file), exist_ok=True)
    # Save combined DataFrame
    combined_df.to_csv(output_file, index=False)
    print(f"Combined {len(df_list)} files. Output: {output_file} (Rows: {combined_df.shape[0]})")

if __name__ == "__main__":
    project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    input_folder = os.path.join(project_root, 'data', 'raw')
    output_file = os.path.join(project_root, 'data', 'processed', 'combined.csv')
    combine_csvs(input_folder, output_file)

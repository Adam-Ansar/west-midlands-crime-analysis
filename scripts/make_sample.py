import pandas as pd
import os

def make_sample(input_file, output_file, n=5000, random_state=42):
    # Load cleaned data
    df = pd.read_csv(input_file)
    # Take a random sample
    sample_df = df.sample(n=n, random_state=random_state)
    # Ensure output directory exists
    os.makedirs(os.path.dirname(output_file), exist_ok=True)
    # Save sample
    sample_df.to_csv(output_file, index=False)
    print(f"Sample of {n} rows saved to {output_file}")

if __name__ == "__main__":
    project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    input_file = os.path.join(project_root, 'data', 'processed', 'cleaned_crime.csv')
    output_file = os.path.join(project_root, 'data', 'processed', 'sample_crime.csv')
    make_sample(input_file, output_file)

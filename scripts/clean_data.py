import pandas as pd
import os

def clean_data(input_file, output_file):
    # Load combined data
    df = pd.read_csv(input_file)

    # Drop context column as it's empty
    if 'Context' in df.columns:
        df = df.drop(columns=["Context"])

    # Convert 'Month' to datetime
    if 'Month' in df.columns:
        df["Month"] = pd.to_datetime(df["Month"])

    # Remove duplicates
    df = df.drop_duplicates()

    # Create additional time-based columns
    if 'Month' in df.columns:
        df["Year"] = df["Month"].dt.year
        df["MonthName"] = df["Month"].dt.month_name()
        df["MonthNum"] = df["Month"].dt.month
        season_map = {
            12: "Winter", 1: "Winter", 2: "Winter",
            3: "Spring", 4: "Spring", 5: "Spring",
            6: "Summer", 7: "Summer", 8: "Summer",
            9: "Autumn", 10: "Autumn", 11: "Autumn"
        }
        df["Season"] = df["Month"].dt.month.map(season_map)

    # Fill missing 'Last outcome category' with 'Outcome not recorded'
    if 'Last outcome category' in df.columns:
        df['Last outcome category'] = df['Last outcome category'].fillna('Outcome not recorded')

    # Ensure output directory exists
    os.makedirs(os.path.dirname(output_file), exist_ok=True)
    # Save cleaned data
    df.to_csv(output_file, index=False)
    print(f"Cleaned data saved to {output_file} (Rows: {df.shape[0]})")

if __name__ == "__main__":
    project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    input_file = os.path.join(project_root, 'data', 'processed', 'combined.csv')
    output_file = os.path.join(project_root, 'data', 'processed', 'cleaned_crime.csv')
    clean_data(input_file, output_file)

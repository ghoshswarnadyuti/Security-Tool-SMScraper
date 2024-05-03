import pandas as pd

def generate_report(profile_data):
    """Generates a basic summary report."""
    df = pd.DataFrame(profile_data, index=[0])  # Create a DataFrame

    print("Profile Summary")
    print(df.to_string())  # Simple text-based report
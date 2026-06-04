import requests
import pandas as pd
from pathlib import Path

output_folder = Path("data/raw")
output_folder.mkdir(parents=True, exist_ok=True)

schemes = {
    "HDFC_Top100": 125497,
    "SBI_Bluechip": 119551,
    "ICICI_Bluechip": 120503,
    "Nippon_LargeCap": 118632,
    "Axis_Bluechip": 119092,
    "Kotak_Bluechip": 120841
}

for name, code in schemes.items():

    url = f"https://api.mfapi.in/mf/{code}"

    print(f"Fetching {name}...")

    response = requests.get(url)

    data = response.json()

    nav_df = pd.DataFrame(data["data"])

    file_path = output_folder / f"{name}_NAV.csv"

    nav_df.to_csv(file_path, index=False)

    print(f"Saved: {file_path}")
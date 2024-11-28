import pandas as pd
import matplotlib.pyplot as plt
import os


# Projekt gyökérkönyvtárának meghatározása
projekt_gyoker = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))


def get_bar_chart_data():
    # Adatfájlok elérési útvonalainak beállítása
    file_path =  os.path.join(projekt_gyoker, 'raw_data', 'kor0048.csv')  # Update this to your file path

    # Load the CSV file with the appropriate encoding and delimiter
    data = pd.read_csv(file_path, encoding='latin-1', delimiter=';', header=None)

    # Extract the years from the second row
    years = data.iloc[1, 1:].astype(str).str.extract(r'(\d+)')[0]

    # Identify rows containing "Határérték-túllépés, Hosszú távú célkitûzés-túllépés %"
    target_rows = data[0].str.contains('Határérték-túllépés, Hosszú távú célkitûzés-túllépés %', na=False)

    # Extract rows and the relevant columns for processing (drop the first column with labels)
    target_data = data.loc[target_rows, 1:]

    # Replace ".." with NaN and convert the data to numeric
    target_data = target_data.replace('..', pd.NA).apply(lambda x: x.str.replace(',', '.')).apply(pd.to_numeric, errors='coerce')

    # Compute averages for each year (column)
    averages = target_data.mean(axis=0)

    # Filter valid years and averages for plotting
    valid_years = years[~averages.isna()]
    valid_averages = averages[~averages.isna()]

    # Create the bar graph
    plt.figure(figsize=(14, 7))
    plt.bar(valid_years, valid_averages, color='skyblue', edgecolor='black')
    plt.xlabel('Év')
    plt.ylabel('Átlag %')
    plt.title('A levegő Országos Átlag ózon(O3) koncentráció Határérték-túllépése Évenként')
    plt.xticks(rotation=45)
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.tight_layout()

    # A diagram mentése
    plt.savefig('app/static/images/bar_chart.png')





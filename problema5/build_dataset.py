import requests
import pandas as pd
import sys

def fetch_data(site):
    url = f"https://api.mercadolibre.com/sites/{site}/search?q=tv%204k&condition=new"
    response = requests.get(url)
    data = response.json()
    return data.get('results', [])

def build_dataset(site, filename):
    items = fetch_data(site)
    
    df = pd.DataFrame(items)
    df = df[['id', 'title', 'price', 'domain_id', 'brand']]
    df.columns = ['ITEM_ID', 'TITLE', 'PRICE', 'DOMAIN_ID', 'BRAND']
    
    df.to_csv(filename, index=False)
    print("Dataset built and saved successfully.")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python build_dataset.py <site>")
        sys.exit(1)
    
    site = sys.argv[1]
    filename = "dataset.csv"
    
    build_dataset(site, filename)

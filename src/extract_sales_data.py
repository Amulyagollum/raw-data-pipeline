import requests
from datetime import datetime
import os
import json

RAW_PATH = './data/raw/'
API_ENDPOINTS = {
            'products': 'https://fakestoreapi.com/products',
            'users':'https://fakestoreapi.com/carts',
            'carts': 'https://fakestoreapi.com/users'
}

def fetch_and_save(endpoint, name):
    try:
        response = requests.get(endpoint)
        response.raise_for_status()
        data = response.json()
        
        date_stamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"{RAW_PATH}{name}/{name}_{date_stamp}.json"
        
        os.makedirs(os.path.dirname(filename), exist_ok=True)
        with open(filename, 'w') as f:
            import json
            json.dump(data, f, indent=4)
        print(f"[✓] {name} data saved: {filename}")
    except Exception as e:
        print(f"[✗] Error fetching {name}: {str(e)}")

if __name__ == "__main__":
    for name, url in API_ENDPOINTS.items():
        fetch_and_save(url, name)


    


import pytest
import requests
import config

@pytest.fixture(scope="session")
def auth_headers():
    url = "https://admin.nnaconnected.com/api/idm/api/client_token"

    headers = {
        "API_KEY": config.API_KEY,
        "APP_TYPE": config.APP_TYPE,
        "Content-Type": "application/json"
    }

    payload = {
        "client_id": config.CLIENT_ID,
        "client_secret": config.CLIENT_SECRET,
        "grant_type": "client_credentials"
    }

    response = requests.post(url, headers=headers, json=payload)
        
    # Eğer hata alırsak (200 dönmezse), çökmeden önce gerçek hatayı ekrana bas!
    if response.status_code != 200:
        print(f"\n--- TOKEN API HATASI ---")
        print(f"Status: {response.status_code}")
        print(f"Hata Detayı: {response.text}")
            
    response.raise_for_status()

    print(f"\n---TOKEN API STATUS CODE: {response.status_code} ---")
    print(f"\---TOKEN API Response: {response.text} ---")

    response.raise_for_status()
    token = response.json().get("access_token")

    return {
        "Authorization": f"Bearer {token}",
        "Accept": "application/json",
        "API_KEY": config.API_KEY,
        "APP_TYPE": config.APP_TYPE
    }

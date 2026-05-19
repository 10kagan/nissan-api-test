import requests
import pytest
import config

class TestVehicleLockUnlock:

    def test_lock_returns_200(self,auth_headers):
        url = f"{config.BASE_URL}{config.REMOTE_DOOR_ENDPOINT}"

        payload = {
            "command": "REMOTE_DOOR_LOCK",
            "target": "DOORS_HATCH",
            "vin": config.VIN
        }

        response = requests.post(url, headers=auth_headers, json=payload)

        print(f"\n Lock Status: {response.status_code}")
        print(f" Lock Response: {response.text}")

        assert response.status_code == 200, f"Expected 200, Result {response.status_code}"

    def test_unlock_returns_200(self,auth_headers):
        url = f"{config.BASE_URL}{config.REMOTE_DOOR_ENDPOINT}"

        payload = {
            "command": "REMOTE_DOOR_UNLOCK",
            "target": "DOORS_HATCH",
            "vin": config.VIN
        }

        response = requests.post(url, headers=auth_headers, json=payload)

        print(f"\n UnLock Status: {response.status_code}")
        print(f" Unlock Response: {response.text}")

        assert response.status_code == 200, f"Expected 200, Result {response.status_code}"

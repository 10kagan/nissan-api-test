# Vehicle API Test Automation

This repository contains an automated API testing framework for a B2B Connected Vehicle Platform. It verifies the authentication flow and remote command execution (Lock/Unlock) using Python and Pytest.

## 🛠️ Technologies Used
* **Language:** Python 3
* **Framework:** Pytest
* **HTTP Client:** Requests
* **Architecture:** Modular setup with Pytest Fixtures (`conftest.py`)

## ⚙️ How It Works
1. **Authentication:** The `conftest.py` file dynamically fetches a Bearer Access Token using valid Client Credentials.
2. **Dynamic Headers:** The token is automatically injected into the headers for all subsequent test requests.
3. **Command Execution:** The `test_vehicle.py` suite sends JSON payloads to the API to simulate Remote Door Lock and Unlock commands.
4. **Assertions:** Validates HTTP status codes (200 OK, 401 Unauthorized) and JSON response structures.

## 🚀 Setup & Installation
1. Clone the repository.
2. Install dependencies: `pip install -r requirements.txt`
3. Create a `config.py` file based on the provided `config_template.py` and fill in your actual API credentials.
4. Run the tests: `python -m pytest -v -s`
2. Adım: Kullanım Kılavuzu (config_template.py)

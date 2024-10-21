import requests
import json

# Apptio Cloudability Business Endpoint API URL
api_url = 'https://api.cloudability.com/v3/business-mappings'  # Replace with the actual API endpoint URL

# API Key for authentication (replace with your actual API key)
api_key = 'your_api_key_here'

# Headers for the request
headers = {
    'Authorization': f'Bearer {api_key}',
    'Content-Type': 'application/json'
}

# Example VAST or business mapping data (dynamic structure)
vast_data = {
    "total": "as",
    "Applications": [
        {
            "vsad": "T7II",
            "appid": "2588",
            "owner": "as@mska.com",
            "group": "IT"
        },
        {
            "vsad": "T6U",
            "appid": "8788",
            "owner": "aasas@mska.com",
            "group": "NonIT"
        },
        {
            "vsad": "YUjU",
            "appid": "3553288",
            "owner": "aasas@mska.com",
            "group": "NonIT"
        }
    ]
}

# Sending the POST request to Cloudability API
response = requests.post(api_url, headers=headers, data=json.dumps(vast_data))

# Checking the response
if response.status_code == 200:
    print("Data posted successfully!")
    print("Response:", response.json())
else:
    print(f"Failed to post data. Status code: {response.status_code}")
    print("Error response:", response.text)

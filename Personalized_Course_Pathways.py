import requests

# Replace with your actual API key
API_KEY = "qdh8u6s1HT9q4yl-3gsBiju4vP4CLuqwFKANtafigWqq"

# Step 1: Get IAM Token
token_response = requests.post(
    'https://iam.cloud.ibm.com/identity/token',
    data={
        "apikey": API_KEY,
        "grant_type": 'urn:ibm:params:oauth:grant-type:apikey'
    },
    headers={"Content-Type": "application/x-www-form-urlencoded"}
)

mltoken = token_response.json()["access_token"]

# Step 2: Prepare headers
headers = {
    'Content-Type': 'application/json',
    'Authorization': f'Bearer {mltoken}'
}

# Step 3: Prepare the prompt (user message)
payload_scoring = {
    "messages": [
        {
            "role": "user",
            "content": "What is the difference between supervised and unsupervised learning?"
        }
    ]
}

# Step 4: Send the request to the public deployment endpoint
url = "https://us-south.ml.cloud.ibm.com/ml/v4/deployments/55e76ad4-0b0b-43af-8d27-30f4ac35137d/ai_service?version=2021-05-01"

response = requests.post(url, headers=headers, json=payload_scoring)

# Step 5: Print the model's reply
try:
    response_json = response.json()
    print("Scoring response:")
    print(response_json["choices"][0]["message"]["content"])
except Exception as e:
    print("Error or unexpected format:")
    print(response.text)

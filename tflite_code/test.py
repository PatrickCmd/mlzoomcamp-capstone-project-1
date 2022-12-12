import os

import requests
from dotenv import load_dotenv

load_dotenv()  # take environment variables from .env.

url = "http://localhost:8080/2015-03-31/functions/function/invocations"

# example aws endpoint "https://m2eoxb7xelbkdxacxjhhrypic40aslby.lambda-url.us-east-1.on.aws/"
aws_lambda_endpoint = os.getenv("AWS_LAMBDA_ENDPOINT")
if aws_lambda_endpoint:
    url = aws_lambda_endpoint

# image_url = "https://thumbs.dreamstime.com/b/glass-clean-drinking-water-44066082.jpg"
image_url = "https://img.freepik.com/free-psd/close-up-ceramic-plate-mockup_53876-98747.jpg?w=2000"
data = {"url": image_url}

result = requests.post(url, json=data).json()
print(result)

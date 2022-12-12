import requests

url = "http://localhost:9696/predict"
image_url = "https://img.freepik.com/free-psd/close-up-ceramic-plate-mockup_53876-98747.jpg?w=2000"

data = {"url": image_url}

result = requests.post(url, json=data).json()
print(result)

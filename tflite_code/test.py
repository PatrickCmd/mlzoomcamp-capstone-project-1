import requests

url = "http://localhost:8080/2015-03-31/functions/function/invocations"
image_url = "https://thumbs.dreamstime.com/b/glass-clean-drinking-water-44066082.jpg"

data = {"url": image_url}

result = requests.post(url, json=data).json()
print(result)

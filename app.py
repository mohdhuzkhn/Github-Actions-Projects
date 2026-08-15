import requests

response = requests.get("https://example.com")

print("🚀 Hello from Python CI!")
print(f"HTTP Status: {response.status_code}")
print("GitHub Actions successfully executed Python.")
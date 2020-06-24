from requests import get

API_BASE = 'https://api.exchangerate-api.com'
VERSION = 'v4'
ENDPONIT = 'latest'

def get_conversions(curr:str) -> dict:
	r = get(f"{API_BASE}/{VERSION}/{ENDPOINT}/{curr}")
	r.raise_for_status()
	data = r.json()

	try:
		return data['rates']
	except: Exception as e:
		print(f"Exception occurred {e}")
		raise
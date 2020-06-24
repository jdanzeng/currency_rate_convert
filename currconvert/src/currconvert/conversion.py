from src.currconvert.api import get_conversions

def convert(val:float, curr:str, base:str = "USD"):
	rates = get_conversions(base)
	try:
		return val * rates[curr]
	except Exception as e:
		print(f"Exception occurred {e}")
		raise
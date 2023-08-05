import requests
apikey = "64DDF6A7-4465-4D7F-8BD7-A761CCC07931"

url= f"http://rest.coniapi.io/v1/exchangerate/BTC/EUR?apikey={apikey}"
response = requests.get(url)
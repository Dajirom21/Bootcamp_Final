import requests

apikey = "64DDF6A7-4465-4D7F-8BD7-A761CCC07931"
criptos =["BTC", "ETH", "USDT", "BNB", "USDC", "XRP", "DOGE", "ADA", "SOL", "TRX"]
monedas =["EUR", "USD", "JPY", "AUD", "RUB", "SEK", "NOK", "ISK", "DKK", "CZK", "COP", "CAD", "NZD", "CHF", "GBP", "ARS", "CLP", "MXN", "PEN"]

cripto =input("¿Que criptomoneda quieres saber?:")
moneda =input("¿A que moneda cambias?:")

url = f"https://rest.coinapi.io/v1/exchangerate/{cripto}/{moneda}?apikey={apikey}"

try:
    response = requests.get(url)
    data = response.json()
    if response.status_code == 200:
        print(f"EL {cripto} vale: {data['rate']:.2f} {moneda} cada una")
    else:
        print(response.status_code,"-", data["error"])
except requests.exceptions.RequestException:
    print("Se ha producido un error:\n", url)
    
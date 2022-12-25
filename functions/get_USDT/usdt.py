import requests

async def get_usdt():
  base = 'https://api.binance.com'
  path = '/api/v3/ticker/24hr'

  url = base + path
  params = {'symbol': 'USDTRUB'}
  r = await requests.get(url, params)

  if r.status_code == 200:
    data = r.json()
    price = round(float(data['lastPrice']), 2)
    percent = round(float(data['priceChangePercent']), 3)
    print(price, percent)
    return {
      'price': price,
      'percent': percent
    }
  else: 
    print('error connect')
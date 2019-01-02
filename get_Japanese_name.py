import requests
import json
import time
apikey = "c6cebfad880aa0a2fa834875a30620f15c1d90ec9b74271ca209dfa4f2b7faf3"
api = "https://api-tokyochallenge.odpt.org/api/v4/odpt:Station?&acl:consumerKey={key}"
url = api.format(key=apikey)
r = requests.get(url)
try:
	data = json.loads(r.text)

except json.decoder.JSONDecodeError:
	data = r.text


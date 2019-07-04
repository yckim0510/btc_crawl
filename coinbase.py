from coinbase.wallet.client import Client

############## using coinbase package #####################
client = Client(<api_key>, <api_secret>, api_version='YYYY-MM-DD')
currency_code = 'USD'  # can also use EUR, CAD, etc.
# Make the request
price = client.get_spot_price(currency=currency_code)
print 'Current bitcoin price in %s: %s' % (currency_code, price.amount)
############## using coinbase package #####################


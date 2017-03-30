import osa

###
URL1 = 'http://www.webservicex.net/ConvertTemperature.asmx?WSDL'

client1 = osa.client.Client(URL1)

response1 = client1.service.ConvertTemp(Temperature=12.5, FromUnit='degreeCelsius', ToUnit='degreeFahrenheit')

###
URL2 = 'http://www.webservicex.net/ConvertSpeed.asmx?WSDL'

client2 = osa.client.Client(URL2)

response2 = client2.service.ConvertSpeed(speed=121.25, FromUnit='milesPerhour', ToUnit='kilometersPerhour')

# print(response2)

###

URL3 = 'http://fx.currencysystem.com/webservices/CurrencyServer4.asmx?WSDL'

client3 = osa.client.Client(URL3)

response3 = client3.service.Currencies()

# print(response3.split(';'))

###

URL4 = 'http://fx.currencysystem.com/webservices/CurrencyServer4.asmx?WSDL'

client4 = osa.client.Client(URL4)

"""
fromCurrency" type="s:string"/>
<s:element minOccurs="0" maxOccurs="1" name="toCurrency" type="s:string"/>
<s:element minOccurs="1" maxOccurs="1" name="amount" type="s:double"/>
<s:element minOccurs="1" maxOccurs="1" name="rounding" type="s:boolean"/>
"""

response4 = client4.service.ConvertToNum(toCurrency='USD', fromCurrency='RUB', amount=100.00, rounding=True)

print(response4)
print(100.00 / float(response4))

###

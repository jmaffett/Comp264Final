from twython import Twython
import requests

url = "https://quotes15.p.rapidapi.com/quotes/random/"

headers = {
    'x-rapidapi-key': "12f723e552msh03388fd6e21de72p18ed2ejsn4a833f3fced7",
    'x-rapidapi-host': "quotes15.p.rapidapi.com"
    }

response = requests.request("GET", url, headers=headers)

file = response.text.split(":")
quote = file[3]
tweet = quote[:-6]


Key = "LWFU6WbGgvXKwfV7BUs4ERule"
Secret = "slGhcZipm6CGbR1AYf1MGjl2dFuKGcp5G29SHXzb8983sbVmbx"
Token = "1048976365570019328-vrEMwvYSIHY74fQeviAYuxGhgIszN5"
TokenSecret = "C72N056oHLwmzuGIj9SWIPxLWJG8MTNNrwb8t0P1QlSai"
Tweet = Twython(Key, Secret, Token, TokenSecret)

Tweet.update_status(status=tweet)
print(tweet)

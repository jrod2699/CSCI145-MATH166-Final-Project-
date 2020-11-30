import json

# Enter your keys/secrets as strings in the following fields
credentials = {}
credentials['CONSUMER_KEY'] = "Pchw4LSJoAUhjvN4af8rVMCmx"
credentials['CONSUMER_SECRET'] = "z68CbP7YkoAXeZASnTXw1KKxxbX5NSg6FGUmo7f88abI5RvSr6"
credentials['ACCESS_TOKEN'] = "1332899507822944261-EvB5OiHmslJVz4bltMUXGPpKumSrPw"
credentials['ACCESS_SECRET'] = "bix0rPeeB9wXWyipgeNbh19OXtgHddl8e1dJIJMjO35GB"

# Save the credentials object to file
with open("twitter_credentials.json", "w") as file:
    json.dump(credentials, file)

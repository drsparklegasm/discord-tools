import requests

"""
This script sends Discord a delete request to remove one's self from PM channels. 
For each channel you want to leave, if you load the conversation you will have an
address of https://discord.com/channels/@me/123456789012345678,  
where {123456789012345678} is the channel ID. 
"""

# You will need to gather your auth token from an active browser session, and the channel IDs of any 
# PM channels you wish to leave.

# Insert your auth token here:
authToken = ''

# If you want to notify folks, change this to false
silent = 'true' 

# Edit channels here:
channels = [
    '123456789012345678',
    '876543210987654321'
]

# Leave these alone unless you want to customize your user agent or something.
headers = {
    'Host': 'discord.com',
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:123.0) Gecko/20100101 Firefox/123.0',
    'Accept': '*/*',
    'Accept-Language': 'en-US,en;q=0.5',
    'Accept-Encoding': 'gzip, deflate, br',
    'Authorization': authToken,
    'X-Super-Properties': 'eyJvcyI6IkxpbnV4IiwiYnJvd3NlciI6IkZpcmVmb3giLCJkZXZpY2UiOiIiLCJzeXN0ZW1fbG9jYWxlIjoiZW4tVVMiLCJicm93c2VyX3VzZXJfYWdlbnQiOiJNb3ppbGxhLzUuMCAoWDExOyBMaW51eCB4ODZfNjQ7IHJ2OjEyMy4wKSBHZWNrby8yMDEwMDEwMSBGaXJlZm94LzEyMy4wIiwiYnJvd3Nlcl92ZXJzaW9uIjoiMTIzLjAiLCJvc192ZXJzaW9uIjoiIiwicmVmZXJyZXIiOiJodHRwczovL2R1Y2tkdWNrZ28uY29tLyIsInJlZmVycmluZ19kb21haW4iOiJkdWNrZHVja2dvLmNvbSIsInNlYXJjaF9lbmdpbmUiOiJkdWNrZHVja2dvIiwicmVmZXJyZXJfY3VycmVudCI6IiIsInJlZmVycmluZ19kb21haW5fY3VycmVudCI6IiIsInJlbGVhc2VfY2hhbm5lbCI6InN0YWJsZSIsImNsaWVudF9idWlsZF9udW1iZXIiOjI3MTIxNiwiY2xpZW50X2V2ZW50X3NvdXJjZSI6bnVsbH0=',
    'X-Discord-Locale': 'en-US',
    'X-Discord-Timezone': 'America/Los_Angeles',
    'X-Debug-Options': 'bugReporterEnabled',
    'Origin': 'https://discord.com',
    'DNT': '1',
    'Connection': 'keep-alive',
    'Referer': 'https://discord.com/channels/@me',
    'Cookie':'__dcfduid=734623c02dae11eebd57a114118a48e7; __sdcfduid=734623c12dae11eebd57a114118a48e712419d7cac427e87fda459aacf449bc027cfa4e60d3dacfd37f37cf16b7b490f; cf_clearance=QcyhwvhLlvK93gPj8d9BupL0c0pffhY4E9sqxVf9VH8-1709342981-1.0.1.1-IUrnBr8ol1nvrHPRfBZ5QbXT3U1J_d0Usyr5WG6DNYtYSS5Wdm_HGdBWjkFBQSIQrK7DHMJZ0TuiQ5Don.tmdw; __cfruid=53bbc4809480da318e11e74d44da8988a4ab696d-1709342979; _cfuvid=4Vs73oHB3OmNMdpiEX9aWka6zxdJnydioVLQVAsSqRE-1709342979677-0.0.1.1-604800000; locale=en-US; OptanonConsent=isIABGlobal=false&datestamp=Fri+Mar+01+2024+17%3A29%3A41+GMT-0800+(Pacific+Standard+Time)&version=6.33.0&hosts=&groups=C0001%3A1%2CC0002%3A1%2CC0003%3A1',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-GPC': '1',
    'TE': 'trailers'
}
params = {
    'silent': silent  
}


# Send the requests:
for i, channel in enumerate(channels):
    # Send the request and collect the response
    url = 'https://discord.com/api/v9/channels/'+ channel
    response = requests.delete(url, headers=headers, params=params)

    if response.status_code == 200:
        print(f"DELETE request was successful. Channel {channel} has been left.")
    else:
        print(f"Failed to send DELETE request. Status code: {response.status_code}, Response: {response.text}")

print('All channel delete requests have been sent. Exiting...')
import requests

url = "https://oauth2.googleapis.com/token"

payload='client_id=320233672341-dfueb086tq4or815f0rrdhm6pvm5p0bm.apps.googleusercontent.com&client_secret=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&grant_type=refresh_token&refresh_token=1%2F%2F0gsAVgWxgBjClCgYIARAAGBASNwF-L9Irp-26rHBi_go1P89VZHtO5Cp4ECo16xF0QnvX8K1u7pu_xbCzs8gBRgU7y7NMSmf-47Y'
headers = {
  'Content-Type': 'application/x-www-form-urlencoded'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
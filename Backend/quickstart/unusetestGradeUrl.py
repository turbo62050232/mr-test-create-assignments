import requests

url = "https://classroom.googleapis.com/v1/courses/578789685769/courseWork/610422162098/studentSubmissions/Cg4I1pqKqZgBELKF_P_hEQ"

payload = ""
headers = {
  'Authorization': 'Bearer ya29.a0Ael9sCNJByQPn1fACBEJ9UHVypoetcEl5fjGp529hFvohYfTxOUrIpj9isHp3UBFZFCTELLNloM6fkp1YEaakv8im7HAc4VrROAGIV6bWiZEgMY2iJlK38Vg2X_OD3t_Ln1Mc0dwSeMJoex0tKU9aYGgBMcfaCgYKAXgSARMSFQF4udJhAkHzYpVFVBfNTA-k5JSWjA0163'
}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)

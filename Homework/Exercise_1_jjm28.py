import requests
import json

url = "https://student-info-api.netlify.app/.netlify/functions/submit_student_info?UCID=12345678&section=101"

data = {
        "UCID": "jjm28",
        "first_name": "Jordan",
        "last_name": "Mosley",
        "github_username": "jjm28",
        "discord_username": "soul_maka",
        "favorite_cartoon": "Regular Show",
        "favorite_language": "Java",
        "movie_or_game_or_book": "League of Legends",
        "section": "103"
    }

response = requests.post(url, json = data)

if response.status_code == 201:
    print("POST request successful w/ status 201! The response JSON follows:")
    print(response.json())
elif response.status_code == 200:
    print("POST request successful w/ status 200! The response JSON follows:") 
    print(response.json())
else:
    print("Error! POST request failed w/status {response.status_code}")
    print(response.text)
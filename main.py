import requests
import os
import pickle

if os.getenv('API_KEY') is None:
  raise ValueError("No API key set for Textbelt. Please set the API_KEY environment variable.")

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
}

new_content = requests.get("https://uwbadgers.com/services/schedule_txt.ashx?schedule=694", headers=headers).text
old_content = pickle.load(open('old_content.pkl', 'rb'))

if new_content == old_content:
    print("No change detected.")

else:
  print("Change detected, sending texts.")
  numbers = ['9205174889', '4143799373']
  for number in numbers:
    resp = requests.post('https://textbelt.com/text', {
      'phone': number,
      'message': 'It changed, send the email. https://uwbadgers.com/services/schedule_txt.ashx?schedule=694',
      'key': os.getenv('API_KEY')
    })
    resp = requests.post('https://textbelt.com/text', {
      'phone': number,
      'message': new_content,
      'key': os.getenv('API_KEY')
    })

import requests
import os
import pickle
import time


def main():
    if os.getenv('API_KEY') is None:
      raise ValueError("No API key set for Textbelt. Please set the API_KEY environment variable.")

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
    }

    new_content_response = requests.get("https://uwbadgers.com/services/schedule_txt.ashx?schedule=694", headers=headers)

    if new_content_response.status_code != 200:
        raise ValueError(f"Failed to fetch content, status code: {new_content_response.status_code}")

    new_content = new_content_response.text
    old_content = pickle.load(open('old_content.pkl', 'rb'))

    if new_content == old_content:
        print("No change detected.")

    else:
      print("Change detected, sending texts.")
      numbers = ['9205174889', '4143799373']
      for number in numbers:
        print(f"Sending url to: {number}")
        resp = requests.post('https://textbelt.com/text', {
          'phone': number,
          'message': new_content,
          'key': os.getenv('API_KEY')
        })
        print(resp.json())
        time.sleep(1)
        resp = requests.post('https://textbelt.com/text', {
          'phone': number,
          'message': 'It changed, send the email.\n\n\t1. October 3rd\n\t2. September 26th\n\t3. October 17th\n\nEmail: nachtigall@wisc dot edu',
          'key': os.getenv('API_KEY')
        })
        print(resp.json())

if __name__ == "__main__":
    for x in range(15):
        print(f"Check iteration {x+1}/15")
        main()
        time.sleep(60)  # Sleep for 10 minutes

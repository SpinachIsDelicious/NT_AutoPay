import requests
import json
import time
import math

PAY_PER_HUNDRED_RACES = 1000000 # 1 Million because all the races have to be in the same session

TEAM = "IBM" # IBM ON TOP
TEAM_URL_ = f"https://www.nitrotype.com/api/v2/teams/{TEAM}"

PAY_PWD = "" # Do not share your Nitrotype Password with anyone.
AUTHORIZATION = "" # Do not share your Authorization with anyone.

def SCRAPE_JSON(TEAM_URL):
     response = requests.get(TEAM_URL)
     response_data = json.loads(response.text)
     return response_data

def PAY_USER(USER_ID, AMOUNT):
     TEMP_PAY = f"https://www.nitrotype.com/api/v2/players/{USER_ID}/send-cash"
     
     payload = {
          "amount":AMOUNT,
          "password":PAY_PWD
     }
     
     headers = {
          "authorization":AUTHORIZATION
     }
     
     requests.post(TEMP_PAY, data=payload, headers=headers) # Sent the money!
     
while True:
     time.sleep(600) # Sleep 10 minutes!
     
     SCRAPED_JSON = SCRAPE_JSON(TEAM_URL_)
     for NO_LIFE in SCRAPED_JSON:
          if NO_LIFE["played"] > 100:
               NO_LIFE["played"] = int(math.ceil(NO_LIFE["played"] / 100.0)) * 100
               PAY_COUNTS = NO_LIFE / 100
               NO_LIFE_ID = NO_LIFE["userID"]
               PAY_USER(NO_LIFE_ID, PAY_PER_HUNDRED_RACES * PAY_COUNTS) # Give the user that hard earned cash

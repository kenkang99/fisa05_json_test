# update_weather.py
# pip install python-dotenv requests
import requests
import os
from datetime import datetime
from dotenv import load_dotenv

load_dotenv()

NOW = datetime.now()

URL = f"https://jsonplaceholder.typicode.com/todos/{NOW+1}"

JSON_PATH = "/tmp/test.json"

def get_weather():
    response = requests.get(URL)
    if response.status_code == 200:
        datas = response.json()
        for data in datas:
            print(data)
    else:
        return "호출 실패"

def update_json():
    
    print(get_weather())
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    json_content = f"""
    
    FISA 5기 화이팅

    업데이트 시간: {now} (UTC)"""


    with open(JSON_PATH, "w", encoding="utf-8") as file:
        file.write(json_content)

if __name__ == "__main__":
    update_json()



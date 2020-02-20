import requests
from datetime import datetime
import json

DATA_PATH = "../data/cardapio"

headers = {
    'Connection': 'keep-alive',
    'Cache-Control': 'max-age=0',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Mobile Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'pt-BR,pt;q=0.9,en-US;q=0.8,en;q=0.7',
}

def separate_meals(json_data):
  SEPARATOR_MEAL = 4
  SEPARATOR_WEEK = 12

  week_days = {
    12: "Domingo-1",
    24: "Segunda",
    36: "Terça"  ,
    48: "Quarta" ,
    60: "Quinta" ,
    72: "Sexta"  ,
    84: "Sábado" 
  }

  meals_of_day = {
    0:  "Café da Manhã",
    1:  "Almoço",
    2: "Jantar"
  }
  
  list_food = []
  dict_meal = {}
  dict_week = {}
  counter_meal = 0

  for food in json_data["refeicoes"]:
    food["pid"] = int(food["pid"])

    list_food.append(food["name"])

    if food["pid"] % SEPARATOR_MEAL == 0 and food["pid"] != 0:
      dict_meal[meals_of_day[counter_meal]] = list_food.copy()
      counter_meal += 1
      list_food.clear()
        
    if food["pid"] % SEPARATOR_WEEK == 0 and food["pid"] != 0:
      dict_week[week_days[food["pid"]]] = dict_meal.copy()
      counter_meal = 0
      dict_meal.clear()

    if food["pid"] == 84:
      return dict_week

try:
  response = requests.get('http://cardapioufv.com.br/cardapioufv/php/get_ru_fl.php', headers=headers, verify=False)
  # with open(DATA_PATH + datetime.now().strftime("%Y-%m-%d|%H:%M:%S") + ".json", "w") as f:
  #   json.dump(response.json(), f)
  #   
  with open(DATA_PATH + ".json", "w") as f:
    json.dump(separate_meals(response.json()), f, indent=2, ensure_ascii=False)

except requests.exceptions.ConnectionError as err:
  print("Ocurred a connection error")
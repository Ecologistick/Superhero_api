import requests

names = ['Captain_America','Hulk' ,'Thanos']
  
def hero_intellegence(names):
  heroes = {}
  for name in names:
    Hero_response = requests.get('https://superheroapi.com/api/2619421814940190/search/'+ name)
    Hero_data = Hero_response.json()
    Hero_id = Hero_data['results'][0]['id']
    Hero_response_id = requests.get('https://superheroapi.com/api/2619421814940190/'+ Hero_id +'/powerstats')
    Hero_powerstats = Hero_response_id.json()
    heroes.update({Hero_powerstats['name']:int(Hero_powerstats['intelligence'])})
  print(heroes)
  print (max(heroes, key=heroes.get))

hero_intellegence(names)

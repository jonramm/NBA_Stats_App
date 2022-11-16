
import datetime
import time
import requests
import pprint
import json
from plyer import notification
from nba_api.stats.endpoints import playercareerstats
from nba_api.live.nba.endpoints import scoreboard

# Nikola Jokić
career = playercareerstats.PlayerCareerStats(player_id='203999') 
career_data = career.get_json()

games = scoreboard.ScoreBoard()
games_data = json.loads(games.get_json())
# pprint.pprint(games_data["scoreboard"]["games"])

str_arr = []
for game in games_data["scoreboard"]["games"]:
    data = {
        "home": game["awayTeam"]["teamName"],
        "away": game["awayTeam"]["teamName"],
        "home_score": game["awayTeam"]["score"],
        "away_score": game["homeTeam"]["score"]
    }

    string = "-----------------------\n" + \
        "{} vs {}\n".format(data["home"], data["away"]) + \
        "{} - {}\n".format(data["home_score"], data["away_score"]) + \
        "-----------------------\n"
    str_arr.append(string)

for gm in str_arr:
    print(gm)
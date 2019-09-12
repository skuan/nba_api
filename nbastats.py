from nba_api.stats.endpoints import commonplayerinfo
from nba_api.stats.endpoints._base import Endpoint
from nba_api.stats.library.http import NBAStatsHTTP
from nba_api.stats.endpoints import playerdashboardbyteamperformance
from nba_api.stats.endpoints import teamdashboardbyteamperformance
from nba_api.stats.endpoints import playerdashboardbylastngames
from nba_api.stats.static import teams
from nba_api.stats.static import players
import pandas

# Basic Request
#player_info = commonplayerinfo.CommonPlayerInfo(player_id=2544)
#player_info = commonplayerinfo.player_headline_stats(player_id=2544)
#playerdashboard = playerdashboardbyteamperformance.PlayerDashboardByTeamPerformance(player_id=2544)
#print(playerdashboard.overall_player_dashboard.get_json())


player1_input = input('Enter player 1: ')
print(player1_input)

player1 = players.find_players_by_full_name(player1_input)[0]['id']

player_info = playerdashboardbylastngames.PlayerDashboardByLastNGames(player_id=player1, last_n_games=20)
player_headers = player_info.last20_player_dashboard.get_dict().get('headers')
player_data = player_info.last20_player_dashboard.get_dict().get('data')[0]

print(player_headers[5], player_data[5], 
	player_headers[2], player_data[2], 
	player_headers[26], player_data[26],
	player_headers[27], player_data[27])


# team1_input = input('Enter team 1: ')
# print(team1_input)

# team1 = teams.find_teams_by_full_name(team1_input)[0]['id']
# print(team1)
# teamdashboard = teamdashboardbyteamperformance.TeamDashboardByTeamPerformance(team_id=team1)

# print(teamdashboard.overall_team_dashboard.get_dict().get('data')[0][-1])

# print(teamdashboard.overall_team_dashboard.get_dict().get('headers')[9], ': ',
# 	teamdashboard.overall_team_dashboard.get_dict().get('data')[0][9])


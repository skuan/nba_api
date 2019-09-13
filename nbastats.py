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

#PER Calculation
factor = (2 / 3) -(0.5 * (lg_AST / lg_FG)) / (2 * (lg_FG / lg_FT)) 
VOP = lg_PTS / (lg_FGA -lg_ORB + lg_TOV + 0.44 * lg_FTA) 
DRB_perc = (lg_TRB -lg_ORB) / lg_TRB
lg_AST = 
lg_FG = 
lg_PTS =
lg_FGA =
lg_FT = 
lg_FTA = 
lg_TRB =
lg_ORB =
lg_TOV = 
#####stats####
MP = player_data[6]
ThrP = player_data[10] 
AST = player_data[19]
team_AST =  
team_FG = 
TOV = player_data[20]
FGA = player_data[8]
FG = player_data[7]+player_data[10] 
FTA = player_data[14]
FT = player_data[13]
TRB = player_data[18]
ORB = player_data[16]
STL = player_data[21]
BLK = player_data[22]
PF = player_data[24]


PER_calc_player = (1/MP) * [ThrP + (2/3) * AST + 
(2-factor * (team_AST/team_FG)) * FG + 
(FT * 0.5 * (1 + (1 -(team_AST/team_FG)) 
	+ (2/3) * (team_AST / team_FG))) -VOP * TOV -VOP * DRB_perc * 
(FGA -FG) -VOP * 0.44 * (0.44 + (0.56 * DRP_perc)) * (FTA -FT) + VOP * 
(1 -DRB_perc) * (TRB -ORB) + VOP * DRB_perc * ORB + VOP *STL + VOP * DRB_perc * 
BLK -PF * ((lg_FT / lg_PF) -0.44 * (lg_FTA / lg_PF) * VOP)]


# team1_input = input('Enter team 1: ')
# print(team1_input)

# team1 = teams.find_teams_by_full_name(team1_input)[0]['id']
# print(team1)
# teamdashboard = teamdashboardbyteamperformance.TeamDashboardByTeamPerformance(team_id=team1)

# print(teamdashboard.overall_team_dashboard.get_dict().get('data')[0][-1])

# print(teamdashboard.overall_team_dashboard.get_dict().get('headers')[9], ': ',
# 	teamdashboard.overall_team_dashboard.get_dict().get('data')[0][9])


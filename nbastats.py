from nba_api.stats.endpoints import commonplayerinfo
from nba_api.stats.endpoints._base import Endpoint
from nba_api.stats.library.http import NBAStatsHTTP
from nba_api.stats.endpoints import playerdashboardbyteamperformance
from nba_api.stats.endpoints import teamdashboardbyteamperformance
from nba_api.stats.endpoints import playerdashboardbylastngames
from nba_api.stats.endpoints import teamplayerdashboard
from nba_api.stats.static import teams
from nba_api.stats.static import players
import pandas


#Player Input
player1_input = input('Enter player 1: ')
print(player1_input)

player1 = players.find_players_by_full_name(player1_input)[0]['id']

player_info = playerdashboardbylastngames.PlayerDashboardByLastNGames(player_id=player1)

#player_headers = player_info.overall_player_dashboard.get_dict().get('headers')
#player_data = player_info.overall_player_dashboard.get_dict().get('data')[0]

##last 20 games##
player_headers = player_info.last20_player_dashboard.get_dict().get('headers')
player_data = player_info.last20_player_dashboard.get_dict().get('data')[0]

print(player_headers[5], player_data[5], 
	player_headers[2], player_data[2], 
	player_headers[26], player_data[26],
	player_headers[27], player_data[27])

#Team Input

team1_input = input('Enter team 1: ')
print(team1_input)
team1 = teams.find_teams_by_full_name(team1_input)[0]['id']
teamdashboard = teamdashboardbylastngames.TeamDashboardByLastNGames(team_id=team1)

#team_headers = teamdashboard.overall_team_dashboard.get_dict().get('headers')
#team_data = teamdashboard.overall_team_dashboard.get_dict().get('data')[0]

##last 20 games##
team_headers = teamdashboard.last20_team_dashboard.get_dict().get('headers')
team_data = teamdashboard.last20_team_dashboard.get_dict().get('data')[0]

print(team1, 'Season:', team_data[-1])
print(team_headers[2], team_data[2], team_headers[3], team_data[3],
      team_headers[4], team_data[4], team_headers[9], team_data[9])

#PER Data 

##League Avg Data (2018-19)
lg_AST = 24.6
lg_FG = 41.1
lg_PTS = 111.2
lg_FGA = 89.2
lg_FT = 17.7
lg_FTA = 23.1
lg_TRB = 45.2
lg_ORB = 10.3
lg_TOV = 14.1
lg_PF = 20.9
lg_pace = 100

factor = (2/3) - (0.5*(lg_AST/lg_FG)) / (2*(lg_FG/lg_FT)) 
VOP = lg_PTS / (lg_FGA-lg_ORB+lg_TOV+0.44*lg_FTA) 
DRB_perc = (lg_TRB -lg_ORB) / lg_TRB
 
print('league stats:', factor, VOP, DRB_perc)

##PER player stats
MP = player_data[6]
ThrP = player_data[10] 
AST = player_data[19]
TOV = player_data[20]
FGA = player_data[8]
FG = player_data[7] + player_data[10] 
FTA = player_data[14]
FT = player_data[13]
TRB = player_data[18]
ORB = player_data[16]
STL = player_data[21]
BLK = player_data[22]
PF = player_data[24]
print(MP)

##PER team stats
team_AST = team_data[19]
team_FG = team_data[7]+team_data[10]
team_pace = 103.2 #Lakers
print(team_AST, team_FG)

#PER Calculation                    
PER_calc_player = (1 / MP) * ( ThrP + (2/3) * AST
     + (2 - factor * (team_AST / team_FG)) * FG
     + (FT *0.5 * (1 + (1 - (team_AST / team_FG)) + (2/3) * (team_AST / team_FG)))
     - VOP * TOV - VOP * DRB_perc * (FGA - FG)
     - VOP * 0.44 * (0.44 + (0.56 * DRB_perc)) * (FTA - FT)
     + VOP * (1 - DRB_perc) * (TRB - ORB) + VOP * DRB_perc * ORB + VOP * STL + VOP * DRB_perc * BLK - PF * ((lg_FT / lg_PF) - 0.44 * (lg_FTA / lg_PF) * VOP) )

adj_PER_calc_player = PER_calc_player * (lg_pace /team_pace)
print(PER_calc_player, adj_PER_calc_player)

#Team Roster
roster1 = teamplayerdashboard.TeamPlayerDashboard(team_id=team1, last_n_games=20).get_dict()#.PlayersSeasonTotals(team_id=team1, last_n_games=20)
print(roster1)

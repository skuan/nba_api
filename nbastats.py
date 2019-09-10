from nba_api.stats.endpoints import commonplayerinfo
from nba_api.stats.endpoints._base import Endpoint
from nba_api.stats.library.http import NBAStatsHTTP
from nba_api.stats.endpoints import playerdashboardbyteamperformance
from nba_api.stats.endpoints import teamdashboardbyteamperformance
from nba_api.stats.static import teams
import pandas

# Basic Request
player_info = commonplayerinfo.CommonPlayerInfo(player_id=2544)
#player_info = commonplayerinfo.player_headline_stats(player_id=2544)

#print(player_info.player_headline_stats.get_json())

#playerdashboard = playerdashboardbyteamperformance.PlayerDashboardByTeamPerformance(player_id=2544)
#print(playerdashboard.overall_player_dashboard.get_json())

team1_input = input('Enter team 1: ')
print(team1_input)

team1 = teams.find_teams_by_full_name(team1_input)[0]['id']
print(team1)
teamdashboard = teamdashboardbyteamperformance.TeamDashboardByTeamPerformance(team_id=team1)

print(teamdashboard.overall_team_dashboard.get_dict().get('data')[0][-1])

print(teamdashboard.overall_team_dashboard.get_dict().get('headers')[9], ': ',
	teamdashboard.overall_team_dashboard.get_dict().get('data')[0][9])

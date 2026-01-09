from data_collection import *
from feature_engineering import *
from training_data import *
import pandas as pd
testing_data = []
matchups = [
    ('CAR', 'LAR'),
    ('CHI', 'GB'),
    ('JAX','BUF'),
    ('PHI','SF'),
    ('NE','LAC'),
    ('PIT','HOU')]

def create_testing_data(home_team, away_team):
    home_team_stats = get_teams_stats_including_week(team=home_team, week=18, data=games_df)
    away_team_stats = get_teams_stats_including_week(team=away_team, week=18, data=games_df)
    win_pct_diff = home_team_stats['win_pct'] - away_team_stats['win_pct']
    ppg_diff = home_team_stats['ppg'] - away_team_stats['ppg']
    papg_diff = home_team_stats['papg'] - away_team_stats['papg']
    point_diff_diff = home_team_stats['point_diff'] - away_team_stats['point_diff']
    game_features = {
            'win_pct_diff': win_pct_diff,
            'ppg_diff': ppg_diff,
            'papg_diff': papg_diff,
            'point_diff_diff': point_diff_diff,
            'home_field':1
        }
    return game_features

for matchup in matchups:
    game_features = create_testing_data(matchup[0], matchup[1])
    testing_data.append(game_features)

testing_df = pd.DataFrame(testing_data)



import pandas as pd
from data_collection import *
from feature_engineering import *
import sklearn

training_data = []
training_games = games_df[games_df['week'] >= 2]
for index, row in training_games.iterrows():
    home_team = row['home_team']
    away_team = row['away_team']
    week = row['week']
    home_score = row['home_score']
    away_score = row['away_score']
    home_team_stats = get_teams_stats_through_week(team=home_team, week=week, data=games_df)
    away_team_stats = get_teams_stats_through_week(team=away_team, week=week, data=games_df)
    home_win_pct = home_team_stats['win_pct']
    away_win_pct = away_team_stats['win_pct']
    home_ppg = home_team_stats['ppg']
    away_ppg = away_team_stats['ppg']
    home_papg = home_team_stats['papg']
    away_papg = away_team_stats['papg']
    home_point_diff = home_team_stats['point_diff']
    away_point_diff = away_team_stats['point_diff']
    win_pct_diff = home_win_pct - away_win_pct
    ppg_diff = home_ppg - away_ppg
    papg_diff = home_papg - away_papg
    point_diff_diff = home_point_diff - away_point_diff
    if home_score > away_score:
        home_won = 1
    else:
        home_won = 0
    game_features = {
        'win_pct_diff': win_pct_diff,
        'ppg_diff': ppg_diff,
        'papg_diff': papg_diff,
        'point_diff_diff': point_diff_diff,
        'home_field':1,
        'home_team_won': home_won
    }
    training_data.append(game_features)
    
training_df = pd.DataFrame(training_data)

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

# CAR_stats = get_teams_stats_including_week(team='CAR', week=18, data=games_df)
# LAR_stats = get_teams_stats_including_week(team='LAR', week=18, data=games_df)
# win_pct_diff = CAR_stats['win_pct'] - LAR_stats['win_pct']
# ppg_diff = CAR_stats['ppg'] - LAR_stats['ppg']
# papg_diff = CAR_stats['papg'] - LAR_stats['papg']
# point_diff_diff = CAR_stats['point_diff'] - LAR_stats['point_diff']
# game_features = {
#         'win_pct_diff': win_pct_diff,
#         'ppg_diff': ppg_diff,
#         'papg_diff': papg_diff,
#         'point_diff_diff': point_diff_diff,
#         'home_field':1,
#     }
# testing_data.append(game_features)
# CHI_stats = get_teams_stats_including_week(team='CHI', week=18, data=games_df)
# GB_stats = get_teams_stats_including_week(team='GB', week=18, data=games_df)
# win_pct_diff = CHI_stats['win_pct'] - GB_stats['win_pct']
# ppg_diff = CHI_stats['ppg'] - GB_stats['ppg']
# papg_diff = CHI_stats['papg'] - GB_stats['papg']
# point_diff_diff = CHI_stats['point_diff'] - GB_stats['point_diff']
# game_features = {
#         'win_pct_diff': win_pct_diff,
#         'ppg_diff': ppg_diff,
#         'papg_diff': papg_diff,
#         'point_diff_diff': point_diff_diff,
#         'home_field':1,
#     }
# testing_data.append(game_features)
# JAX_stats = get_teams_stats_including_week(team='JAX', week=18, data=games_df)
# BUF_stats = get_teams_stats_including_week(team='BUF', week=18, data=games_df)
# win_pct_diff = JAX_stats['win_pct'] - BUF_stats['win_pct']
# ppg_diff = JAX_stats['ppg'] - BUF_stats['ppg']
# papg_diff = JAX_stats['papg'] - BUF_stats['papg']
# point_diff_diff = JAX_stats['point_diff'] - BUF_stats['point_diff']
# game_features = {
#         'win_pct_diff': win_pct_diff,
#         'ppg_diff': ppg_diff,
#         'papg_diff': papg_diff,
#         'point_diff_diff': point_diff_diff,
#         'home_field':1,
#     }
# testing_data.append(game_features)
# PHI_stats = get_teams_stats_including_week(team='PHI', week=18, data=games_df)
# SF_stats = get_teams_stats_including_week(team='SF', week=18, data=games_df)
# win_pct_diff = PHI_stats['win_pct'] - SF_stats['win_pct']
# ppg_diff = PHI_stats['ppg'] - SF_stats['ppg']
# papg_diff = PHI_stats['papg'] - SF_stats['papg']
# point_diff_diff = PHI_stats['point_diff'] - SF_stats['point_diff']
# game_features = {
#         'win_pct_diff': win_pct_diff,
#         'ppg_diff': ppg_diff,
#         'papg_diff': papg_diff,
#         'point_diff_diff': point_diff_diff,
#         'home_field':1,
#     }
# testing_data.append(game_features)
# NE_stats = get_teams_stats_including_week(team='NE', week=18, data=games_df)
# LAC_stats = get_teams_stats_including_week(team='LAC', week=18, data=games_df)
# win_pct_diff = NE_stats['win_pct'] - LAC_stats['win_pct']
# ppg_diff = NE_stats['ppg'] - LAC_stats['ppg']
# papg_diff = NE_stats['papg'] - LAC_stats['papg']
# point_diff_diff = NE_stats['point_diff'] - LAC_stats['point_diff']
# game_features = {
#         'win_pct_diff': win_pct_diff,
#         'ppg_diff': ppg_diff,
#         'papg_diff': papg_diff,
#         'point_diff_diff': point_diff_diff,
#         'home_field':1,
#     }
# testing_data.append(game_features)
# PIT_stats = get_teams_stats_including_week(team='PIT', week=18, data=games_df)
# HOU_stats = get_teams_stats_including_week(team='HOU', week=18, data=games_df)
# win_pct_diff = PIT_stats['win_pct'] - HOU_stats['win_pct']
# ppg_diff = PIT_stats['ppg'] - HOU_stats['ppg']
# papg_diff = PIT_stats['papg'] - HOU_stats['papg']
# point_diff_diff = PIT_stats['point_diff'] - HOU_stats['point_diff']
# game_features = {
#         'win_pct_diff': win_pct_diff,
#         'ppg_diff': ppg_diff,
#         'papg_diff': papg_diff,
#         'point_diff_diff': point_diff_diff,
#         'home_field':1,
#     }
# testing_data.append(game_features)
# print(testing_data)


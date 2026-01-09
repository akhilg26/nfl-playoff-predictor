import pandas as pd

def get_teams_stats_through_week(team, week, data):
    games_before_week = data[data['week'] < week]
    team_games = games_before_week[((games_before_week['away_team'] == team) | (games_before_week['home_team'] == team))]
    # print(f"Team: {team}, Week: {week}")
    # print(f"Games found: {len(team_games)}")
    # print(team_games)
    wins = 0
    losses = 0
    
    total_points_scored = 0
    total_points_allowed = 0
    for index, row in team_games.iterrows():
        if row['away_team'] == team:
            total_points_scored += row['away_score']
            total_points_allowed += row['home_score']
            if row['away_score'] > row['home_score']:
                wins += 1
            else:
                losses +=1
        else:
            total_points_scored += row['home_score']
            total_points_allowed += row['away_score']
            if row['home_score'] > row['away_score']:
                wins += 1
            else:
                losses +=1
    games_played = wins + losses
    
    if games_played == 0:
        return{
            'wins': 0,
            "losses": 0,
            "games_played": 0,
            "total_points_scored": 0,
            "total_points_allowed": 0,
            "win_pct": 0,
            "ppg": 0,
            "papg": 0,
            "point_diff": 0
        }
    return {
        'wins': wins,
        "losses": losses,
        "games_played": games_played,
        "total_points_scored": total_points_scored,
        "total_points_allowed": total_points_allowed,
        "win_pct": (wins / games_played),
        "ppg": (total_points_scored / games_played),
        "papg": (total_points_allowed / games_played),
        "point_diff": ((total_points_scored / games_played) - (total_points_allowed / games_played))
    }


def get_teams_stats_including_week(team, week, data):
    games_before_week = data[data['week'] <= week]
    team_games = games_before_week[((games_before_week['away_team'] == team) | (games_before_week['home_team'] == team))]
    # print(f"Team: {team}, Week: {week}")
    # print(f"Games found: {len(team_games)}")
    # print(team_games)
    wins = 0
    losses = 0
    
    total_points_scored = 0
    total_points_allowed = 0
    for index, row in team_games.iterrows():
        if row['away_team'] == team:
            total_points_scored += row['away_score']
            total_points_allowed += row['home_score']
            if row['away_score'] > row['home_score']:
                wins += 1
            else:
                losses +=1
        else:
            total_points_scored += row['home_score']
            total_points_allowed += row['away_score']
            if row['home_score'] > row['away_score']:
                wins += 1
            else:
                losses +=1
    games_played = wins + losses
    
    if games_played == 0:
        return{
            'wins': 0,
            "losses": 0,
            "games_played": 0,
            "total_points_scored": 0,
            "total_points_allowed": 0,
            "win_pct": 0,
            "ppg": 0,
            "papg": 0,
            "point_diff": 0
        }
    return {
        'wins': wins,
        "losses": losses,
        "games_played": games_played,
        "total_points_scored": total_points_scored,
        "total_points_allowed": total_points_allowed,
        "win_pct": (wins / games_played),
        "ppg": (total_points_scored / games_played),
        "papg": (total_points_allowed / games_played),
        "point_diff": ((total_points_scored / games_played) - (total_points_allowed / games_played))
    }
# return team's stats (wins, losses, points_for, points_against)
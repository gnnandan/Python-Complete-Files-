team=['india','usa','germany','austraila','bangladesh']

for home_team in team:
    for away_team in team:
        if home_team != away_team:
            print(home_team + " VS "+away_team)
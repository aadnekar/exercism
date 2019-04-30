def tally(tournament_results):
    result = ['Team'.ljust(31) + '| MP |  W |  D |  L |  P']
    if not tournament_results:
        return result[0]
    
    # right_team outputs the result of the away_team
    right_team = {'win': 'loss', 'loss': 'win', 'draw': 'draw'}
    point_scale = {'win': 3, 'draw': 1, 'loss': 0}
    team_stats = {}

    tournament_results = tournament_results.split('\n')
    for line in tournament_results:
        game = line.split(';')
        home_team, home_result = game[0], game[2]
        away_team, away_result = game[1], right_team[game[2]]
        if home_team not in team_stats:
            team_stats[home_team] = {'MP':0,'win':0,'draw':0,'loss':0,'P':0}
        if away_team not in team_stats:
            team_stats[away_team] = {'MP':0,'win':0,'draw':0,'loss':0,'P':0}
        
        team_stats[home_team]['MP'] += 1
        team_stats[away_team]['MP'] += 1

        team_stats[home_team][home_result] += 1
        team_stats[away_team][away_result] += 1

        team_stats[home_team]['P'] += point_scale[home_result]
        team_stats[away_team]['P'] += point_scale[away_result]

    for team, stats in sorted(team_stats.items(), key = lambda i: (-i[1]['P'], i[0])):
        played = str(stats['MP'])
        win    = str(stats['win'])
        draw   = str(stats['draw'])
        loss   = str(stats['loss'])
        points = str(stats['P'])

        result.append(
            team.ljust(31) + '|'
            + played.rjust(3) + ' |'
            + win.rjust(3) + ' |'
            + draw.rjust(3) + ' |'
            + loss.rjust(3) + ' |'
            + points.rjust(3)
        )
        
    return '\n'.join(result)
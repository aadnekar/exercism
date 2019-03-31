def tally(tournament_results):
    rv = 'Team                           | MP |  W |  D |  L |  P'

    if tournament_results == '':
        return rv
    
    POS = 0             # Position for the current team.
    tmt = []            # list of teams in the tournment.
    team_location = {}  # location of the team in the list above.

    tournament_results = tournament_results.split('\n')
    for line in tournament_results:
        game = line.split(';')
        for tmt_team in range(2):
            if not any(_['team'] == game[tmt_team] for _ in tmt):
                tmt.append({'team': game[tmt_team], 'MP': 0, 'W': 0, 'D': 0, 'L': 0, 'P': 0})
                team_location[game[tmt_team]] = POS
                POS += 1
        if game[2]== 'draw':
            pos_one, pos_two = team_location[game[0]], team_location[game[1]]
            ''' Increment matches played, draw and points. '''
            tmt[pos_one]['MP'] += 1
            tmt[pos_one]['D'] += 1
            tmt[pos_one]['P'] += 1
            ''' Increment matches played, draw and points. '''
            tmt[pos_two]['MP'] += 1
            tmt[pos_two]['D'] += 1
            tmt[pos_two]['P'] += 1
        else:
            if game[2] == 'win':
                pos_winner, pos_loser = team_location[game[0]], team_location[game[1]]
            elif game[2] == 'loss':
                pos_winner, pos_loser = team_location[game[1]], team_location[game[0]]

            ''' Winner increments Matches played and Wins: and gains three points. '''
            tmt[pos_winner]['MP'] += 1
            tmt[pos_winner]['W'] += 1
            tmt[pos_winner]['P'] += 3
            ''' Losers increment Matches played and losses: gains zero points. '''
            tmt[pos_loser]['MP'] += 1
            tmt[pos_loser]['L'] += 1
    for team in sorted(tmt, key = lambda i: (-i['P'], i['team']), reverse=False):
        spaces = ' '*(31 - len(team['team']))
        rv += '\n{}{}|  {} |  {} |  {} |  {} |  {}'.format(
                                                team['team'],
                                                spaces,
                                                str(team['MP']),
                                                str(team['W']),
                                                str(team['D']),
                                                team['L'],
                                                str(team['P'])
                                            )
    return rv
def tally(tournament_results):
    rv = 'Team                           | MP |  W |  D |  L |  P'
    
    POS = 0             # Position for the current team.
    tmt = []            # list of teams in the tournment.
    team_location = {}  # location of the team in the list above.
    for line in tournament_results:
        game = line.split(';')
        for tmt_team in range(2):
            if not any(_['team'] == game[tmt_team] for _ in tmt):
                tmt.append({'team': game[tmt_team], 'MP': 0, 'W': 0, 'D': 0, 'L': 0, 'P': 0})
                team_location[tmt_team] = POS
                POS += 1
        if game[3] == 'draw':
            pos_one, pos_two = team_location[game[1]], team_location[game[2]]
            ''' Increment matches played, draw and points. '''
            tmt[pos_one]['MP'] += 1
            tmt[pos_one]['D'] += 1
            tmt[pos_one]['P'] += 1
            ''' Increment matches played, draw and points. '''
            tmt[pos_two]['MP'] += 1
            tmt[pos_two]['D'] += 1
            tmt[pos_two]['P'] += 1
        else:
            if game[3] == 'win':
                pos_winner, pos_loser = team_location[game[1]], team_location[game[2]]
            elif game[3] == 'loss':
                pos_winner, pos_loser = team_location[game[2]], team_location[game[1]]

            ''' Winner increments Matches played and Wins: and gains three points. '''
            tmt[pos_winner]['MP'] += 1
            tmt[pos_winner]['W'] += 1
            tmt[pos_winner]['P'] += 3
            ''' Losers increment Matches played and losses: gains zero points. '''
            tmt[pos_loser]['MP'] += 1
            tmt[pos_loser]['L'] += 1
    print(sorted(tmt, key = lambda i: i['P'], reverse=True))
        # print(team)
        # rv += '{}{}{} | {} | {} | {} | {}'.format(tm['Team'], ' '*(30 - len(tm['team']), tm['MP'], tm['W'], tm['D'], tm['L'], tm['P']))
    
    return rv

print(tally('Allegoric Alaskans;Blithering Badgers;win'))
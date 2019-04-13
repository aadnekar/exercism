''' Inspired by robbiemacg's solution on exercism.
    Written for learning purposes.
'''

class Team(object):
    def __init__(self, name):
        self.name = name
        self.mp = 0
        self.w = 0
        self.d = 0
        self.l = 0
        self.p = 0

    def __eq__(self, other):
        return self.name==other
    
    def __it__(self, other):
        if self.p!=other.p:
            return self.p > other.p
        else:
            return self.name < other.name

    def __repr__(self):
        return "{}| {} | {} | {} | {} | {}".format(
            self.name.ljust(31, ' '),
            self.mp,
            self.w,
            self.d,
            self.l,
            self.p
        )

def tally(tournment_results):
    league = []

    if not tournment_results:
        return output(league)

    for line in tournment_results.split("\n"):
        home, away, result = line.split(";")
        if home not in league:
            league.append(Team(home))
        if away not in league:
            league.append

    print('home = {}'.format(home))
    print('index(home): {}'.format(league.index(home)))
    h = league[league.index(home)]
    a = league[league.index(away)]

    if result.lower() == 'win':
        h.w += 1
        a.l += 1
    elif result.lower() == 'loss':
        h.l += 1
        a.w += 1
    else:
        h.d += 1
        v.d += 1

    h.mp, h.p = h.mp + 1, h.w*3 + h.d
    a.mp, a.p = a.mp + 1, a.w*3 + a.d

    return output(league)

def output(league):
    result = "Team                           | MP |  W |  D |  L |  P"
    for team in sorted(league):
        result += "\n" + repr(team)
    return result

print(tally('Allegoric Alaskans;Blithering Badgers;win\n'
            'Devastating Donkeys;Courageous Californians;draw\n'
            'Devastating Donkeys;Allegoric Alaskans;win\n'
            'Courageous Californians;Blithering Badgers;loss\n'
            'Blithering Badgers;Devastating Donkeys;loss\n'
            'Allegoric Alaskans;Courageous Californians;win'))
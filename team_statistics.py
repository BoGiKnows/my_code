import re

def nba_cup(result_sheet, to_find):
    data = result_sheet.split(',')
    result = {}
    for game in data:
        try:
            team1_result, team2_result = list(map(int, re.findall(r'\b\d+\b', game)))
        except Exception:
            return f"Error(float number):{game}"
        team1, team2 = list(map(lambda x: x.strip(), re.split(r'\b\d+\b', game)[:-1]))
        # "Team Name:W=nb of wins;D=nb of draws;L=nb of losses;Scored=nb;Conceded=nb;Points=nb"
        if team1 not in result:
            result[team1] = [0, 0, 0, 0, 0, 0]
        if team2 not in result:
            result[team2] = [0, 0, 0, 0, 0, 0]
        if team1_result > team2_result:
            result[team1][0] += 1
            result[team1][-1] += 3
            result[team1][3] += team1_result
            result[team1][4] += team2_result
            result[team2][2] += 1
            result[team2][3] += team2_result
            result[team2][4] += team1_result
        elif team1_result < team2_result:
            result[team2][0] += 1
            result[team2][-1] += 3
            result[team2][3] += team2_result
            result[team2][4] += team1_result
            result[team1][2] += 1
            result[team1][3] += team1_result
            result[team1][4] += team2_result
        else:
            result[team1][1] += 1
            result[team2][1] += 1
            result[team1][3] += team1_result
            result[team1][4] += team2_result
            result[team2][3] += team2_result
            result[team2][4] += team1_result
            result[team1][-1] += 1
            result[team2][-1] += 1
    if not to_find:
        return ''
    if to_find not in result:
        return f"{to_find}:This team didn't play!"
    return f'{to_find}:W={result[to_find][0]};D={result[to_find][1]};L={result[to_find][2]};' \
           f'Scored={result[to_find][3]};Conceded={result[to_find][4]};Points={result[to_find][5]}'


r = "Los Angeles Clippers 103.21 Dallas Mavericks 103,New York Knicks 101 Atlanta Hawks 112,Indiana Pacers 103 Memphis Grizzlies 112"

print(nba_cup(r, 'Los Angeles Clippers'))
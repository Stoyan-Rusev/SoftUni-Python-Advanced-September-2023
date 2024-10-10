def team_lineup(*args):
    country_dict = {}
    for name, country in args:
        if country not in country_dict.keys():
            country_dict[country] = []
        country_dict[country].append(name)
    sorted_info = sorted(country_dict.items(), key=lambda kvp: (-len(kvp[1]), kvp[0]))
    result = []
    for current_country, players_names in sorted_info:
        result.append(f'{current_country}:')
        for current_name in players_names:
            result.append(f'  -{current_name}')
    return '\n'.join(result)


print(team_lineup(
   ("Harry Kane", "England"),
   ("Manuel Neuer", "Germany"),
   ("Raheem Sterling", "England"),
   ("Toni Kroos", "Germany"),
   ("Cristiano Ronaldo", "Portugal"),
   ("Thomas Muller", "Germany")))
print()
print(team_lineup(
   ("Lionel Messi", "Argentina"),
   ("Neymar", "Brazil"),
   ("Cristiano Ronaldo", "Portugal"),
   ("Harry Kane", "England"),
   ("Kylian Mbappe", "France"),
   ("Raheem Sterling", "England")))
print()
print(team_lineup(
   ("Harry Kane", "England"),
   ("Manuel Neuer", "Germany"),
   ("Raheem Sterling", "England"),
   ("Toni Kroos", "Germany"),
   ("Cristiano Ronaldo", "Portugal"),
   ("Thomas Muller", "Germany"),
   ("Bruno Fernandes", "Portugal"),
   ("Bernardo Silva", "Portugal"),
   ("Harry Maguire", "England")))

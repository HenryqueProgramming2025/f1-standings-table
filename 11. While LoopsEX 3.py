def big_line():
    print('-=' * 37)

big_line()
print('Formula 1 Standings - Position, Names, Teams, Points, Wins, Poles'.center(74))

drivers = [
    (1, 'Lando Norris', 'McLaren', 357, 6, 5),
    (2, 'Oscar Piastri', 'McLaren', 356, 7, 5),
    (3, 'Max Verstappen', 'Red Bull', 321, 5, 7),
    (4, 'George Russel', 'Mercedes', 258, 2, 2),
    (5, 'Charles Leclerc', 'Ferrari', 210, 0, 1),
    (6, 'Lewis Hamilton', 'Ferrari', 146, 0, 0),
    (7, 'Kimi Antonelli', 'Mercedes', 97, 0, 0,),
    (8, 'Alexander Albon', 'Williams', 73, 0, 0),
    (9, 'Nico Hulkenberg', 'Kick Sauber', 41, 0, 0),
    (10, 'Isack Hadjar', 'Racing Bulls', 39, 0, 0),
    (11, 'Carlos Sainz', 'Williams', 38, 0, 0),
    (12, 'Fernando Alonso', 'Aston Martin', 37, 0, 0),
    (13, 'Oliver Bearman', 'Haas', 32, 0, 0),
    (14, 'Lance Stroll', 'Aston Martin', 32, 0, 0),
    (15, 'Liam Lawson', 'Racing Bulls', 30, 0, 0),
    (16, 'Esteban Ocon', 'Haas', 30, 0, 0),
    (17, 'Yuki Tsunoda', 'Red Bull', 28, 0, 0),
    (18, 'Pierre Gasly', 'Alpine', 20, 0, 0),
    (19, 'Gabriel Bortoleto', 'Kick Sauber', 19, 0, 0),
    (20, 'Franco Colapinto', 'Alpine', 0, 0, 0),
    (21, 'Jack Doohan', 'Alpine', 0, 0, 0)
]

big_line()
print(f"| {'POSITION':^5} | {'DRIVER NAMES':^17} | {'TEAMS':^13} | {'POINTS':^5} | {'WINS':^6} | {'POLES':^6} |")

for pos, name, team, pts, wins, poles in drivers:
    print(f'| {pos:^8} | {name:^17} | {team:^13} | {pts:^6} | {wins:^6} | {poles:^6} |')
big_line()
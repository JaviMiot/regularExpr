#!/user/bin/python

import re
import time


class SoccerGameData():
    def __init__(self, **kwargs):
        self.year_of_champion: str = kwargs.get('year_of_champion')
        self.team_1: str = kwargs.get('team_1')
        self.team_2: str = kwargs.get('team_2')
        self.score_team_1: int = kwargs.get('score_team_1')
        self.score_team_2: int = kwargs.get('score_team_2')


def generate_game_soccer(dataOfGame: re) -> SoccerGameData:
    game_data_generated = {
        'year_of_champion':  dataOfGame.group(1),
        'team_1':  dataOfGame.group(2),
        'team_2':  dataOfGame.group(3),
        'score_team_1':  int(dataOfGame.group(4)),
        'score_team_2':  int(dataOfGame.group(5))
    }

    return SoccerGameData(**game_data_generated)


def results_of_game(game: SoccerGameData) -> str:
    teams = f'{game.team_1} - {game.team_2}'
    scores = f'({game.score_team_1}-{game.score_team_2})'
    return f'{game.year_of_champion} ::  {teams} => {scores}'


def find_games_by_greater_than(score_to_find: int, file_name: str) -> None:

    regex = re.compile(
        r'^(\d{4})\-\d{2}\-\d{2},(.+),(.+),(\d+),(\d+),(.+),.*$')

    file_to_read = open(file_name, 'r')

    for line in file_to_read:
        response_regex = re.match(regex, line)
        if response_regex:
            game = generate_game_soccer(response_regex)
            score_total = game.score_team_1 + game.score_team_2
            if score_total > score_to_find:
                print(f'{results_of_game(game)}, Total de gles: {score_total}')

    file_to_read.close()


initTime = time.time()
find_games_by_greater_than(10, './results.csv')
print(f'total time: {time.time() - initTime}')

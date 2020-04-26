from django.core.management.base import BaseCommand
from football_app.statistica.models import Statistica


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument('-g', '--goals', type=int, help='Number of goals for creation')
        parser.add_argument('-a', '--assists', type=int, help='Number of assists for creation')
        parser.add_argument('-r', '--red_cards', type=int, help='Number of red cards for creation')
        parser.add_argument('-y', '--yellow_cards', type=int, help='Number of yellow cards for creation')
        parser.add_argument('-p', '--played_games', type=int, help='Number of played games for creation')
        parser.add_argument('-n', '--null', type=bool, help='Create Statistics with null statistics')

    def handle(self, *args, **kwargs):
        goals = kwargs.get('goals')
        assists = kwargs.get('assists')
        red_cards = kwargs.get('red_cards')
        yellow_cards = kwargs.get('yellow_cards')
        played_games = kwargs.get('played_games')
        null = kwargs.get('null')
        if null:
            s = Statistica.objects.create()
            print(s)
        else:
            s = Statistica.objects.create(
                goals=goals,
                assists=assists,
                red_card=red_cards,
                yellow_card=yellow_cards,
                played_games=played_games
            )
            print(s)

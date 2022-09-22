import character
from character import *


class UnknownAction(Exception):
    def __init__(self, message):
        self.message = message

    def __str__(self):
        return self.message


def choose_action(player: Character, enemy: Character):
    action = input('Выберите действие(ударить; лечиться; уклониться; перезарядить(если доступно)):\n>').lower()
    match action:
        case 'уклониться':
            player.dodge(enemy)
        case 'ударить':
            player.attack(enemy)
        case 'лечиться':
            player.take_heal(player.damage)
        case 'перезарядить':
            if type(player) != Gunner:
                raise UnknownAction('Действие недоступно для данного персонажа.')
            player.reload()
        case _:
            raise UnknownAction('Неизвестное действие')


if __name__ == '__main__':
    p1 = Gunner(name='Vasya')
    p2 = Character(name='Petya')

    while p1.hp > 0 and p2.hp > 0:
        try:
            choose_action(p1, p2)
        except UnknownAction:
            print(f'Игрок {p1.name} выбрал несуществующее действие и пропускает ход!')

        try:
            choose_action(p2, p1)
        except UnknownAction:
            print(f'Игрок {p2.name} выбрал несуществующее действие и пропускает ход!')

        print(p1.stats())
        print(p2.stats())
from Lesson_1.character import Character


class UnknownAction(Exception):
    def __init__(self, message):
        self.message = message

    def __str__(self):
        return self.message


def choose_action(player: Character, enemy: Character):
    action = input('Выберите действие: ')

    if action == 'ударить':
        player.attack(enemy)
    elif action == 'лечиться':
        player.take_heal(player.damage)
    else:
        raise UnknownAction('Неизвестное действие')


if __name__ == '__main__':
    p1 = Character(name='Vasya')
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
# Импортируем модуль `random`, который используется для работы с генерацией случайных чисел
import random
# Затем мы определяем два класса: `Soldier` (Солдат) и `Hero` (Герой)
# У обоих классов есть конструктор `__init__`, который инициализирует объекты с указанными свойствами
# Такими как идентификационный номер (`id`), команда (`team`) и уровень героя (`level`)
# У класса `Soldier` также есть метод `follow_hero`, который выводит текст о том, что солдат следует за героем
class Soldier:
    def __init__(self, id, team):
        self.id = id
        self.team = team
    def follow_hero(self, hero):
        print(f"Солдат {self.id} следует за героем {hero.id}")
class Hero:
    def __init__(self, id, team, level=1):
        self.id = id
        self.team = team
        self.level = level
    def increase_level(self):
        self.level += 1
# Создаются два объекта класса `Hero` для каждой из двух команд
team1_hero = Hero(id=1, team='Team1')
team2_hero = Hero(id=2, team='Team2')
# Создаются списки `soldiers_team1` и `soldiers_team2` для солдат каждой команды
soldiers_team1 = []
soldiers_team2 = []
# С помощью цикла `for` генерируется 10 солдат случайным образом для каждой команды и добавляются в соответствующий список
for i in range(10):
    team = random.choice(['Team1', 'Team2'])
    if team == 'Team1':
        soldiers_team1.append(Soldier(id=i, team=team))
    else:
        soldiers_team2.append(Soldier(id=i, team=team))
# Выводится длина списков солдат для обеих команд
print(f"Длина списка солдат команды Team1: {len(soldiers_team1)}")
print(f"Длина списка солдат команды Team2: {len(soldiers_team2)}")
# Проверяется, у какой команды больше солдат, и в зависимости от этого, увеличивается уровень соответствующего героя
if len(soldiers_team1) > len(soldiers_team2):
    team1_hero.increase_level()
    print(f"Уровень героя команды Team1 увеличен до {team1_hero.level}")
else:
    team2_hero.increase_level()
    print(f"Уровень героя команды Team2 увеличен до {team2_hero.level}")
# С помощью `random.choice` выбирается солдат из списка солдат первой команды, и этот солдат следует за героем первой команды
soldier_follow = random.choice(soldiers_team1)
soldier_follow.follow_hero(team1_hero)
#  На экран выводится идентификационный номер солдата и героя, за которым он следует
print(f"Идентификационные номера солдата и героя: {soldier_follow.id}, {team1_hero.id}")
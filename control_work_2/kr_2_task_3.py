"""
Соревнования по футболу между командами проводятся в два этапа.
Для проведения первого этапа участники разбиваются на две группы
по 12 команд. Для проведения второго этапа выбирается 6 лучших команд
каждой группы по результатам первого этапа. Составить список команд участников
второго этапа.
"""
import random

class Team:
    def __init__(self, name):
        self.name = name
        self.points = 0

    def update_points(self, points):
        self.points += points

    def __str__(self):
        return f"Команда >> {self.name}, Очки >> {self.points}"


class Group:
    def __init__(self, group_name):
        self.group_name = group_name
        self.teams = []

    def add_team(self, team):
        if len(self.teams) < 12:
            self.teams.append(team)

    def get_top_teams(self, count=6):
        # Сортируем команды по очкам и выбираем лучших
        top_teams = sorted(self.teams, key=lambda team: team.points, reverse=True)[:count]
        return top_teams


class Tournament:
    def __init__(self):
        self.group_a = Group("Группа A")
        self.group_b = Group("Группа B")

    def add_team_to_group(self, group_name, team):
        if group_name == "A":
            self.group_a.add_team(team)
        elif group_name == "B":
            self.group_b.add_team(team)

    def get_final_teams(self):
        top_teams_a = self.group_a.get_top_teams()
        top_teams_b = self.group_b.get_top_teams()
        return top_teams_a + top_teams_b


# Пример использования
tournament = Tournament()

# Добавляем команды в группы
for i in range(1, 13):
    team_a = Team(f"Команда A{i}")
    team_b = Team(f"Команда B{i}")

    # Обновляем очки для примера
    team_a.update_points(random.randint(0, 30))
    team_b.update_points(random.randint(0, 30))

    tournament.add_team_to_group("A", team_a)
    tournament.add_team_to_group("B", team_b)

# Получаем команды, прошедшие в финал
final_teams = tournament.get_final_teams()

print("Команды второго этапа >>")
for team in final_teams:
    print(team)
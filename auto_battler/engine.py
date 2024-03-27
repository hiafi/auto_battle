import random
from collections import defaultdict

class CombatEngine():
    def __init__(self, player_team, enemies):
        self.turn = 1
        self.player_team = player_team
        self.enemies = enemies

    @property
    def teams(self):
        return [self.player_team, self.enemies]

    def check_for_team_wipe(self, team):
        all_dead = True
        for fighter in team:
            if fighter.hp > 0:
                all_dead = False
        return all_dead

    def get_teams(self, combatant):
        friendlies = self.player_team
        enemies = self.enemies
        if combatant in self.enemies:
            enemies = self.player_team
            friendlies = self.enemies
        return friendlies, enemies

    def take_turn(self, combatant):
        if combatant.hp <= 0:
            return
        friendlies, enemies = self.get_teams(combatant)
        results = combatant.take_turn(friendlies, enemies)
        for r in results:
            print(r)

    def do_round(self):
        combatants = self.player_team + self.enemies
        random.shuffle(combatants)
        for combatant in combatants:
            self.take_turn(combatant)

    def assign_numbers(self, enemies):
        enemy_list = defaultdict(int)
        for enemy in enemies:
            enemy_list[enemy._name] += 1
        enemy_list = {e: i for (e, i) in enemy_list.items() if i > 1}
        for enemy in enemies:
            if enemy._name in enemy_list:
                enemy.set_number(enemy_list[enemy._name])
                enemy_list[enemy._name] -= 1

    def run(self):
        end_combat = False
        self.assign_numbers(self.enemies)
        while not end_combat:
            print("="*20)
            print("Turn {}".format(self.turn))
            print("=" * 20)
            self.do_round()
            self.turn += 1
            print("")
            for team in self.teams:
                if self.check_for_team_wipe(team):
                    end_combat = True
                    break

        if self.check_for_team_wipe(self.player_team):
            print("The heroes lost...")
        else:
            print("The heroes are victorious!")
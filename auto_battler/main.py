import random


class Character(object):

    def __init__(self, character_name, character_hp, extra_damage):
        self.name = character_name
        self.hp = character_hp
        self.extra_damage = extra_damage

    def take_damage(self, amount):
        self.hp -= amount
        print("{} HP: {}, {} damage taken".format(self.name, self.hp, amount))

    def get_damage(self):
        return random.randint(1, 6) + self.extra_damage


def check_for_team_wipe(team):
    all_dead = True
    for fighter in team:
        if fighter.hp > 0:
            all_dead = False
    return all_dead


def take_turn(heroes, villians):
    combatants = heroes + villians
    random.shuffle(combatants)
    for combatant in combatants:
        if combatant.hp <= 0:
            continue
        target_list = villians
        if combatant in villians:
            target_list = heroes
        damage = combatant.get_damage()
        target = random.choice(target_list)
        target.take_damage(damage)


def main():
    hero = Character("Hero", 20, 0)
    evil_dude = Character("Evil Dude", 15, 1)

    heroes = [hero]
    villians = [evil_dude]
    turn = 1
    while not check_for_team_wipe(heroes) and not check_for_team_wipe(villians):
        print("="*20)
        print("Turn {}".format(turn))
        print("=" * 20)
        take_turn(heroes, villians)
        turn += 1
        print("")

    if check_for_team_wipe(heroes):
        print("The heroes lost...")
    else:
        print("The heroes are victorious!")


if __name__ == "__main__":
    main()

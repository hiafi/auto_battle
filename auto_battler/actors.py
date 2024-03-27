import random

class Result(object):
    pass

class DamageResult(Result):
    def __init__(self, actor_name, targets, damage):
        self.actor_name = actor_name
        self.targets = targets
        self.damage = damage

    def __str__(self):
        for target in self.targets:
            return "{} attacks {} for {} damage".format(self.actor_name, target, self.damage)

class DeathResult(Result):
    def __init__(self, actor_name):
        self.actor_name = actor_name

    def __str__(self):
        return "{} has died".format(self.actor_name)

class Actor(object):

    def __init__(self, character_name, health, extra_damage):
        self._name = character_name
        self.hp = health
        self.extra_damage = extra_damage

    @property
    def name(self):
        return self._name

    def take_damage(self, amount):
        self.hp -= amount
        return amount
        print("{} HP: {}, {} damage taken".format(self.name, self.hp, amount))

    def get_damage(self):
        return random.randint(1, 6) + self.extra_damage

    def take_turn(self, allies, enemies):
        raise NotImplementedError("Subclasses must implement take_turn")

    def random_target(self, enemies):
        if not enemies:
            return None
        damage = self.get_damage()
        target = random.choice([e for e in enemies if e.hp > 0])
        return target

    def deal_damage(self, enemies, targeting):
        results = []
        damage = self.get_damage()
        target = targeting(enemies)
        final_damage = target.take_damage(damage)
        results.append(DamageResult(self.name, [target.name], final_damage))
        if target.hp <= 0:
            results.append(DeathResult(target.name))
        return results


class PlayerCharacter(Actor):

    def take_turn(self, allies, enemies):
        return self.deal_damage(enemies, self.random_target)


class Enemy(Actor):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.number = 0

    def set_number(self, number):
        self.number = number

    def take_turn(self, allies, enemies):
        return self.deal_damage(enemies, self.random_target)

    @property
    def name(self):
        if self.number > 0:
            return self._name + " " + str(self.number)
        return self._name

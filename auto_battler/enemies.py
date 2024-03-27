from actors import Enemy

class Goblin(Enemy):

    def __init__(self):
        super().__init__("Goblin", health=10, extra_damage=0)


class Zombie(Enemy):

    def __init__(self):
        super().__init__("Zombie", health=30, extra_damage=0)


class Ghoul(Enemy):

    def __init__(self):
        super().__init__("Zombie", health=60, extra_damage=4)


class Orc(Enemy):

    def __init__(self):
        super().__init__("Orc", health=20, extra_damage=5)


class Kobold(Enemy):

    def __init__(self):
        super().__init__("Kobold", health=10, extra_damage=0)


class Dragon(Enemy):

    def __init__(self):
        super().__init__("Orc", health=150, extra_damage=10)
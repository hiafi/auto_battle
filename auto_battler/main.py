import random

from engine import CombatEngine
from actors import PlayerCharacter
from stages import stages

def main():
    hero = PlayerCharacter("Hero", 20, 0)

    combat_engine = CombatEngine([hero], stages[1])
    combat_engine.run()


if __name__ == "__main__":
    main()

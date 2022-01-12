from enum import Enum, Flag

class Weapon(Enum):
    DAGGER = {'cost': 8, 'damage': 4, 'armor': 0}
    SHORTSWORD = {'cost': 10, 'damage': 5, 'armor': 0}
    WARHAMMER = {'cost': 25, 'damage': 6, 'armor': 0}
    LONGSWORD = {'cost': 40, 'damage': 7, 'armor': 0}
    GREATAXE = {'cost': 74, 'damage': 8, 'armor': 0}

class Armor(Enum):
    LEATHER = {'cost': 13, 'damage': 0, 'armor': 1}
    CHAINMAIL = {'cost': 31, 'damage': 0, 'armor': 2}
    SPLINTMAIL = {'cost': 53, 'damage': 0, 'armor': 3}
    BANDEDMAIL = {'cost': 75, 'damage': 0, 'armor': 4}
    PLATEMAIL = {'cost': 102, 'damage': 0, 'armor': 5}
    NONE = {'cost': 0, 'damage': 0, 'armor': 0}

class Ring(Flag):
    DAMAGE_1 = {'cost': 25, 'damage': 1, 'armor': 0}
    DAMAGE_2 = {'cost': 50, 'damage': 2, 'armor': 0}
    DAMAGE_3 = {'cost': 100, 'damage': 3, 'armor': 0}
    DEFENSE_1 = {'cost': 20, 'damage': 0, 'armor': 1}
    DEFENSE_2 = {'cost': 40, 'damage': 0, 'armor': 2}
    DEFENSE_3 = {'cost': 80, 'damage': 0, 'armor': 3}
    NONE = {'cost': 0, 'damage': 0, 'armor': 0}
# Not needed but could be useful in the future
# damage_ring = Ring.DAMAGE_1 | Ring.DAMAGE_2 | Ring.DAMAGE_3
# defense_ring = Ring.DEFENSE_1 | Ring.DEFENSE_2 | Ring.DEFENSE_3

ring_pairs = [(Ring.NONE, Ring.NONE)]
for a in range(0, len(list(Ring))):
    for b in range(a + 1, len(list(Ring))):
        ring_pairs.append((list(Ring)[a], list(Ring)[b]))

games_won = []
games_lost = []
for weapon in list(Weapon):
    for armor in list(Armor):
        for ring_1, ring_2 in ring_pairs:
            player_damage = sum([weapon.value['damage' ], armor.value['damage' ], ring_1.value['damage' ], ring_2.value['damage' ]])
            player_armor = sum([weapon.value['armor' ], armor.value['armor' ], ring_1.value['armor' ], ring_2.value['armor' ]])
            player = {'hit_points': 100, 'damage': player_damage, 'armor': player_armor}

            puzzle_input = {'hit_points': 100, 'damage': 8, 'armor': 2}

            while(puzzle_input['hit_points'] > 0 or player['hit_points'] > 0):
                hit_points = (player_damage - puzzle_input['armor'])
                hit_points = 1 if hit_points <= 0 else hit_points
                puzzle_input['hit_points'] -= hit_points

                if puzzle_input['hit_points'] <= 0 or player['hit_points'] <= 0:
                    break

                hit_points = (puzzle_input['damage'] - player_armor)
                hit_points = 1 if hit_points <= 0 else hit_points
                player['hit_points'] -= hit_points
            if player['hit_points'] > puzzle_input['hit_points']:
                games_won.append(((weapon, armor, ring_1, ring_2), sum([weapon.value['cost' ], armor.value['cost' ], ring_1.value['cost' ], ring_2.value['cost' ]])))
            else:
                games_lost.append(((weapon, armor, ring_1, ring_2), sum([weapon.value['cost' ], armor.value['cost' ], ring_1.value['cost' ], ring_2.value['cost' ]])))

games_won.sort(key=lambda gw: gw[1])
print(f'The cheapest game to win will require {games_won[0][1]} gold')

games_lost.sort(key=lambda gw: gw[1])
print(f'The most expensive game to lose will require {games_lost[-1][1]} gold')
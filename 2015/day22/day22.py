player_initial = {
    "health": 50,
    "mana": 500,
    "mana_total": 0,
    "armor": 0,
    "poison": 0,
    "recharge": 0,
    "shield": 0
}

monster_initial = {
    "health": 71,
    "damage": 10
}

spells_cost = {
    "magic_missile": 53,
    "drain": 73,
    "shield": 113,
    "poison": 173,
    "recharge": 229
}


def applyEffects(player, monster):
    for e in ['poison', 'recharge', 'shield']:
        player[e] -= 1
        if player[e] >= 0:
            if e == "poison":
                monster["health"] -= 3
            elif e == "recharge":
                player["mana"] += 101
            elif e == "shield":
                if player[e] == 0:
                    player["armor"] -= 7


def playerTurn(player, monster, mod=0):
    res = 1000000
    player["health"] -= mod
    if player["health"] <= 0:
        return res

    applyEffects(player, monster)

    for s in [ "magic_missile", "drain", "shield", "poison", "recharge" ]:
        if s not in player or player[s] <= 0:
            new_player = player.copy()
            new_player["mana"] -= spells_cost[s]
            if new_player["mana"] < 0:
                pass
            else:
                new_player["mana_total"] += spells_cost[s]
                new_monster = monster.copy()
                if s == "poison":
                    new_player[s] = 6
                elif s == "magic_missile":
                    new_monster["health"] -= 4
                elif s == "recharge":
                    new_player[s] = 5
                elif s == "shield":
                    new_player["armor"] += 7
                    new_player[s] = 6
                elif s == "drain":
                    new_player["health"] += 2
                    new_monster["health"] -= 2

                res = min(monsterTurn(new_player, new_monster, mod), res)

    return res


def monsterTurn(player, monster, mod):
    applyEffects(player, monster)

    if monster["health"] <= 0:
        return player["mana_total"]

    damage = max(1, monster["damage"] - player["armor"])
    player["health"] -= damage

    if player["health"] <= 0:
        return 1000000

    return playerTurn(player, monster, mod)



def main():
    res = playerTurn(player_initial, monster_initial)
    print(res)

    res = playerTurn(player_initial, monster_initial, 1)
    print(res)


if __name__ == "__main__":
    main()

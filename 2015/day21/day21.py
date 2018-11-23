player = {
    "health": 100,
    "damage": 0,
    "armor": 0
}

monster = {
    "health": 104,
    "damage": 8,
    "armor": 1
}

weapons = {
    "dagger": (8, 4, 0),
    "shortsword": (10, 5, 0),
    "warhammer": (25, 6, 0),
    "longsword": (40, 7, 0),
    "greataxe": (74, 8, 0)
}

armors = {
    "leather": (13, 0, 1),
    "chainmail": (31, 0, 2),
    "splintmail": (53, 0, 3),
    "bandedmail": (75, 0, 4),
    "platemail": (102, 0, 5)
}

rings = {
    "damage1": (25, 1, 0),
    "damage2": (50, 2, 0),
    "damage3": (100, 3, 0),
    "defense1": (20, 0, 1),
    "defense2": (40, 0, 2),
    "defense3": (80, 0, 3)
}


def get_weapon():
    res = []
    for key in weapons:
        res.append(key)
    return res


def get_armor():
    res = []
    res.append("")
    for key in armors:
        res.append(key)
    return res


def get_rings():
    res = []
    res.append([])
    for key in rings:
        res.append([key])
    rlist = list(rings)
    for a in range(0, len(rlist)-1):
        for b in range(a+1, len(rlist)):
            res.append([rlist[a], rlist[b]])
    return res


def battle():
    monster_health = monster["health"]
    monster_damage = monster["damage"]
    monster_armor = monster["armor"]
    player_health = player["health"]
    player_damage = player["damage"]
    player_armor = player["armor"]

    while True:
        monster_health -= max(1, player_damage - monster_armor)
        if monster_health <= 0:
            return True
        player_health -= max(1, monster_damage - player_armor)
        if player_health <= 0:
            return False


def main():
    wlist = get_weapon()
    alist = get_armor()
    rlist = get_rings()

    win = 1000
    lose = 0
    for w in wlist:
        for a in alist:
            for rl in rlist:
                gold = 0
                player["damage"] = 0
                player["armor"] = 0
                for r in rl:
                    if r in rings:
                        gold += rings[r][0]
                        player["damage"] += rings[r][1]
                        player["armor"] += rings[r][2]
                if a in armors:
                    gold += armors[a][0]
                    player["damage"] += armors[a][1]
                    player["armor"] += armors[a][2]
                if w in weapons:
                    gold += weapons[w][0]
                    player["damage"] += weapons[w][1]
                    player["armor"] += weapons[w][2]
                if battle() == True:
                    win = min(win, gold)
                else:
                    lose = max(lose, gold)

    print(win, lose)


if __name__ == "__main__":
    main()

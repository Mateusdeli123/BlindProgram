
def addToInventory(inventory_Player, additens):
    dic = {}

    for k,v in inventory_Player.items():
        for i in additens:
            if k == i:
                v = v + 1
                dic[k] = v
            else:
                dic.setdefault(i, 1)
    return dic


def displayInventory(player_equips):
    c = 0
    for k,v in player_equips.items():
        c = c + v
        print v, k
    print 'Total number of items:',c

player_equips = {'torch': 6,'gold coin':3}
dragonLoot = ['gold coin','torch','sword','axe','shield','demon armor']
player_equips = addToInventory(player_equips,dragonLoot)
displayInventory(player_equips)




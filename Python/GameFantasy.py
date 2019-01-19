# Game Fantasia -- Automatizando Tarefas Python

player_equips = {'rope': 1,
                 'torch': 6,
                 'gold coin': 42,
                 'dagger' : 1,
                 'arrow': 12}

player_equips2 = {'rope': 3,
                 'torch': 1,
                 'gold coin': 56,
                 'dagger' : 3,
                 'arrow': 2}

def displayInventory(player_equips):
    print 'Inventory:'
    item = 0
    for k,v in player_equips.items():
        print 'Equip:',k
        print 'Qtd:',v
        item += v
    print 'Quantidade total de Itens: ', item

print displayInventory(player_equips)
print '\n'
print displayInventory(player_equips2)


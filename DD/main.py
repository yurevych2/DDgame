'''
Main module of the game.
Consist game loop.
'''

import game

kitchen = game.Room('Кухня')
kitchen.set_description('Мокра і брудна кімната, яка дзижчить від мух.')

dining_hall = game.Room('Їдальня')
dining_hall.set_description('Велика кімната з багато прикрашеними золотими прикрасами на кожній стіні.')

ballroom = game.Room('Бальна зала')
ballroom.set_description('Величезна кімната з блискучою дерев’яною підлогою. Величезні свічники біля входу.')

kitchen.link_room(dining_hall, 'південь')
dining_hall.link_room(kitchen, 'північ')
dining_hall.link_room(ballroom, 'захід')
ballroom.link_room(dining_hall, 'схід')

dave = game.Enemy('Дейв', 'Смердючий зомбі.')
dave.set_conversation('Як життя? Я дуже голодний...')
dave.set_weakness('сир')
dining_hall.set_character(dave)

tabitha = game.Enemy('Тобіто', 'Величезний павук з незліченною кількістю очей і пухнастими ногами.')
tabitha.set_conversation('Ссссс... Мені так нудно...')
tabitha.set_weakness('книга')
ballroom.set_character(tabitha)

cheese = game.Item('сир')
cheese.set_description('Великий і смердючий шматок сиру.')
ballroom.set_item(cheese)

book = game.Item('книга')
book.set_description('Дійсно хороша книга під назвою "В`язання для чайників".')
dining_hall.set_item(book)

if __name__ == '__main__':
    current_room = kitchen
    backpack = []

    dead = False

    while dead == False:
        print('\n')
        current_room.get_details()
        inhabitant = current_room.get_character()

        if inhabitant:
            inhabitant.describe()

        item = current_room.get_item()
        if item:
            item.describe()

        command = input('(поговорити, вбити, взяти)\n> ')

        if command in ['південь', 'північ', 'захід', 'схід']:
            # Move in the given direction
            current_room = current_room.move(command)
        elif command == 'поговорити':
            # Talk to the inhabitant - check whether there is one!
            if inhabitant is not None:
                inhabitant.talk()
            else:
                print('Хей, ти нормальний? Там нікого нема!')
        elif command == 'вбити':
            if inhabitant:
                # Fight with the inhabitant, if there is one
                print('Чим будеш битися?')
                fight_with = input()

                # Do I have this item?
                if fight_with in backpack:
                    if inhabitant.fight(fight_with) == True:
                        # What happens if you win?
                        print('Ура, ти переміг!')
                        current_room.character = None
                        if inhabitant.get_defeated() == 2:
                            print('О, невже ти переміг їх усіх? Неочікувано... Вітаю!')
                            dead = True
                    else:
                        # What happens if you lose
                        print('О, милий, ти програв бій...')
                        print('Ось і кінець гри :=(')
                        dead = True
                else:
                    print('У вас немає ' + fight_with)
            else:
                print('Досить бити повітря! Там нікого нема!')
        elif command == 'взяти':
            if item is not None:
                print('Ти підібрав ' + item.get_name() + ' у свій рюкзак.')
                backpack.append(item.get_name())
                current_room.set_item(None)
            else:
                print('Тут нічого брати!')
        else:
            print('Я незнаю як ' + command)


'''
Main module of the game.
Consist game loop.
'''

import game

hall_1 = game.Room('Каса магазинy')
hall_1.set_description('Черги немає.')

hall_2 = game.Room('Перший зал')
hall_2.set_description('Велика кімната з побутовими речами.')

hall_3 = game.Room('Другий зал')
hall_3.set_description('Величезна кімната з продуктами.')

hall_1.link_shop(hall_2, 'південь')
hall_2.link_shop(hall_1, 'північ')
hall_2.link_shop(hall_3, 'захід')
hall_3.link_shop(hall_2, 'схід')

dave = game.Seller('Касир Дейв', 'Високий брюнет.')
dave.set_conversation('Як життя? Я готовий пробити ваші товари.')
dave.set_weakness('100 грн.')
hall_1.set_character(dave)

student = game.Human('Покупець', 'Судячі з мішків під очима - студент.\
\nТримає в руках останню буханку хлібу.', 'Енергос')
student.set_conversation('Хочу вмерти.')
student.set_weakness('Енергос')
hall_2.set_character(student)

energy = game.Item('Енергос')
energy.set_description('Точно здоровий, 100% екологічний продукт.')
hall_3.set_item(energy)

if __name__ == '__main__':
    current_room = hall_1
    backpack = ['100 грн.']

    print('Тобі треба купити хліб, інакше жінка не пустить додому.')

    done = False
    while not done:
        print('\n')
        current_room.get_details()
        inhabitant = current_room.get_character()

        if inhabitant:
            inhabitant.describe()

        item = current_room.get_item()
        if item:
            item.describe()

        command = input('(1 - поговорити, 2 - обміняти / купити, 3 - взяти)\n> ')

        if command in ['південь', 'північ', 'захід', 'схід']:
            # Move in the given direction
            current_room = current_room.move(command)
        elif command == '1':
            # Talk to the inhabitant - check whether there is one!
            if inhabitant:
                inhabitant.talk()
            else:
                print('Хей, ти нормальний? Там нікого нема!')
        elif command == '2':
            if inhabitant:
                # Fight with the inhabitant, if there is one
                print('Що будеш міняти?')
                fight_with = input()

                # Do I have this item?
                if fight_with in backpack:
                    idx = backpack.index(fight_with)
                    backpack[idx] = inhabitant.exchange(fight_with, backpack)
                    if backpack[-1] == 'Хліб' and backpack[-2] == 'Чек':
                        print('Вітаю!!! Ти повертаєшся додому.')
                        done = True
                else:
                    print('У вас немає ' + fight_with)
            else:
                print('Досить бути шизіком повітря! Там нікого нема!')
        elif command == '3':
            if item is not None:
                print('Ти підібрав ' + item.get_name() + ' у свій рюкзак.')
                backpack.append(item.get_name())
                current_room.set_item(None)
            else:
                print('Тут нічого брати!')
        else:
            print('Я незнаю як ' + command)

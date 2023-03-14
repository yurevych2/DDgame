'''
Module with required classes to import.
'''

class Room:
    '''Class for shops.'''
    word = {'південь': 'північ', 'північ': 'південь', 'захід': 'схід', 'схід': 'захід'}
    def __init__(self, name):
        '''Initialization.'''
        self.name = name
        self.item = None
        self.links = {}
        self.info = {}
        self.character = None
        self.description = ''

    def __str__(self):
        '''String representation.'''
        return self.name

    def set_description(self, description):
        '''Set description.'''
        self.description = description

    def get_details(self):
        '''Return information.'''
        print(f'{self.name}\n--------------------\n{self.description}. {str(self.info)}.')

    def link_shop(self, shop, direction):
        '''Create map.'''
        self.info.update({Room.word.get(direction): shop.name})
        self.links.update({Room.word.get(direction): shop})

    def set_character(self, inhabitant):
        '''Create a character.'''
        self.character = inhabitant
    
    def get_character(self):
        '''Return the name.'''
        return self.character
    
    def set_item(self, item):
        '''Set item.'''
        self.item = item

    def get_item(self):
        '''Return all items in the room.'''
        return self.item

    def move(self, direct):
        '''Return possible directions.'''
        return self.links.get(direct)

class Item:
    '''Class for items.'''
    def __init__(self, name):
        '''Initialization.'''
        self.name = name
        self.text = ''

    def set_description(self, text):
        '''Set description.'''
        self.text = text

    def describe(self):
        '''Return the description.'''
        print(f'{self.name}.', self.text)

    def get_name(self):
        '''Return the name.'''
        return self.name

class Character:
    '''Class for characters.'''
    def __init__(self, name, appiarence):
        '''Initialisation.'''
        self.name = name
        self.appiarence = appiarence
        self.text = ''
        self.weakness = ''

    def set_conversation(self, text):
        '''Set text.'''
        self.text = text

    def set_weakness(self, weakness):
        '''Set the item the character is interested in.'''
        self.weakness = weakness

    def describe(self):
        '''Print the description.'''
        print(f'{self.name}.', self.appiarence)

    def talk(self):
        '''Print the text.'''
        print(self.text)

class Human(Character):
    '''Class for humans.'''
    def __init__(self, name, appiarence, item):
        '''Initialization.'''
        super().__init__(name, appiarence)
        self.item = item

    def exchange(self, other_item, _):
        '''Exchange an item.'''
        if self.weakness == other_item:
            self.item = other_item
            return 'Хліб'
        else:
            print('Мені це не всралося!')
            return other_item

class Seller(Character):
    '''Class for sellers.'''
    def __init__(self, name, appiarence):
        '''Initialization.'''
        super().__init__(name, appiarence)

    def exchange(self, other_item, backpack):
        '''Exchange an item.'''
        if self.weakness == other_item and len(backpack) > 1:
            return 'Чек'
        else:
            print('Перепрошую, приймаю лише готівку!')
            return other_item

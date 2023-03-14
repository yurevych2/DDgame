'''
Module with required classes to import.
'''

class Room:
    '''Class for rooms.'''
    word = {'південь': 'північ', 'північ': 'південь', 'захід': 'схід', 'схід': 'захід'}
    def __init__(self, name):
        '''Initialization.'''
        self.name = name
        self.links = {}
        self.info = {}
        self.character = None
        self.item = None
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

    def link_room(self, room, direction):
        '''Create map.'''
        self.info.update({Room.word.get(direction): room.name})
        self.links.update({Room.word.get(direction): room})

    def set_character(self, inhabitant):
        '''Create a character.'''
        self.character = inhabitant
    
    def get_character(self):
        '''Return the name.'''
        return self.character

    def set_item(self, item):
        '''Set item.'''
        self.item = item

    def move(self, direct):
        '''Return possible directions.'''
        return self.links.get(direct)

    def get_item(self):
        '''Return all items in the room.'''
        return self.item

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
        print(self.text)

    def get_name(self):
        '''Return the name.'''
        return self.name

class Enemy:
    '''Class for characters.'''
    num_of_defeation = 0
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
        '''Set the item that kill the character.'''
        self.weakness = weakness

    def describe(self):
        '''Print the description.'''
        print(self.appiarence)

    def talk(self):
        '''Print the text.'''
        print(self.text)

    def fight(self, weapon):
        '''Figth with the character.'''
        if weapon == self.weakness:
            Enemy.num_of_defeation += 1
            return True
        else:
            return False

    def get_defeated(self):
        '''Return the number of defeations.'''
        return Enemy.num_of_defeation

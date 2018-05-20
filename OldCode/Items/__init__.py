'''
Created on Mar 25, 2018

@author: Joshua
'''

import Production

class Item(object):
    '''
    Item.
    '''


    def __init__(self, item_type, amount, quality):
        '''
        Constructor
        '''
        self.item_type = item_type;
        self.amount = amount;
        self.quality = quality;
        
class ItemType(object):
    '''
    A type of item, e.g. Apple.
    '''
    
    def __init__(self, name, source, traits):
        self.name = name;
        self.source = source;
        self.traits = traits;

APPLE = ItemType("Apple", Production.ItemSource.FARM, {"Edibleness": 1, "Hardness": 0.2});
IRON_ORE = ItemType("Iron Ore", Production.ItemSource.MINE, {"Edibleness": 0.1, "Hardness": 0.4})
IRON = ItemType("Iron Ingot", [IRON_ORE], {"Edibleness": 0.1, "Hardness": 0.8})
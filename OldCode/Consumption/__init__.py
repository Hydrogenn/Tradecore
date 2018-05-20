'''
Created on Mar 27, 2018

@author: Joshua
'''

from enum import Enum
import time
import random

class Demand(object):
    
    '''
    Creates a real demand that can be cashed in for luxury points.
    '''
    def __init__(self, items, duration, points_awarded):
        self.items_left = items
        self.items_completed = []
        self.start_time = time.time()
        self.duration = duration
        self.points_awarded = points_awarded

'''
Indicates a type of demand.
'''
class DemandType(object):
    
    def __init__(self, demands):
        self.demands = demands
    
    '''
    Generates a demand from a given DemandType
    '''
    def generate(self, difficulty):
        
        item_count = round(difficulty * random.randrange(2,3))
        items = []
        
        for i in range(0,item_count):
            items.append(random.choice(self.demand))
        
        point_value = round(item_count/3)
        
        return Demand(items, 0, point_value)
'''
Created on Mar 26, 2018

@author: Joshua
'''

from enum import Enum
import time
import random

class Producer(object):
    '''
    Produces goods.
    '''
    
    def __init__(self, resource):
        self.resource = resource
        self.initial_time = time.time()
        self.last_used = self.initial_time
        self.storage = []
        
        if self.resource.source is ItemSource.MINE:
            self.supply = random.random(1) + 1 #either default or twice as much
            self.speed = random.random(1) + 1 #either default or twice as fast
    
    def get_type(self):
        return self.resource.source
    
    def view(self):
        print(time.time() - self.last_used)
        self.last_used = time.time()
        

class ItemSource(Enum):
    '''
    Indicates where the items come from.
    '''
    
    MINE = 0
    '''
    Limited supply per mine. Curve is derivative of logistic growth.
    '''
    
    FARM = 1
    '''
    Unlimited supply per farm. Curve is logistic.
    '''
    
    MADE = 2
    '''
    Supply is provided by the user. Curve is asymptotic.
    '''
    
    WILD = 3
    '''
    The details for this haven't exactly been worked out.
    '''

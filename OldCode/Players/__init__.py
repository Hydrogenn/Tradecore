'''
Created on Mar 25, 2018

@author: Joshua
'''

class Player(object):
    '''
    Has all the things players do.
    '''


    def __init__(self, username):
        '''
        Creates a new player with the given username.
        '''
        self.username = username
        self.luxury = 0
        self.factories = []
        self.kudos = []
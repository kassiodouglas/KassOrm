
from KassOrm import Migration

class migrate(Migration):   

    __type__ = 'alter'
    __table__ = 'users'
    __comment__ = ''

    def up(self):
        return self

    def down(self): 
        return self
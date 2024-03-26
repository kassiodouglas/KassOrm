
from KassOrm import Migration

class migrate(Migration): 

    __type__ = 'create'  
    __table__ = 'users'
    __comment__ = ''

    def up(self):
        self.id()
        self.datetime('created_at')

        return self

    def down(self): 
        self.drop_table()

        return self
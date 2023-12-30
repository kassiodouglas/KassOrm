
from KassOrm import Migration

class migrate(Migration): 
  
    __type__ = 'create'  
    __table__ = 'users'
    __comment__ = 'teste de criação das migrations, tabela users'
    
    def up(self):
        self.id().add()
        self.datetime('created_at').add()
        
        
        
    def down(self): 
        self.dropTableIfExists()        
        

        
        
        
        
        
      
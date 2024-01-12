
from KassOrm import Migration


class migrate(Migration):

    __type__ = 'create'
    __table__ = 'tb_users'
    __comment__ = 'tabela de usuarios'

    def up(self):
        self.id().add()
        self.datetime('created_at').current_timestamp().add()
        self.string('name').add()
        self.bigInteger('address_id').unsigned().add()

    def down(self):
        self.dropTableIfExists()

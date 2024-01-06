
from KassOrm import Querier, Migration, Modelr



#CRIE O BANCO kassorm_test

# #criando as migrations
# Migration().make_file_migration('create_tb_users', "app/database/migrations", 'tb_users', 'tabela de usuarios')

# #executando as  migrations
Migration().migrate("app/database/migrations")

# #criando o model
# Migration().make_file_model("app/database/models", "tb_users")

# Migration().rollback("app/database/migrations",1)

# #inserindo dados
usinsert = Querier().table('tb_users').insert({"name":"kassio xxx"})


#lendo pelo querier
users = Querier().table('tb_users').get()
print(users)


#lendo pelo modelr
# usersModel = Tb_users().get()
# print(usersModel)

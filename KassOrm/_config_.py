
"""
Conexões existentesCon
Configira aqui seus bnaco de dados

Drivers aceitos: Mysql
"""
connections = {
    
    "default": {
        "driver":"mysql",
        "pool_name": "ormkass_pool",
        "pool_size": 5,
        "pool_reset_session": True,
        "connect_timeout": 30,
        "user": "root",
        "password": "",
        "host": "127.0.0.1",
        "database": "nuvem_flask_api"
    },
    
}



"""
Define quais conexões  em 'connections' usam softDelete
Informe o nome da conexão e qual o campo padrão para determinar a exclusão

Padrão: default => deleted_at
"""
useSofdelete = {
    
    "default":{ "deleted_at"},
}







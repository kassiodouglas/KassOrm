from KassOrm import Creator, Migrater, Querier
from _app_test_.models.User import User
import time
from rich.console import Console
from rich.panel import Panel

console = Console()

conn = {
    "default": {
        "database": "kassorm",
        "port": 3306,
        "host": "localhost",
        "user": "root",
        "password": "",
    }
}

connection = conn["default"]

MIGRATIONS_DIR = "_app_test_/migrations"
MODELS_DIR = "_app_test_/models"


## criar migrations [OK] --------------------------------------------------
# Creator.make_migration(MIGRATIONS_DIR, "create_users", "Tabela de usuarios")
# time.sleep(1)
# Creator.make_migration(MIGRATIONS_DIR, "create_profiles", "Tabela de perfis")
# time.sleep(1)
# Creator.make_migration(MIGRATIONS_DIR, "create_users_profiles", "Amarração de usuaros e perfis")
# Creator.make_migration(MIGRATIONS_DIR, "alter_users", "Add deleted_at")
# Creator.make_migration(MIGRATIONS_DIR, "create_address", "Tabela de endereços")
# Creator.make_migration(MIGRATIONS_DIR, "alter_users_add_address", "Add address")


## migrar [OK] --------------------------------------------------
# Migrater(conn=connection, dir_migrations=MIGRATIONS_DIR).execute()


## insert [OK] --------------------------------------------------
# profile_ids = (
#     Querier(connection)
#     .table("profiles")
#     .insert(
#         [
#             {"name": "Admin", "description": "Acesso total"},
#             {"name": "User", "description": "Acesso Comun"},
#         ]
#     )
# )

# user_id = (
#     Querier(connection).table("users").insert({"name": "Dandara Souza", "login": "jan"})
# )
# Querier(connection).table("users_profiles").insert(
#     {"user_id": user_id, "profile_id": 2}
# )


## select [OK] --------------------------------------------------
# profiles = Querier(connection).table("profiles").get()
# profiles = "\n".join(str(profile) for profile in profiles)
# console.print(Panel(profiles, title="Select with get()"))

# user = Querier(connection).table("users").first()
# console.print(Panel(str(user), title="Select with first()"))

# profile = Querier(connection).table("profiles").select("name").where({"id": 1}).first()
# console.print(Panel(str(profile), title="Select with where() and first()"))


## update [OK] --------------------------------------------------
# user = (
#     Querier(connection).table("users").where({"id": 1}).update({"login": "jan.souza"})
# )
# console.print(Panel(str(user), title="Update with where()"))


## delete [OK] --------------------------------------------------
# user_id = (
#     Querier(connection).table("users").insert({"name": "kassio", "login": "kass.souza"})
# )
# delete = Querier(connection).table("users").where({"id": user_id}).delete()
# console.print(Panel(str(delete), title="Delete with where()"))


## criar models [OK] --------------------------------------------------
# Creator.make_model(MODELS_DIR, "User")
# Creator.make_model(MODELS_DIR, "Profile")
# Creator.make_model(MODELS_DIR, "Address")


## usando models -----------------------------------------

## select
# data = User().select("name").whereLike("name", "%kass%").get()
# console.print(Panel(str(data), title="Select with Modelr"))

# data = User().withTrashed().select("name").whereLike("name", "%kass%").get()
# console.print(Panel(str(data), title="Select withtrashed in Modelr"))


## insert
# user_id = User().insert({"name": "Kassio", "login": "Kass"})
# console.print(Panel(str(user_id), title="Insert with Modelr"))


## update
# user_id = User().where({"id": 1}).update({"name": "Kassio"})
# console.print(Panel(str(user_id), title="Update with Modelr"))

## delete
# user_id = User().where({"id": 1}).delete()
# console.print(Panel(str(user_id), title="Delete with Modelr"))


## softDelete

# delete
# user_id = User().where({"id": 3}).delete()
# console.print(Panel(str(user_id), title="Delete with softdelete with Modelr"))

# active
# user_id = User().where({"id": 2}).active()
# console.print(Panel(str(user_id), title="Active with softdelete with Modelr")).


# related

# users = User().withRelated("profiles").get()
# console.print(users)

users = User().withRelated("address").get()
console.print(users)

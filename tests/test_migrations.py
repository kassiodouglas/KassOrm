from KassOrm import Creator, Migrater, Querier, Conn
import os
import shutil
import pytest
import time

PROJECT_PATH = "tests/app_test"
MIGRATIONS_DIR = f"{PROJECT_PATH}/migrations"
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


@pytest.fixture()
def reset():
    yield

    Conn(connection).set_query("DROP TABLE IF EXISTS users").execute().exec()
    Conn(connection).set_query("DROP TABLE IF EXISTS _migrations_").execute().exec()
    if os.path.isdir(PROJECT_PATH):
        shutil.rmtree(PROJECT_PATH)


def test_criar_migration_prefix_create(reset):
    check = Creator.make_migration(dir=MIGRATIONS_DIR, migration_name="create_users")
    assert True == check


def test_criar_migration_prefix_alter(reset):
    check = Creator.make_migration(dir=MIGRATIONS_DIR, migration_name="alter_users")
    assert True == check


def test_executar_as_migrations_criadas(reset):
    Creator.make_migration(dir=MIGRATIONS_DIR, migration_name="create_users")
    time.sleep(1)
    Creator.make_migration(dir=MIGRATIONS_DIR, migration_name="alter_users")
    check = Migrater(conn=connection, dir_migrations=MIGRATIONS_DIR).execute()
    assert True == check


def test_executar_as_migrations_criadas_e_voltar_1(reset):
    Creator.make_migration(dir=MIGRATIONS_DIR, migration_name="create_users")
    time.sleep(1)
    Creator.make_migration(dir=MIGRATIONS_DIR, migration_name="alter_users")
    Migrater(conn=connection, dir_migrations=MIGRATIONS_DIR).execute()
    check = (
        Migrater(conn=connection, dir_migrations=MIGRATIONS_DIR).rollback(1).execute()
    )
    assert True == check


def test_executar_as_migrations_criadas_e_voltar_todos(reset):
    Creator.make_migration(dir=MIGRATIONS_DIR, migration_name="create_users")
    time.sleep(1)
    Creator.make_migration(dir=MIGRATIONS_DIR, migration_name="alter_users")
    Migrater(conn=connection, dir_migrations=MIGRATIONS_DIR).execute()
    check = (
        Migrater(conn=connection, dir_migrations=MIGRATIONS_DIR).rollback().execute()
    )
    assert True == check

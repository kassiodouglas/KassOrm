from KassOrm import Creator, Migrater, Querier
import os
import shutil
import pytest
import time

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


def test_raw():
    data = Querier(conn=connection).selectRaw("SELECT * FROM users limit 1")
    assert None != data


def test_select_get():
    data = Querier(conn=connection).table("users").select("*").get()
    assert None != data


def test_select_first():
    data = Querier(conn=connection).table("users").select("*").first()
    assert None != data


def test_tosql():
    data = Querier(conn=connection).table("users").select("*").toSql()
    assert dict == type(data)


def test_where():
    data = Querier(conn=connection).table("users").select("*").where({"id": 1}).get()
    assert None != data


def test_orWhere():
    data = (
        Querier(conn=connection)
        .table("users")
        .select("*")
        .where({"id": 1})
        .orWhere({"id": 10})
        .get()
    )
    assert None != data


def test_whereIn():
    data = (
        Querier(conn=connection)
        .table("users")
        .select("*")
        .whereIn("name", ["kassio", "douglas"])
        .get()
    )
    assert None != data


def test_orWhereIn():
    data = (
        Querier(conn=connection)
        .table("users")
        .select("*")
        .whereIn("name", ["kassio", "douglas"])
        .orWhereIn("sobrenome", ["mateus", "daniel"])
        .get()
    )
    assert None != data

import os, glob, importlib
from KassOrm._helpers import getStub
from datetime import datetime as dt

class Migration:
    __file__ = None
    __conn__ = None
    __type__ = None
    __table__ = None
    __comment__ = None

    __rollback__ = False

    def __init__(self) -> None:
        self.SQL = ""

        self.params = {}

        self.columns = []

        self.column = {}

        self.primary_key = None

    def up(self):
        return self

    def down(self):
        return self

    #  TIPOSS ------------------

    def add(self):
        self.columns.append(self.column)
        self.column = {}
        return

    def id(self):
        self.column["name"] = "id"
        self.column["type"] = "BIGINT"
        self.column["unsigned"] = "UNSIGNED"
        self.column["isNull"] = "NOT NULL"
        self.column["autoIncrement"] = "AUTO_INCREMENT"
        self.column["primary_key"] = "PRIMARY KEY"

        return self

    def string(self, name, qnt: int = 255):
        self.column["name"] = name
        self.column["type"] = f"VARCHAR({qnt})"
        self.column["isNull"] = "NOT NULL"

        return self

    def bigInteger(self, name):
        self.column["name"] = name
        self.column["type"] = f"BIGINT"
        self.column["isNull"] = "NOT NULL"

        return self

    def bigIntegerUnisigned(self, name):
        self.column["name"] = name
        self.column["type"] = f"BIGINT UNSIGNED"
        self.column["isNull"] = "NOT NULL"

        return self

    def text(self, name):
        self.column["name"] = name
        self.column["type"] = f"TEXT"
        self.column["isNull"] = "NOT NULL"

        return self

    def enum(self, name: str, values: list):
        str_values = ", ".join(map(lambda x: f'"{x}"', values))

        self.column["name"] = name
        self.column["type"] = f"ENUM({str_values})"
        self.column["isNull"] = "NOT NULL"

        return self

    def integer(self, name: str, qnt: int = None):
        self.column["name"] = name

        if qnt != None:
            self.column["type"] = f"INT({qnt}) ZEROFILL UNSIGNED"
        else:
            self.column["type"] = f"INT"
        self.column["isNull"] = "NOT NULL"

        return self

    def datetime(self, name: str):
        self.column["name"] = name
        self.column["type"] = "DATETIME"
        self.column["isNull"] = "NOT NULL"

        return self

    # TIPOSS-----------

    # TOOLS-----------

    def nullable(self):
        self.column["isNull"] = "NULL"

        return self

    def unsigned(self):
        self.column["unsigned"] = "UNSIGNED"

        return self

    def comment(self, comment: str):
        self.column["comment"] = f"COMMENT '{comment}' "
        return self

    def unique(self, columns: list = None, name=None):
        if columns != None or name != None:
            uniq = ""
            for col in columns:
                uniq += f"{col}, "

            uniq = uniq[:-2]

            self.column["unique_key"] = f" UNIQUE KEY {name} ()"
            return self
        else:
            self.column["unique"] = f"UNIQUE"
            return self

    def current_timestamp(self):
        self.column["current_timestamp"] = "DEFAULT CURRENT_TIMESTAMP"

        return self

    def update_timestamp(self):
        self.column["on_update_timestamp"] = "ON UPDATE CURRENT_TIMESTAMP"

        return self

    # TOOLS-----------

    def addColumn(self):
        self.column["add"] = "ADD COLUMN "

        return self

    def dropColumn(self):
        print("dropColumn in dev")

        return self

    def after(self, column: string):
        self.column["after"] = f"AFTER {column}"
        return self

    def first(self, column: string):
        self.column["first"] = f"FIRST {column}"
        return self

    def generate_sql(self):
        if self.__type__ in ["create", "alter"]:
            self.up()

        elif self.__type__ == "drop":
            self.down()

        if self.__type__ == "create" and self.__rollback__ == False:
            self.SQL = f"CREATE TABLE IF NOT EXISTS {self.__table__} {'('}"

            for col in self.columns:
                column = ""
                for value in col.values():
                    column += f"{value} "

                self.SQL += f"{column}, "

            if self.primary_key != None:
                self.SQL += f"PRIMARY KEY ({self.primary_key})"

            self.SQL = self.SQL[:-2]
            self.SQL += ");"

        elif self.__type__ == "alter" and self.__rollback__ == False:
            self.SQL = f"ALTER TABLE {self.__table__} "

            for col in self.columns:
                column = ""
                for value in col.values():
                    column += f"{value} "

                self.SQL += f"{column}, "

            self.SQL = self.SQL[:-2]

        else:
            print("DROP")

    def dropTableIfExists(self):
        self.SQL = f"DROP TABLE IF EXISTS {self.__table__};"

    def execute(self, rollback: bool = False):
        if rollback == False:
            self.generate_sql()
        else:
            self.dropTableIfExists()

        try:
            # db.get_engine(self.__conn__).connect().execute(statement=text(self.SQL),parameters=self.params)
            return True
        except Exception as err:
            return err

    def color(self, code=""):
        """Cores para usar no terminal"""

        if code == "green":
            return "\033[0;32m"

        elif code == "yellow":
            return "\033[0;33m"

        elif code == "red":
            return "\033[0;31m"

        else:
            return "\033[m"

    def create_table_migrations(self, conn: str):
        sql = "CREATE TABLE IF NOT EXISTS _migrations_ (date DATETIME NOT NULL, migration VARCHAR(255) NOT NULL UNIQUE, description VARCHAR(255) NULL);"
        # db.get_engine(conn).connect().execute(statement=text(sql))

    def drop_table_migrations(self, conn: str):
        sql = "DROP TABLE IF EXISTS _migrations_"
        # db.get_engine(conn).connect().execute(statement=text(sql))

    def save_migration_executed(
        self, conn: str, migration: str, description: str = None
    ):
        try:
            sql = """INSERT INTO _migrations_ (date, migration, description) VALUES (NOW(), :migration, :description)"""
            # with db.get_engine(conn).connect() as cursor:
            #     cursor.execute(
            #         text(sql),
            #         parameters={"migration": migration, "description": description},
            #     )
            #     cursor.commit()

            return True
        except Exception as err:
            print(err)
            return False

    def has_migration_executed(self, conn: str, migration: str):
        sql = """SELECT migration FROM _migrations_ WHERE migration = :migration"""
        # cursor = (
        #     db.get_engine(conn)
        #     .connect()
        #     .execute(text(sql), parameters={"migration": migration})
        # )
        # return cursor.fetchone()

    def delete_migration_executed(self, conn, migration):
        sql = f"DELETE FROM _migrations_ WHERE migration = '{migration}'"
        # db.get_engine(conn).connect().execute(statement=text(sql))

    def execute_all_migrations(self, pathmodule: str):
        if pathmodule == "api":
            app = f"core/modules/{pathmodule}/database/migrations"
            mod = "core.modules"
        else:
            app = f"apps/{pathmodule}/database/migrations"
            mod = "apps"

        self.create_table_migrations(pathmodule)

        migrations = glob.glob(os.path.join(app, "*.py"))

        fail = False
        for migration in migrations:
            file = os.path.basename(migration).replace(".py", "")

            if self.has_migration_executed(pathmodule, file) == None:
                module_name = f"{mod}.{pathmodule}.database.migrations.{file}"
                module = importlib.import_module(module_name)
                result = module.migrate().execute()

                if result == True and fail == False:
                    self.save_migration_executed(
                        pathmodule, file, module.migrate().__comment__
                    )

                    print(f"{file} {self.color('green')}[OK]{self.color()}")
                else:
                    print(f"{file} {self.color('red')}[Fail]{self.color()}")
                    print(f"{result}\n")
                    fail = True
                    return False

            else:
                print(f"{file} {self.color('yellow')}[ALREADY EXISTS]{self.color()}")

    def drop_all_migrations(self, pathmodule: str):
        app = f"apps/{pathmodule}/database/migrations"
        migrations = glob.glob(os.path.join(app, "*.py"))

        self.drop_table_migrations(pathmodule)

        for migration in migrations:
            file = os.path.basename(migration).replace(".py", "")
            module_name = f"apps.ga_plin.database.migrations.{file}"
            module = importlib.import_module(module_name)
            module.migrate().execute(True)

            print(f"{file} {self.color('yellow')} [DROPPED]" + self.color())

        def toSql(self):
            self.generate_sql()

            print(self.SQL)

            return self.SQL

        # def types(self):

        #     # Números Inteiros:
        #     TINYINT
        #     SMALLINT
        #     MEDIUMINT
        #     INT ou INTEGER
        #     BIGINT

        #     # Números Decimais/Floating-Point:
        #     FLOAT
        #     DOUBLE
        #     DECIMAL ou NUMERIC

        #     # Datas e Horas:
        #     DATE
        #     TIME
        #     DATETIME
        #     TIMESTAMP
        #     YEAR

        #     # Texto e Caracteres:
        #     CHAR
        #     VARCHAR
        #     TEXT
        #     TINYTEXT
        #     MEDIUMTEXT
        #     LONGTEXT

        #     # Binários:
        #     BINARY
        #     VARBINARY
        #     BLOB
        #     TINYBLOB
        #     MEDIUMBLOB
        #     LONGBLOB

        #     # Valores Booleanos:
        #     BOOLEAN ou BOOL
        #     BIT

        #     # Outros Tipos Especiais:
        #     ENUM
        #     SET

        #     # Tipos Espaciais (para dados geoespaciais):
        #     GEOMETRY
        #     POINT
        #     LINESTRING
        #     POLYGON
        #     MULTIPOINT
        #     MULTILINESTRING
        #     MULTIPOLYGON
        #     GEOMETRYCOLLECTION

    def make_file_migration(self, name_migration, dir_migration, comment:str=''):
        
        print("make_file_migrationmake_file_migrationmake_file_migrationmake_file_migration")
        name_migration = name_migration.lower()

        if os.path.isdir(dir_migration) == False:
            os.makedirs(dir_migration)

        if "create" in name_migration:
            content = getStub("migration_create.stub")
            table = name_migration.replace("create_", "")
        else:
            content = getStub("migration_alter.stub")
            table = name_migration
            
        content = content.replace("%COMMENT%", f"'{comment.lower()}'" if comment!= '' else "''") 
        content = content.replace("%TABLE%", table.lower())   
    
        filename = dt.now() .strftime("%Y_%m_%d__%H%M%S" ) +"_"+ name_migration + ".py"
        file = open(f"{dir_migration}/{filename}", 'w+')  
        file.writelines(content)   
        file.close()             
from pathlib import Path
import os,shutil
import pytest
from KassOrm.Migration import Migration  


_PATH_ = Path("_tests_results_/tests_migrations")

@pytest.fixture
def reset_migration_tests():
    if os.path.isdir(_PATH_) == True:
        shutil.rmtree(_PATH_)
    os.makedirs(f"{_PATH_}")  
    



def test_create_file_migration(reset_migration_tests):       
        
    name_migration = "create_users" 
    dir_migration = Path(f"{_PATH_}/api/database")  
    comment = "teste de criação das migrations, tabela users"
    
    Migration().make_file_migration(name_migration, dir_migration, comment)
    
    assert os.path.isdir(dir_migration), f"Migration {name_migration} not created!"
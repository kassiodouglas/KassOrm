from app import *
import os
from dotenv import load_dotenv
from dotenv import dotenv_values
load_dotenv(".env")

env = {
    **os.environ,  # override loaded values with environment variables    
    **dotenv_values(".env"),  # load shared development variables
    **dotenv_values(".env.prod"),  # load sensitive variables
} 

print(os.getenv("BD_HOST"))
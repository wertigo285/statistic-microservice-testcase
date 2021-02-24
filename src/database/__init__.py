import os

from dotenv import load_dotenv

dotenv_path = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), '.env')
if os.path.exists(dotenv_path):
    load_dotenv(dotenv_path)

SQL = os.environ.get('SQL') == 'True'
if SQL: 
    from .crud import Base as Base
else:
    from .in_memory import Base as Base

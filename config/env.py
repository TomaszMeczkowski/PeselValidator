from pathlib import Path
from environ import Env


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Init env
env = Env()

# Take environment variables from .env a file
Env.read_env(BASE_DIR / 'config' / '.env')

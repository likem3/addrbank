import os
from dotenv import load_dotenv


load_dotenv()

SECRET_KEY = os.getenv('SECRET_KEY')

ENVIRONMENT_SETTING = os.getenv('ENVIRONMENT_SETTING')

if ENVIRONMENT_SETTING not in ['local', 'development', 'production']:
    print('please provide correct ENVIRONMENT_SETTING on your/project/dir/.env')

if ENVIRONMENT_SETTING == 'production':
    try:
        from main.settings.settings_productions import *
    except:
        print(f'please provide {ENVIRONMENT_SETTING}.py')

elif ENVIRONMENT_SETTING == 'development':
    try:
        from main.settings.settings_development import *
    except:
        print(f'please provide {ENVIRONMENT_SETTING}.py')

else:
    try:
        from main.settings.settings_local import *
    except:
        print(f'please provide {ENVIRONMENT_SETTING}.py')

# write env settings here
SAFE_USER_KEY = os.getenv('SAFE_USER_KEY')
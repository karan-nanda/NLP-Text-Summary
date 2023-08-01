import os
from pathlib import Path
import logging


logging.basicConfig(level=logging.INFO, format='[%(asctime)]: %(message)s:')

project_name = 'TextSummarizer'

list_of_files= [
    '.github/workflows/.gitkeep',
    f'src{project_name}/__init__.py',
    f'src{project_name}/components/__init__.py',
    f'src{project_name}/utils/__init__.py',
    f'src{project_name}/utils/common.py',
    f'src{project_name}/logging//__init__.py', #Pretty sure there is supposed to only one slash
    f'src{project_name}/config/__init__.py',
    f'src{project_name}/config/configuration.py',
    f'src{project_name}/pipeline/__init__.py',
    f'src{project_name}/entity/__init__.py',
    f'src{project_name}/constants/__init__.py',
    "config/config.yaml",
    'params.yaml',
    'app.py',
    'main.py',
    'DockerFile',
    'requirements.txt',
    'setup.py',
    'research/trials.ipynb',
    ]

for filepath in list_of_files:
    filepath = Path(filepath)
    fileDirectory, filename = os.path.split(filepath)
    
    if fileDirectory != '':
        os.makedirs(fileDirectory, exist_ok=True)
        logging.info(f'Creating directory : {fileDirectory} for the file{filename}')
                     
    if(not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, 'w') as f:
            pass
            logging.info(f'Creating empty file: {filepath}')
            
    else:
        logging.info(f'{filename} already exists')
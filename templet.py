import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s %(message)s')

projecct_name = 'TextSummarizer'

list_of_files =[
    '.github/workflows/.gitkeep',
    f"src/{projecct_name}/__intit__.py",
    f"src/{projecct_name}/components/__intit__.py",
    f"src/{projecct_name}/utils/__intit__.py",
    f"src/{projecct_name}/utils/common.py",
    f"src/{projecct_name}/logging/__intit__.py",
    f"src/{projecct_name}/config/__intit__.py",
    f"src/{projecct_name}/config/configuration/__intit__.py",
    f"src/{projecct_name}/pipeline/__intit__.py",
    f"src/{projecct_name}/entity/__intit__.py",
    f"src/{projecct_name}/constants/__intit__.py",
    'config/config.yaml',
    'params.yaml',
    'app.py',
    'main.py',
    'Dockerfile',
    'requirments.txt',
    'setup.py',
    'research/trails.ipynb',
    'test.py'
    
]


for filepath in list_of_files:
    filepath = Path(filepath)
    filedir,filename =  os.path.split(filepath)
    
    
    if filedir != '':
        os.makedirs(filedir,exist_ok=True)
        logging.info(f"creating directory :{filedir} for the file {filename}")
        
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath,'w') as f:
            pass
            logging.info(f"Creating empty file: {filepath}")
    else:
        logging.info(f"File already exists: {filepath}")       
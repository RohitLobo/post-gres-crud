from configparser  import ConfigParser,NoSectionError
from typing import Dict
def config (filename:str,section:str) -> dict:
    parser = ConfigParser()
    parser.read(filename)
    db_config = {}
    if parser.has_section:
        # print((parser.items(section)))
        for config in parser.items(section):
            db_config[config[0]]= config[1]
    else:
        raise NoSectionError('Section {section} not found')
        
    return db_config 

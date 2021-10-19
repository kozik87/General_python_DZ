# 2.	*(вместо 1) Написать скрипт, создающий из config.yaml стартер для проекта со следующей структурой:
# |--my_project
#    |--settings
#    |  |--__init__.py
#    |  |--dev.py
#    |  |--prod.py
#    |--mainapp
#    |  |--__init__.py
#    |  |--models.py
#    |  |--views.py
#    |  |--templates
#    |     |--mainapp
#    |        |--base.html
#    |        |--index.html
#    |--authapp
#    |  |--__init__.py
#    |  |--models.py
#    |  |--views.py
#    |  |--templates
#    |     |--authapp
#    |        |--base.html
#    |        |--index.html

import os
import yaml

with open('ДЗ 7/config.yml') as f:
    content = yaml.safe_load(f)

def create_path(values, prefix =""):
    for derictory, paths in values.items():
        dir_path = os.path.join(prefix, derictory)
        os.makedirs(dir_path, exist_ok=True)
        if isinstance(paths, dict):
            create_path(paths, dir_path)
        else:
            for i in paths:
                if isinstance(i, dict):
                    create_path(i, dir_path)
                elif isinstance(i, str):
                    with open(os.path.join(dir_path, f'{i}'), 'w') as _:
                        pass

create_path(content)




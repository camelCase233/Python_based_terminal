import os
from pathlib import Path

home_dir = Path(os.path.expanduser('~'))

with open('current_dir.txt', 'w') as file:
    file.write(str(home_dir))
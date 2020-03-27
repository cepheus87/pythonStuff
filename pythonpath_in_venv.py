# https://stackoverflow.com/questions/4757178/how-do-you-set-your-pythonpath-in-an-already-created-virtualenv/17963979#17963979
# add export PYTHONPATH="/the/path/you/want" in /bin/activate

import os
try:
        user_paths = os.environ['PYTHONPATH'].split(os.pathsep)
except KeyError:
        user_paths = []

print(user_paths)

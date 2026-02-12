"""Load environment variables defined in ``.env`` and expose them as paths."""

import os
from dotenv import dotenv_values

here = os.path.dirname(__file__)
project_root = os.path.abspath(os.path.join(here, "..", ".."))
repo_root = os.path.abspath(os.path.join(project_root, ".."))

env_path = os.path.join(project_root, ".env")
if not os.path.exists(env_path):
    env_path = os.path.join(repo_root, ".env")

CONFIG = dotenv_values(env_path)
for key, value in CONFIG.items():
    if value is not None:
        path = os.path.join(project_root, value)
        path = path.replace("\\", os.sep)
        globals()[key] = os.path.normpath(path)

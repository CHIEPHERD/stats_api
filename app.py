#!/usr/bin/env python3
from src.main import main
from src.jobs import jobs
import os


file = open(".env", "r")
envs = file.read().splitlines()

for env in envs:
    if env == "":
        continue
    key, value = env.split("=")
    if not key in os.environ:
        os.environ[key] = value

jobs.jobs()
# main()

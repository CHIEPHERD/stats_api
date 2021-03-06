#!/usr/bin/env python3
from src.main import main
import os


file = open(".env", "r")
envs = file.read().splitlines()

for env in envs:
    key, value = env.split("=")
    if not key in os.environ:
        os.environ[key] = value

main()

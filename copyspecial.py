#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Copyspecial Assignment"""

# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

import re
import os
import shutil
import subprocess
import argparse

# This is to help coaches and graders identify student assignments
__author__ = "Ybrayym Abamov"


# +++your code here+++
# Write functions and modify main() to call them


def get_special_paths(dir):
    special_files = []
    list_paths = os.listdir(dir)
    for file in list_paths:
        match_obj = re.search(r'__(\w+)__', file)
        if match_obj:
            abs_path = os.path.abspath(os.path.join(dir, file))
            special_files.append(abs_path)
    return special_files


def copy_to(paths, dir):
    # check if destination of the dir exists
    if not os.path.isdir(dir):
        os.makedirs(dir)
    # at this point the destination of the dir exists
    # let's start copying
    for file in paths:
        dest = os.path.join(dir, os.path.basename(file))
        print('copying source = {} dest = {} '.format(file, dest))
        shutil.copy(file, dest)


def zip_to(paths, zippath):
    cmd = ['zip', '-j', zippath]
    cmd.extend(paths)
    print("Command I'm going to do: ")
    print(cmd)
    output = subprocess.check_output(cmd)
    print(output)


def main():
    # This snippet will help you get started with the argparse module.
    parser = argparse.ArgumentParser()
    parser.add_argument('--todir', help='dest dir for special files')
    parser.add_argument('--tozip', help='dest zipfile for special files')
    parser.add_argument('from_dir', help='returns directories')
    # TODO need an argument to pick up 'from_dir'
    args = parser.parse_args()
    # TODO you must write your own code to get the cmdline args.
    # Read the docs and examples for the argparse module about how to do this.

    # extracintg arguments from parser
    fromdir = args.from_dir
    copy_dir = args.todir
    zip_dir = args.tozip

    special_paths = get_special_paths(fromdir)

    # deciding where to send the special file
    if copy_dir:
        copy_to(special_paths, copy_dir)
    elif zip_dir:
        zip_to(special_paths, zip_dir)
    else:
        print(special_paths)

    # Parsing command line arguments is a must-have skill.
    # This is input data validation.
    # If something is wrong (or missing) with any
    # required args, the general rule is to print a usage message and exit(1).

    # +++your code here+++
    # Call your functions


if __name__ == "__main__":
    main()

#!/usr/bin/python
# -*- coding: utf-8 -*-
import subprocess
import sys
import time
import os

try:
    trashcan = open(os.devnull, "w")
    actualpath = os.getcwd()
    arglength = len(sys.argv[1:])
    option = sys.argv[1]

    def autogit (filepath, message):
    	#subprocess.call(["git", "init"])
    	filepathsplit = filepath.split('/')
    	filename = filepathsplit[-1]
    	path = "/".join(filepathsplit[:-1])
        os.chdir(path)
        subprocess.call(["git", "add", filename], stdout=trashcan)
        subprocess.call(["git", "commit", "-m", message], stdout=trashcan)
        subprocess.call(["git", "push"])

    def help():
        print "Simple usage: ./autogit.py [OPTION] PATH MESSAGE URL"
        print "PATH = the path to the file, e.g: /home/XXX/clonedrepository/example.py"
        print "URL = the url of the GitHub repository"
        print "OPTIONS \n==============="
        print "-h displays this message"
        print "-m introduce a message to commit (by default the date)"
        print "================"
        print "WARNING: you must have git configured (git config)"

    if arglength == 1 and option != "-h" and option != "-m":
    	filepath = sys.argv[1]
        localtime = time.strftime("%x")
        autogit(filepath, localtime)
    elif option == "-m":
        filepath = sys.argv[2]	
        message = sys.argv[3]
        print message
        autogit(filepath, message)
    elif option == "-h":
        print help()
    else:
        print help()

    trashcan.close()
    os.chdir(actualpath)
except (SyntaxError, KeyboardInterrupt):
    print "Something happened (use autogit -h for help)."
    print "If the that didn't please report the bug."

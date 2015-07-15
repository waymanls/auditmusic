#!/usr/bin/python
# This a change from master branch. Can it be seen?
#import musicbrainz2.webservice as ws
import time
import sys, parser, os, re
import argparse

parser = argparse.ArgumentParser(description='Music Scanner')
parser.add_argument('-d','--directory', help='Directory', required=True)
args = parser.parse_args()


#M = sys.argv[1]
x = 0
L = []
badalbums = []


for dirName,subdirList,fileList in os.walk(args.directory):
    #Prune bad directories from list
    if re.search(r'([Ss]ingles|lost\+found|System\ Volume\ Information|.*RECYCLE?)',dirName):
        pass
    else:
        try:
            # Separate out Artist Name from Album Title
            em = re.search(r'^.*/(music|MUSIC|Music)/(.*)_-_(.*)/?',dirName)
            # Prune off extra "/". if group 2 contains a "/" character, don't print
            if re.search(r'/',em.group(2)):
                pass
            else:
                #print em.group(1) ,"~~~", em.group(2)
                for fname in fileList:
                    # Get actual music files, not other files
                    if re.search(r'\.(flac|wav|mp3|m4a|mp4|wma)',fname):
                        L.append(fname)
                        x = x+1
                if x == 0:
                    pass
                else:
                    pass
                    # Print out total files contained in Album
                    #print x , "songs in", em.group(1) , em.group(2)

                    # Do you want to print this data to stdout or write it to a file? 
                    print x , "songs in", dirName
                    # Function that compares my albums to musicBrainz goes here!
                    #
                    # End
                L = []
                x = 0
        except AttributeError:
            print "Cannot parse ", dirName
            badalbums.append(dirName)

#This is a comment to test branches
# vim:ts=4:expandtab:

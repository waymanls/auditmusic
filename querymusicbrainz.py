#!/usr/bin/python

import musicbrainzngs
import argparse
import sys
import re
import json
import io

#parser = argparse.ArgumentParser(description='Audit Music collection')
#parser.add_argument('-a','--artist', help='Artist Name', required=True)
#parser.add_argument('-t','--title', help='Album Title', required=True)
#args = parser.parse_args()
musicbrainzngs.set_useragent(
    "auditmusic musicbrainz query",
    "0.1",
    "https://github.com/luckyleftie/auditmusic/",
)
# Add getopts thing. So you can run it like this
# querymusicbrainz.py -a <ARTIST> -t <ALBUM TITLE>
#result = musicbrainzngs.search_releases(artist=args.artist, release=args.title)
actual = []
def gather(artist,title):
    result = musicbrainzngs.search_releases(artist=artist, release=title)
    for item in result['release-list']:
        #print json.dumps(item,sort_keys=True,indent=4, separators=(',', ': '))
        if (re.search(artist, item['artist-credit'][0]['artist']['name'],flags=re.IGNORECASE) and re.search(artist, item['artist-credit-phrase'],flags=re.IGNORECASE) and re.search(title, item['title'],flags=re.IGNORECASE) and re.search('Album', item['release-group']['primary-type'])):
        #if (item['artist-credit'][0]['artist']['name'] == artist and item['title'] == title):
            actual.append(item['id'])
            print actual[0]
            foo = musicbrainzngs.get_release_by_id(actual[0],includes=['recordings','release-groups'])
        #elif (item['title'] == title):
        #    actual = item['id']
        #    foo = musicbrainzngs.get_release_by_id(actual,includes=['recordings','release-groups'])
    #print "Positions: ",foo['release']['medium-list'][0]['track-list'][-1]['position'], "Tracks: ",foo['release']['medium-list'][0]['track-list'][-1]['number']
    return foo['release']['medium-list'][0]['track-list'][-1]['number']
# vim:ts=4:expandtab:

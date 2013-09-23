#!/usr/bin/python

import musicbrainzngs
import argparse
import sys

parser = argparse.ArgumentParser(description='Audit Music collection')
parser.add_argument('-a','--artist', help='Artist Name', required=True)
parser.add_argument('-t','--title', help='Album Title', required=True)
args = parser.parse_args()


musicbrainzngs.set_useragent(
    "auditmusic musicbrainz query",
    "0.1",
    "https://github.com/luckyleftie/auditmusic/",
)

# Add getopts thing. So you can run it like this
# querymusicbrainz.py -a <ARTIST> -t <ALBUM TITLE>

result = musicbrainzngs.search_releases(artist=args.artist, release=args.title)
for item in result['release-list']:
    if (item['artist-credit'][0]['artist']['name'] == args.artist and item['title'] == args.title):
        actual = item['id']
        foo = musicbrainzngs.get_release_by_id(actual,includes=['recordings','release-groups'])
        #print foo
print "Positions: ",foo['release']['medium-list'][0]['track-list'][-1]['position'], "Tracks: ",foo['release']['medium-list'][0]['track-list'][-1]['number']



# vim:ts=4:expandtab:

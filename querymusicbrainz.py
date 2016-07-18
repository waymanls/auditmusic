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
actual = []
def gather(artist,title,total):
  count = 0
  result = musicbrainzngs.search_releases(artist=artist, release=title, limit=5)
  for item in result['release-list']:
    #print json.dumps(item,sort_keys=True,indent=4, separators=(',', ': '))
    if (re.search(artist, item['artist-credit'][0]['artist']['name'],flags=re.IGNORECASE) and re.search(artist, item['artist-credit-phrase'],flags=re.IGNORECASE) and re.search(title, item['title'],flags=re.IGNORECASE) and re.search('Official', item['status'],flags=re.IGNORECASE) and total == item['medium-track-count']):
      #actual.append(item['id'])
      #print actual[0]
      count = item['medium-track-count']
  #return foo['release']['medium-track-count']
  return count
# vim:ts=4:expandtab:

#!/usr/bin/python

import musicbrainzngs

musicbrainzngs.set_useragent(
    "auditmusic musicbrainz query",
    "0.1",
    "https://github.com/luckyleftie/auditmusic/",
)


#album_id="45562d89-0c2a-481d-a367-9977891e32bd"
result = musicbrainzngs.search_releases(artist='Ray Cash', release='Cash on Delivery')
#album = musicbrainzngs.get_release_by_id(album_id,includes=['artists'])
print result, "\n"
#print album['release']
for item in result['release-list']:
    print item, "\n"
    #if (item['artist-credit'][0]['artist']['name'] == "French Montana" and item['release-group']['type'] == "Album"):
        #print item['artist-credit'][0]['artist']['name'],"-",item['title'],"-",item['id']
    #    actual = musicbrainzngs.get_release_by_id(item['id'],includes=['media'])
    #    print actual
        
#    print item['release-list'][0]['title'], "\n\n"

#print(u"{id}: {name}".format(id=artist['id'], name=artist["name"]))
# vim:ts=4:expandtab:

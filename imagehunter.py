#! /usr/bin/env python

import sys
import urllib
import urllib2
import simplejson
import os
import pprint
import random


DIR = os.path.abspath(os.path.dirname(sys.argv[0]))

def choose_random_search_term():
    SEARCH_WORD_LIST = os.path.join(DIR, 'searchoptions.txt')
    #SEARCH_WORD_LIST = '/usr/share/dict/words'

    search_terms = [
        line.strip()
        for line in open(SEARCH_WORD_LIST)
        if line.strip()
    ]

    return random.choice(search_terms)


if len(sys.argv) > 1:
    search_term = ' '.join(sys.argv[1:])
else:
    search_term = choose_random_search_term()

print 'Searching for %s' % (search_term,)

url = ('https://ajax.googleapis.com/ajax/services/search/images?' +
       urllib.urlencode(
           dict(
               v='1.0',
               q=search_term,
               userip='93.219.10.12',
               as_filetype='jpg',
           )
       )
   )

print 'Search url: %s' % (url,)

request = urllib2.Request(url, None, {'Referer': "softwareswirl.com"})
response = urllib2.urlopen(request)

# Process the JSON string.
results = simplejson.load(response)

#pprint.pprint(results)

urls = [
    result['url']
    for result in results['responseData']['results']
]

url = random.choice(urls)

print 'Image url: %s' % (url,)

request = urllib2.Request(url, None, {'Referer': "softwareswirl.com"})
response = urllib2.urlopen(request)

picture = response.read()

IMAGE_FILE = os.path.join(DIR, 'image.jpg')

open(IMAGE_FILE, 'wb').write(picture)
os.system('eog %s &' % (IMAGE_FILE,))


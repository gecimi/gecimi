#!/usr/bin/env python
#coding=utf-8

import json
import requests

__version__ = '0.0.1'


class Gecimi(object):

    def __init__(self):
        self.base_url = 'http://gecimi.com/api'


class Lyric(Gecimi):

    def __init__(self, song, artist=None, album=None):
        super(Lyric, self).__init__()
        if artist:
            self.path = '/lyric/%s/%s' % (song, artist)
        else:
            self.path = '/lyric/%s' % song

    def get(self):

        lrc = ''
        try:
            r = requests.get("".join((self.base_url, self.path)),
                             timeout=10, stream=False)
            content = r.content
            try:
                response = json.loads(content)
                if response['code'] == 0:
                    lyric_item = response['result'][0]
                    lrc_url = lyric_item['lrc']
                    lrc = requests.get(lrc_url).content
            except Exception, e:
                print e
        except Exception, e:
            print e
        return lrc


if __name__ == '__main__':
    lyric = Lyric('海阔天空')
    print lyric.get()
    lyric = Lyric('不再犹豫', 'Beyond')
    print lyric.get()

"""
    Banddisam: Band name disambiguation
    Copyright (C) 2011 Ramon Xuriguera

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""

import json
import urllib2
import re 

class LastfmWrapper(object):
    def __init__(self,min_tag_count=50):
        
        self.min_tag_count = min_tag_count
        self.api_key  = open("api_key").readline()
        #self.url_base = ''.join(["http://ws.audioscrobbler.com/2.0/?api_key=",self.api_key])    
        self.url_base = "http://query.yahooapis.com/v1/public/yql?format=json&callback=&env=store%3A%2F%2Fdatatables.org%2Falltableswithkeys&q="#show%20tables&diagnostics=true
    
    def _format_parameters(self, dict):
        return ''.join(map(lambda x: ''.join(['&',str(x),'=',dict[x]]),dict.keys()))
    
    def _get_result(self, url):
        result = urllib2.urlopen(url).read()
        return json.loads(result)
        
    
    def get_artist_top_tracks(self, artist):
        query = """
            select *
            from 
                lastfm.track.gettoptags 
            where 
                api_key="%s" and 
                artist="%s" and 
                track in (
                    select 
                        toptracks.track.name 
                    from 
                        lastfm.artist.gettoptracks 
                    where 
                        api_key="%s" and
                        artist="%s")""" % (self.api_key, artist, self.api_key, artist)
            
        query = re.sub("[\s]+","%20",query)
        url = ''.join([self.url_base, query])
        
        # TODO: Remove and uncomment
        f = open("sample.json")
        result = json.load(f)
        f.close()
        #result = self._get_result(url)
        
        tracks = {}
        for track in result["query"]["results"]["lfm"]:
            track = track['toptags']
            if 'tag' in track.keys():
                try:
                    track_tags =  [tag['name'] for tag in track['tag'] if (tag['name'].strip() and int(tag['count'])>self.min_tag_count)]
                    tracks[track['track']]=track_tags           
                except TypeError:
                    pass
        return tracks

if __name__=="__main__":
    print "BEGIN"
    x = LastfmWrapper()
    for song, tags in x.get_artist_top_tracks("Soko").items():
        print 'Song: ',song
        print '  Tags: ', tags,'\n'
    print "END"
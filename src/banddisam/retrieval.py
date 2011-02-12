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
        
        # TODO: Remove 
        #f = open("sample.json")
        #result = json.load(f)
        #f.close()
        result = self._get_result(url)
        
        tag_count = {}
        tracks = {}
        for track in result["query"]["results"]["lfm"]:
            track = track['toptags']
            if 'tag' in track.keys():
                track_tags = set([])
                try:
                    track_tags =  set([tag['name'] for tag in track['tag'] if (tag['name'].strip() and int(tag['count'])>self.min_tag_count)])                           
                except TypeError:
                    pass
                tracks[track['track']]=track_tags
                for tag in track_tags:
                    try:
                        tag_count[tag] += 1
                    except KeyError:
                        tag_count[tag] = 1
                
        return (tracks, tag_count)
    
    def presence_matrix(self, artist):
        (tracks, tag_count) = self.get_artist_top_tracks(artist)
        
        tags = sorted(tag_count, key=lambda x: 0-tag_count[x])[0:8]
        n_tags = len(tags)    
    
        # Generate presence matrix
        matrix = []    
        for index, track in enumerate(tracks):
    
            # Initialize tag presence
            tag_presence = [0 for i in range(0,n_tags)]
    
            for tag in tracks[track]:
                try:
                    tag_presence[tags.index(tag)] = 1
                except ValueError:
                    pass
            matrix.append(tag_presence)
        return (tracks,matrix)
    
    

if __name__=="__main__":
    print "BEGIN"
    x = LastfmWrapper()
    (tracks, tag_count) = x.get_artist_top_tracks("Soko") 
    
    for song, tags in tracks.items():
        print 'Song: ',song
        print '  Tags: ', tags,'\n'
        
    for tag, count in tag_count.items():
        print 'Tag: ',tag,' count: ',count
    print "END"
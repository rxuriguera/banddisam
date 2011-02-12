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
from bottle import route, run

from retrieval import LastfmWrapper
from clustering import Cluster

@route('/trackclusters/:artist', method='GET')
def track_clusters(artist):
    wrapper = LastfmWrapper()
    (tracks, matrix) = wrapper.presence_matrix(artist)
    
    c = Cluster()
    assignments = c.cluster(matrix)
    
    clusters = {}
    for index, track in enumerate(tracks):
        print assignments[index], " - ", track
        try:
            clusters[assignments[index]].append(track)
        except KeyError:
            clusters[assignments[index]] = [track]

    return ''.join(['clusterCallback(',json.dumps(clusters),')']);

@route('/injectjs', method='GET')
def hello():
    f = open("extension.js").read()
    return f

run(host='localhost', port=8080)
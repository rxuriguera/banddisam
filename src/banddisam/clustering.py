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


from scipy.cluster.hierarchy import fclusterdata


#class Cluster(object):
#    def __init__(self, tracks, threshold=0.3):
#        self.tracks = tracks
#        self.threshold = threshold
#        self.min_clust_size = 3
#        self.clusters = []
#
#    def _track_similarity(self, a_tags, b_tags):
#        intersection = len(a_tags.intersection(b_tags))
#        union = float(len(a_tags.union(b_tags)))
#        if not union:
#            return 0.0
#        else:
#            print intersection/union
#            return intersection/union
#    
#    def _cluster_similarity(self, track, cluster):
#        acum = 0
#        for ct in cluster:
#            acum += self._track_similarity(self.tracks[track], self.tracks[ct])
#        return acum/float(len(cluster))
#    
#    def _merge_clusters(self):
#        other_tracks = []
#        for index, clust in enumerate(self.clusters):
#            print "LEN: ", len(clust), " - ", self.min_clust_size
#            if len(clust) < self.min_clust_size:
#                self.clusters.remove(clust)
#                print len(self.clusters)
#                other_tracks.extend(clust)
#            else:
#                print 'This clust must not be removed ', clust
#        self.clusters.append(other_tracks)
#    
#    def cluster(self):              
#        for track in self.tracks:
#            # First cluster
#            if not self.clusters:
#                self.clusters.append([track])
#                continue
#            
#            assigned = False
#            for index, cluster in enumerate(self.clusters):
#                if self._cluster_similarity(track, cluster) > self.threshold:
#                    assigned = True
#                    cluster.append(track)
#                    break;
#            if not assigned:
#                self.clusters.append([track])
#                
#                
#        self._merge_clusters()
#                
            

        
class Cluster(object):       
    def cluster(self,matrix, threshold=3):
        return fclusterdata(matrix,threshold,criterion='maxclust',method="complete")


if __name__ == '__main__':
    pass
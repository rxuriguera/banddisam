Track Clustering for Artist Disambiguation
==========================================

About banddisam
---------------
At the moment, Last.fm is not offering any kind of 
artist  disambiguation and there is one single artist 
page for all the bands sharing the same name.

For instance, the following two albuns actually belong 
to  two different artists:
http://www.last.fm/music/SoKo/Two
(tags: love, mood, ambient)

http://www.last.fm/music/SoKo/I+Thought+I+Was+an+Alien


The aim of this project is to automatically disambiguate 
bands by creating clusters of tracks depending using the 
tracks' tags as attributes. In the example above, most of 
the tracks for the first album are tagged with words like 
"chillout", "mood", "ambient" while the tracks of the second 
album include tags like "indie", "pop", "french".

Obviously, for this method to work, we must assume that 
two artist with the same name will play different music 
genres.


Components
----------

- A Python webservice that computes track clusters 
using SciPy
- Chrome user script that modifies the layout
of last.fm's artist pages showing track clusters.


This proof of concept is released under the GPL license
and was developed as part of a Yahoo! Hack U event:
http://developer.yahoo.com/hacku/

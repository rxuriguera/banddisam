/*
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
*/

var clusterCallback = function (json) {
  chartstracks = document.getElementsByClassName("modulechartstracks")[0];

  console.log(chartstracks);
  
  var clusters = document.createElement("div");
  clusters.innerHTML = '<div class="module modulecharts modulechartstracks">' +
                       '<h2 class="heading"><span class="h2Wrapper">' +
                       'Multiple Artists?</span></h2> '+
                       '<div class="module-body chart chartweek current">';
                       
  for(var i in json){
    clusters.innerHTML = clusters.innerHTML+'<h3>Cluster '+i+'</h3><ul>';
    
    console.log(json[i]);
    
    for(k=0;k<=json[i].length-1;k++) {
      
      clusters.innerHTML = clusters.innerHTML+'<li><a href="">'+json[i][k]+'</a></li>';
    }
    clusters.innerHTML = clusters.innerHTML+'</ul>';
  }
  
  clusters.innerHTML = clusters.innerHTML+
                       '</div>'+
                       '</div>';
  
  if(chartstracks) {
    chartstracks.parentNode.insertBefore(clusters, chartstracks);
  }
}

var artist = document.getElementsByTagName('h1')[0].innerHTML;
if (artist) {
  var url = "http://localhost:8080/trackclusters/" + artist;

  console.log(url);
 
  var obj = document.createElement("script");
  obj.src=url;
  document.getElementsByTagName('body')[0].appendChild(obj);
} 
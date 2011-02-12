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
      
      clusters.innerHTML = clusters.innerHTML+'<li>'+json[i][k]+'</li>';
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
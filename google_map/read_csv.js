// convert csv file to Json array
function csv_JSON(csv){
  var lines=csv.split("\n"); // split ehch new line
  var result = []; // json var
  var headers=lines[0].split(","); // define headers line
  for(var i=1;i<lines.length;i++){ // for each elemnt (kavon / ellipse) in ellips 
      var obj = {}; 
      obj["Name"] = "AccessPoint"+i // set name for ellipse / kavon by number
      var currentline=lines[i].split(","); // split data by ','

      for(var j=0;j<headers.length;j++){
          obj[headers[j]] = currentline[j]; // insert each elemnt to json with headers, 
                                           //ex: {Name: "ellipse3", lat: xxxx, lon:yyyy
      }
      result.push(obj); // insert to json array
  }
  
  //return result; //JavaScript object
  return JSON.stringify(result); //JSON
}

function create_point(name, lat, long){

  var accessPoint = new google.maps.Circle({
      strokeColor: 'red', // fill color
      strokeOpacity: 0.8,
      strokeWeight: 2,
      fillColor: 'red',
      fillOpacity: 0.65,
      map: map,
      center: {lat: lat ,lng: long}, // location
      radius: 1000 ,// size
      text: name
      
});
};


function read_CSV(polygonDict, num) {
      var out = "";
      var color = '#990000';
      var num_file = "file"+(num).toString();
      // reset lists, for each file. 
      var info = [];

      var diamonds = [];
      mac_list = [];
      all_point[num_file] = {"diamonds":diamonds, "info": info};
      
      for( var e=0 ;e<polygonDict.length; e++) {
        var polygon = polygonDict[e];
        var long = parseFloat(polygon.long);
        var lat = parseFloat(polygon.lat);
        var name = parseFloat(polygon.name)
      create_point(name, lat, long)
    };
    updatepoint(all_point, num_file, info);
  };

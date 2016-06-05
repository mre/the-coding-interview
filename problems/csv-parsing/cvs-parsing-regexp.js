//solution usin regExp

module.exports= function(str){
	var numPattern= /^[\w]+/;
  var txtPattern= /^"[^"]+"/;
  var tmp;
  var res= [];
  
  while(str.length>0){
  	tmp= str.match(numPattern);
    if(tmp){
    	str= str.replace(numPattern,'').slice(1);
      res.push(parseInt(tmp[0]));
    }else{
    	tmp= str.match(txtPattern);
      if(tmp){
      	str= str.replace(txtPattern,'').slice(1);
        res.push(tmp[0].slice(1,-1));
      }else{
      	return -1;
      }
    }
  }
  
  return res;
};

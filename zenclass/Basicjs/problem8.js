function getProperty(obj, key){
 
if(obj.key==undefined){
    return false;
}
else{
console.log(obj.key);
}
}

getProperty(obj = {
    key:"value",
    });
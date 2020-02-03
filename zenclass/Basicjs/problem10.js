function removeproperty() {

 var myobj = {

    myproperty:true,
 }   
 delete myobj.myproperty;
 console.log( myobj.myproperty);   
}
removeproperty();
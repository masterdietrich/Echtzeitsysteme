
function createAjaxRequest(){
    let request;
    if(window.XMLHttpRequest){
        request = new XMLHttpRequest();
    }else{
        request = new ActiveXObject("Microsoft.XMLHTTP");
    }
    return request;
}


function getdate(){
    var today = new Date();
    var date = today.getFullYear()+'-'+(today.getMonth()+1)+'-'+today.getDate();
    let dateipfad= "js/verbrauchsdaten_"+date+".txt"
    console.log(dateipfad)
    countInput(dateipfad)
}

function countInput(dateipfad) {
    var request = createAjaxRequest();
    request.onreadystatechange = function(){
        let counter  =0
        if(4 === this.readyState && 200 === this.status) {
            let test = this.responseText;
            for(let i =0; i<test.length;i++){
                if(test[i]==='['){
                    console.log("true")
                    counter++;
                }

            }
        }
    }
    request.open("GET",dateipfad,true);
    request.send();
}

//setInterval(function (){
  //  getdate();
//},1000)

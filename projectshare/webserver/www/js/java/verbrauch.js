let week =[0,0,0,0,0,0,0]

function createAjaxRequest(){
    let request;
    if(window.XMLHttpRequest){
        request = new XMLHttpRequest();
    }else{
        request = new ActiveXObject("Microsoft.XMLHTTP");
    }
    return request;
}


async function getdate(n=0){
    var today = new Date();
    var date = today.getFullYear()+'-'+(today.getMonth()+1)+'-'+(today.getDate()-n)
    let dateipfad= "js/verbrauchsdaten_"+date+".txt"
  //  console.log(dateipfad)
    return countInput(dateipfad,n)
}


async function getWeek(){
    for(let i =0; i<7;i++){
        await getdate(i)
    }

    let sum = 0;
    let avg =0
    for(let i =0;i< week.length;i++){
        sum += week[i]
        if(week[i]>0){
            avg++
        }
    }
    sum = sum/avg
    for (let i = 0 ;i < week.length; i++) {
        if(week[i]==0) {
            week[i]=sum
        }
    }
    sum=0
   
   
   let wm = document.getElementById("weekcount")
    wm.innerText = sum.toString()
}


function countInput(dateipfad,i) {
    var request = createAjaxRequest();
    request.onreadystatechange = function(){
        let counter  =0
        if(4 === this.readyState && 200 === this.status) {
            let test = this.responseText;
            for(let i =0; i<test.length;i++){
                if(test[i]==='['){
                //    console.log("true")
                    counter++;
                }

            }
        }
	let dm = document.getElementById("countday").innerText = counter.toString()
	//week[i]=counter;
        //dm.innerText = week[6].toString()
        return counter
    }
    request.open("GET",dateipfad,true);
    request.send();
}

//setInterval(function (){
  //  getdate();
//},20000)

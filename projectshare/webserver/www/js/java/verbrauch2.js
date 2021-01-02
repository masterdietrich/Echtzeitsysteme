let mondayFlag = false
let week =[0,0,0,0,0,0,0]
const day = 86400000;
const UKW = 120;

function createAjaxRequest(){
    let request;
    if(window.XMLHttpRequest){
        request = new XMLHttpRequest();
    }else{
        request = new ActiveXObject("Microsoft.XMLHTTP");
    }
    return request;
}


async function getDate( n=0 ){
    let dateipfad= "js/verbrauchsdaten_"+generateDateipfad(n)+".txt"
    console.log(dateipfad)
    return countInput(dateipfad,n)
}



async function getWeek(){
    for(let i =0; i<7;i++){
        await getDate(i)
    }
    let counter =0
    let countDay=0
    for(let i =0 ;i < 7;i++){
        if(week[i]!==0){
            counter=counter+ week[i]
        }
//        else {
  //          countDay++
    //    }
    }
    //let weekly = Math.round(counter + (counter/(7-countDay)*countDay))
    //console.log(week)
    //let con = document.getElementById("Dweek")
    //con.innerText=weekly.toString()
    counter = Math.round(counter*100)
    counter = counter/100
    document.getElementById("week").innerText = counter + " kWh"	
}


function getMonth(){
    let today = new Date();
    let dateipfad= "js/verbrauchsmonth_"+(today.getMonth()+1)+"_"+today.getFullYear()+".txt"
    console.log(dateipfad)
    countMonth(dateipfad)
}


function countMonth(dateipfad) {
    var request = createAjaxRequest();
    request.onreadystatechange = function(){
        let counter  =0
        if(4 === this.readyState && 200 === this.status) {
            let test = this.responseText;
            for (let i =0;i<test.length;i++){
                if(test.charAt(i)==='['){
                    counter++
                }
            }
            month=counter
            counter = Math.round(counter/UKW*100)
            counter = counter/100
            document.getElementById("month").innerText= counter + " kWh"

        }
    }
    request.open("GET",dateipfad,true);
    request.send();
}






function countInput(dateipfad,i) {
    var request = createAjaxRequest();
    request.onreadystatechange = function(){
        let counter  =0
        if(4 === this.readyState && 200 === this.status) {
            let test = this.responseText;
            //console.log(test)
            for(let i =0; i<test.length;i++){
                if(test[i]==='['){
                    console.log("true")
                    counter++;
                }
            }
            let dm = document.getElementById("day")
            week[i]=counter/UKW;
            counter = Math.round(counter /UKW *100)
	    counter = counter/100
            if(i===0){
                dm.innerText = counter + " kWh"
               // document.getElementById("Dday").innerText =counter.toString()
		let text = this.responseText
                let data = new Blob([text], {type: 'text/plain'});
                var url = window.URL.createObjectURL(data);
                document.getElementById('download_link').href = url;
            }
            return counter
        }
    }
    request.open("GET",dateipfad,false);
    request.send();
}



function generateDateipfad(n){
     let today = new Date();
     let temp = new Date(today)
     today = new Date(today - day * n)

     if (!mondayFlag &&temp.getMonth()==today.getMonth()){
         let date = today.getFullYear() + '-'
         if (today.getMonth() + 1 > 9) {
             date = date + (today.getMonth() + 1) + '-'
         } else {
             date = date + '0' + (today.getMonth() + 1) + '-'
         }
         today.setDate(today.getDate())
         if ((today.getDate()) > 9) {
             date = date + (today.getDate());
         } else {
             date = date + '0' + (today.getDate());
         }
         if(today.getDay()==1) {
             mondayFlag = true;
         }
         return date
     }
     else{
         return "no_date"
     }
}




function init(){
    getDate();
    getWeek();
    getMonth()
}

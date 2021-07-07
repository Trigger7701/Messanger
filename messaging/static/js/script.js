reciv = null
function selectuser(reciver_id) {
    reciv = reciver_id
	url = '/chat/'
	fetch(url,{
    method:'POST',
    headers:{
        'Content-Type':'application/json',
        'X-CSRFToken':csrftoken,
    },
    body:JSON.stringify({'reciver_id':reciver_id})
    })
    .then((response)=>{
    response.json().then((data) => {
        console.log(data)
        chatcontext = ''
        for (i=0;i<data.messages.length;i++){
            if (data.messages[i].sender == reciver_id){
                chatcontext += "<div class='container darker'><img src='"+ data.users.reciver.image +"' alt='Avatar' class='right' style='width:100%;'><h3>"+ data.users.reciver.username +"</h3><p>"+data.messages[i].text+"</p><span class='time-left'>"+data.messages[i].time+"</span></div>"
            }
            else{
                chatcontext += "<div class='container'><img src='"+ data.users.sender.image +"' alt='Avatar' style='width:100%;'><h3>"+ data.users.sender.username +"</h3><p>"+data.messages[i].text+"</p><span class='time-right'>"+data.messages[i].time+"</span></div>"
            }
        }
        console.log(chatcontext)
        document.getElementById('chat').innerHTML = chatcontext
       })
    })


}
function sendmessage(){
    message = document.getElementById('message').value
    console.log(message)
    url = '/sendmessage/'
	fetch(url,{
    method:'POST',
    headers:{
        'Content-Type':'application/json',
        'X-CSRFToken':csrftoken,
    },
    body:JSON.stringify({'reciver_id':reciv,'message':message})
    })
    .then((response)=>{
    response.json().then((data) => {
        console.log(data)
        chatcontext = "<div class='container'><img src='"+ data.data.sender.image +"' alt='Avatar' style='width:100%;'><h3>"+ data.data.sender.username +"</h3><p>"+data.data.text+"</p><span class='time-right'>"+data.data.time+"</span></div>"
        document.getElementById('chat').innerHTML += chatcontext
       })
    })
}
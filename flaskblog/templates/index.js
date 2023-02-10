
document.getElementById("submit").addEventListener('click',(e)=>{
    e.preventDefault();
    let text = String(document.getElementById('name').value);
    let password = String(document.getElementById('name').value);
    if((text=="" )||(password=="")){
        alert('Text and Password must be input');
    }else if ((text.length<5)||(password.length<5)){
        alert("Password must bigger than 5 digits")
    }else{
        alert('Login Successful!');
       location.href='index.html';
    }
})


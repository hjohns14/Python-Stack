var myForm = document.getElementById("myForm")

function getUsers(){

    fetch('http://localhost:5000/users')
        .then(res =>  res.json())
        .then(data => {
            var users = document.getElementById('users');
            for( let i = 0; i < data.length; i++){
                let row = document.createElement('tr');

                let name = document.createElement('td');
                name.innerHTML = data[i].user_name;
                row.appendChild(name);
                
                let email = document.createElement('td');
                email.innerHTML = data[i].email;
                row.appendChild(email);
                users.appendChild(row);
            }
        })

}
getUsers();

myForm.onsubmit = function(e){
    e.preventDefault()

    var form = new FormData(myForm)

    fetch("http://localhost:5000/create/user", {method: 'POST', body: form})
        .then( response => response.json() )
        .then( data => {
            console.log(data)
            var users = document.getElementById("users")
            let row = document.createElement("tr")
            let name = document.createElement("td")
            let email = document.createElement('td')
        
            name.innerHTML = data.user.user_name
            email.innerHTML = data.user['email']
            row.appendChild(name)
            row.appendChild(email)
            users.appendChild(row)
            myForm.reset()
        } )
        .catch(err => console.log(err))
    
    
    
}



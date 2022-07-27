var registerForm = document.getElementById("registerForm")
var loginForm = document.getElementById("loginForm")

registerForm.onsubmit = function(e){
    e.preventDefault()

    var form = new FormData(registerForm)

    fetch('http://localhost:5000/register', {method: 'POST', body: form})
    .then( response => response.json() )
    .then (data => {

        let errors = document.createElement("table")
        
        var isValid = true
        if (data.user_info.first_name.length < 3){
            isValid = false
            errors.innerHTML = `<tr><td><p class='text-danger my-0'>Username Must be 3 characters</p></td></tr>`
        }
        if (data.user_info.last_name.length < 3){
            isValid = false
            errors.innerHTML += `<tr><td><p class='text-danger my-0'>last name Must be 3 characters</p></td></tr>`
        }
        if (data.user_info.password.length < 5){
            isValid = false
            errors.innerHTML += `<tr><td><p class='text-danger my-0'>Password Must be 5 characters</p></td></tr>`
        }
        if (data.user_info.password != data.user_info.confirm_password){
            errors.innerHTML += `<tr><td><p class='text-danger my-0'>Passwords Must match</p></td></tr>`
            isValid = false
        }
        if (isValid){
            return
        }
        else{
            registerForm.appendChild(errors)
            
        }
        
        
    })
    .catch(err =>  console.log(err))



}
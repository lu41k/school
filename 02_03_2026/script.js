$(document).ready(function(){
    $("#add-user").on('submit', function(e){
        e.preventDefault();
        error_state = false;
        name  = ("#name").val().trim();
        email = ("#email").val().trim();
        password = ("#password").val().trim();
        if ($name === "" || $email === "" || password != $("#confirm-password").val().trim() || $password === ''){
            error_state = true
        } else {
            error_state = false
        }
        if not error_state{
            $.ajax({
                url: "/add-user",
                method: "POST",
                contentType: "application/json",
                data: JSON.stringify(
                {
                    name: name,
                    email: email,
                    password: password
                })
            })
        }
    })
})
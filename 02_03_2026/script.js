$(document).ready(function () {
    $("#add-user").on("submit", function (e) {
        e.preventDefault();

        var name = $("#name").val().trim();
        var email = $("#email").val().trim();
        var password = $("#password").val().trim();
        var confirmPassword = $("#confirm-password").val().trim();

        var errorState =
            name === "" ||
            email === "" ||
            password === "" ||
            password !== confirmPassword;

        if (!errorState) {
            $.ajax({
                url: "/add-user",
                method: "POST",
                contentType: "application/json",
                data: JSON.stringify({
                    name: name,
                    email: email,
                    password: password
                })
            });
        }
    });
});

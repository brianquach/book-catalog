/*
Copyright 2016 Brian Quach
Licensed under MIT (https://github.com/brianquach/udacity-nano-fullstack-catalog/blob/master/LICENSE)
*/
// Setup csrf protection for all form-less post ajax calls
var csrftoken = $('meta[name=csrf-token]').attr('content')
$.ajaxSetup({
    beforeSend: function(xhr, settings) {
        if (!/^(GET|HEAD|OPTIONS|TRACE)$/i.test(settings.type) && !this.crossDomain) {
            xhr.setRequestHeader("X-CSRFToken", csrftoken)
        }
    }
})

function googleOauthStart() {
    gapi.load(
        'auth2',
        function() {
            auth2 = gapi.auth2.init({
                client_id: catalogOauth.ClientID,
                scope: 'openid email'
            });
        }
    );
}

function signInCallback(authResult) {
    if (authResult['code']) {
        // Hide the sign-in button now that the user is authorized, for example:
        $('#signinButton').attr('style', 'display: none');

        $.ajax({
            type: 'POST',
            url: 'http://localhost:8000/login?state=' + catalogOauth.StateToken,
            contentType: 'application/octet-stream; charset=utf-8',
            success: function(result) {
                if (result['email']) {
                    document.location.reload(true);
                }
            },
            processData: false,
            data: authResult['code']
        });
    } else {
        alert('authorization denied by user.')
    }
}

function singOut() {
    $.ajax({
        type: 'GET',
        url: 'http://localhost:8000/logout',
        success: function() {
            document.location.reload(true);
        }
    });
}
function showAlert(message) {
    const alertBox = $(".alert-box")

    alertBox.fadeIn(function() {
        $(this).text(message)
    })

    const timeOut = 1500
    setTimeout(timeOut, alertBox.fadeOut())
}

function showLoader({ selector }) {
    const loader = !selector ? $(".alert-box") : $(selector) 

    loader.css("display", "flex").hide().fadeIn()
}

function closeLoader({ selector }) {
    const loader = !selector ? $(".alert-box") : $(selector) 
    loader.fadeOut()
}


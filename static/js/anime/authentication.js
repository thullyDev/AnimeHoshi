(function () {
	$(".auth-con span.close-btn, .user-action-btn, .anon-user-con").click(() => {
		$(`.form-con`).removeClass('active')
		$(`.form-con[data-type="signup"]`).addClass('active')
		showCloseEle(".auth-con", "fade")
	});
	
	$(".auth-link").click(function() {
		const thisEle = $(this)
		const closeEle = thisEle.data('type')
		const showEle = closeEle == "login" ? "signup" : "login"
		showCloseAuthEle(closeEle, showEle)
	});

	$(".submit-btn").click(function () {
		const thisEle = $(this)
	  	const type = thisEle.data("type")

	  	if (!["signup", "login", "forgot_password", "resend", "verify", "renew_password"].includes(type)) return

	    const data = getInputs(`.form-con.active .icon-input`)
	    let url = ""


	  	if ("signup" == type) {
	  		const { email, username, password, confirm } = data

	  		if (!isValidEmail(email)) {
	  			showAlert({ message: "email is invalid" })
	  			return
	  		} 

	  		if (password != confirm) {
	  			showAlert({ message: "password and confirm dont match" })
	  			return
	  		}

	  		if (password.length <= 10) {
	  			showAlert({ message: "password should be atleast 10 characters long" })
	  			return
	  		}
	  	}

	  	if (["login", "forgot_password", "resend"].includes(type)) {
	  		const { email } = data

	  		if (!isValidEmail(email)) {
	  			showAlert({ message: "email is invalid" })
	  			return
	  		} 
	  	}

	  	if ("renew_password" == type) {
	  		const { password, confirm } = data

	  		if (password != confirm) {
	  			showAlert({ message: "password and confirm dont match" })
	  			return
	  		}

	  		if (password.length <= 10) {
	  			showAlert({ message: "password should be atleast 10 characters long" })
	  			return
	  		}
	  	}


	$.ajax({
	    url: `/user/ajax/post/${type}/`,
	    type: 'POST',
	    data: {
	        csrfmiddlewaretoken: csrfToken,
	        data: JSON.stringify(data),
	    },
	    beforeSend: function() {
	    	showLoader()
	    },
	    success: function(response) {
	        const { message } = response
			showAlert({ message })
			closeLoader()
			
			if (["login", "renew_password", "verify"].includes(type)) window.location.reload()

			if (["signup", "forgot_password"].includes(type)) showCloseAuthEle(type, "verify")

	    },
	    error: function(error) {
	    	const { message } = error.responseJSON
			showAlert({ message })
			closeLoader()
	    }
	});
	});
})();

function showCloseAuthEle(closeEle, showEle) {
	$(`.form-con[data-type="${closeEle}"]`).removeClass('active')
	$(`.form-con[data-type="${showEle}"]`).addClass('active')
}
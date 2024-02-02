(function () {
	$(".auth-con span.close-btn, .user-action-btn, .anon-user-con").click(() => showCloseEle(".auth-con", "fade"));

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
			window.location.reload()
	    },
	    error: function(error) {
	    	const { message } = error.responseJSON
			showAlert({ message })
			closeLoader()
	    }
	});

	});
})();

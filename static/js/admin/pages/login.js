(function () { 
	$(".submit-btn").click(function() {
	  login()
	});
})();

function login() {
	const data = {}
	$(".icon-input").each(function() {
		const thisEle = $(this)
		const value = thisEle.val()
		const key = thisEle.data("key")

		if (!value || !["email", "password"].includes(key)) return

		data[key] = value
	})

	if (!Object.keys(data).length) return 

	$.ajax({
	    url: "/admin/ajax/post/login/",
	    type: 'POST',
	    data: {
	        csrfmiddlewaretoken: csrfToken,
	        data: JSON.stringify(data),
	    },
	    beforeSend: function() {
	    	// showLoader()
	    },
	    success: function(response) {
	        console.log(response);
	        const { message } = response
			// closeLoader()
			// showAlert(message)
	    },
	    error: function(error) {
	    	console.log(error.responseJSON)
			// closeLoader()
	    }
	});
}
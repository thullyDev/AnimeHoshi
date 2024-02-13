(function () { 
	$("#profile-image-inp").change(function() {
	  const file = this.files[0];
	  const thisEle = $(this)

	  const reader = new FileReader();
	  reader.onload = function(e) {
	  	const callback = () => {
		  	const image = `<img src="${res}" alt="${username}" class="profile-image">`
		    $(".profile-image").html(image)
	  	}
	  	const res = e.target.result
	    changeUserDetails("profile_image", res, callback)
	  }
	  reader.readAsDataURL(file);
	});
	  
	$("input.username-inp").change(() => changeUsername());
	$("button.username-inp").click(() => changeUsername());

})();


function changeUserDetails(type, value, callback = null) {
	$.ajax({
	    url: "/user/ajax/post/change_user_details/",
	    type: 'POST',
	    data: {
	    	type,
	    	value,
	        csrfmiddlewaretoken: csrfToken,
	    },
	    beforeSend: function() {
	    	showLoader()
	    },
	    success: (response) => {
	        const { message } = response
			showAlert({ message })
			if (callback) callback()
			closeLoader()
	    },
	    error: (error) => {
	    	const { message } = error.responseJSON
			showAlert({ message })
			closeLoader()
	    }
	});
}

function changeUsername() {
	const value = $("input.username-inp").val()
	changeUserDetails("username", value, () => {
		username = value
	})
}
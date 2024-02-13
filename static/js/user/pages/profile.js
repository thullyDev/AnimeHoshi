(function () { 
	$("#profile-image-inp").change(function() {
	  const file = this.files[0];
	  const thisEle = $(this)
	  
	  const reader = new FileReader();
	  reader.onload = function(e) {
	  	const res = e.target.result
	  	const image = `<img src="${res}" alt="${username}" class="profile-image">`
	    $(".profile-image").html(image)
	    thisEle.data("value", res)
	  }
	  
	  reader.readAsDataURL(file);
	});
})();


function changeUserDetails(type, value) {
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
			closeLoader()
	    },
	    error: (error) => {
	    	const { message } = error.responseJSON
			showAlert({ message })
			closeLoader()
	    }
	});

}
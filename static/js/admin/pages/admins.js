(function () { 
	$(".add-admin, .outter-add-admin-modal-con .close-btn").click(function() {
		const adminModal = $(".outter-add-admin-modal-con")
		const adminModalIsOpen = adminModal.data("open")

		!adminModalIsOpen ?
			adminModal.css("display", "flex").hide().fadeIn().data("open", true) :
			adminModal.fadeOut().data("open", false) 
	});

	$(".save-btn").click(function() {
		const data = getInput()
		const isValidate = validate(data)
		if(!isValidate) return

		console.log({data, isValidate})
		$.ajax({
		    url: "/admin/ajax/post/add_admin/",
		    type: 'POST',
		    data: {
		        csrfmiddlewaretoken: csrfToken,
		        save_data: JSON.stringify(data),
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
	});


	function getInput() {
	  const settingsInput = $(".outter-add-admin-modal-con .icon-input")
	  const data = {}

	  settingsInput.each((_, ele) => {
	    const thisEle = $(ele)
	    const name = thisEle.data("key")
	    const value = thisEle.val() 
	    data[name] = value
	  })

	  if( Object.keys(data).length < 4) return 

	  return data
	}

	function validate({ username, email, password, confirm }) {
		if (!username || !email || !password || !confirm) {
			showAlert({ message: `missing inputs`})
			return false
		}

		if (password != confirm) {
			showAlert({ message: `confirm and password are not the same`})

			return false
		}

		if (confirm.length < 8) {
			showAlert({ message: `password is too short, it should be atleast 8 characters long`})

			return false
		}

		return true
	}
})();


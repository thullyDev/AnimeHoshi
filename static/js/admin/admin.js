(function () { 
	$(".logout-btn").click(function() {
		$.ajax({
		    url: "/admin/ajax/get/logout/",
		    type: 'POST',
		    data: {
		        csrfmiddlewaretoken: csrfToken,
		    },
		    beforeSend: function() {
		    	showLoader()
		    },
		    success: (response) => {
		        const { message } = response
				showAlert({ message })
				closeLoader()
				window.location.replace("/admin/login")
		    },
		    error: (error) => {
		    	const { message } = error.responseJSON
				showAlert({ message })
				closeLoader()
		    }
		});
	})


	$(".actions-dropdown-btn").click(() => showCloseEle(".actions-dropdown-menu"));
})();

function getSettingsInput({ is_checkbox = false } = {}) {
  const settingsInput = $(".settings-input")
  const data = {}

  settingsInput.each((_, ele) => {
    const thisEle = $(ele)
    const name = thisEle.data("name")
    const value = is_checkbox ? thisEle.is(':checked') : thisEle.data("value").trim() || thisEle.val().trim()  

    data[name] = value
  })

  return data
}

function showCloseEle(showele_key) {
		console.log({ showele_key })
		const showEle = $(showele_key)
		const showEleIsOpen = showEle.data("open")

		!showEleIsOpen ?
			showEle.css("display", "flex").hide().fadeIn().data("open", true) :
			showEle.fadeOut().data("open", false) 
	}

function saveSettings({ data }) {
	const page = getPage()

	$.ajax({
	    url: "/admin/ajax/post/save/",
	    type: 'POST',
	    data: {
	        csrfmiddlewaretoken: csrfToken,
	        save_data: JSON.stringify(data),
	        save: getSaveType(page) || "admins",
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

function getSaveType(page) {
	const types = {
		"admins": "admins",
		"dasboard": "dasboard",
		"advance": "settings",
		"general": "values",
		"scripts": "scripts",
	}

	return types[page]
}


const saveBtn = $(".save-btn")
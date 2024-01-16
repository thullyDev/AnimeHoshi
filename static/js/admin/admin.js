// (function () { 
// 	$(".save-btn").click(function() {
// 	  saveSettings()
// 	});
// })();


function getSettingsInput() {
  const settingsInput = $(".settings-input")
  const data = {}

  settingsInput.each((_, ele) => {
    const thisEle = $(ele)
    const name = thisEle.data("name")
    const value = thisEle.val()

    data[name] = value
  })

  return data
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
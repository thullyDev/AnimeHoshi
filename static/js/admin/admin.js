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

function saveSettings({ data, successCallback, errorCallback }) {
	const page = getPage()

	$.ajax({
	    url: "/admin/ajax/post/save_data/",
	    type: 'POST',
	    data: {
	        csrfmiddlewaretoken: csrfToken,
	        save_data: JSON.stringify(data),
	        save: getSaveType(page) || "admins",
	    },
	    success: successCallback(),
	    error: errorCallback()
	});
}

function getSaveType(page) {
	const types = {
		"admins": "admins",
		"dasboard": "dasboard",
		"advance": "attributes",
		"general": "general",
		"scripts": "scripts",
	}

	return types[page]
}


const saveBtn = $(".save-btn")
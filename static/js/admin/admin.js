import { reloadPage, getPage } from '../resources/urlUtils.js';

(function () { 
	$(".save-btn").click(function() {
	  saveSettings()
	});
})();

function saveSettings() {
	const page = getPage()
	const saveData = {}

	$(".settings-input").each(function() {
		const thisEle = $(this)
		const value = thisEle.val()
		const name = thisEle.data("name")
		saveData[name] = value
	})

	$.ajax({
	    url: "/admin/ajax/post/save_data/",
	    type: 'POST',
	    data: {
	        csrfmiddlewaretoken: csrfToken,
	        save_data: JSON.stringify(saveData),
	        save: getSaveType(page),
	    },
	    success: function(response) {
	        console.log(response);
	    },
	    error: function(error) {
	        console.error('Error:', error);
	    }
	});
}

function getSaveType(page) {
	if (![ "admins", "advance", "general", "scripts" ].includes(page)) return null

	if (page == "advance") return "attributes"
	if (page == "general") return "values"
	if (page == "scripts") return "scripts"

	return "admins"
}
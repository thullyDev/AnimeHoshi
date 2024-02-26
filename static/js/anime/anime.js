(function () {
	$(".menu-btn").click(() => showCloseEle(".mobile-viewer-con", "slide"));
	$(".watch2gather-btn, .watch-room-modal-close-btn").click(() => showCloseEle(".watch-room-modal-con", "fade"));
	$(".create-watch-room-btn").click(() => createRoom())
	$(".search-btn").click(() => search())
	$(".search-input").change(() => search())
	$(".watch-room-input").keyup(function() {
		const thisEle = $(this)
		const limit = thisEle.data("limit")
		const value = $.trim(thisEle.val())
		const length = value.length
		$(".text-limit").text(`${length}/${limit}`)
	})
})();

function search() {
	const searchInp = $(".search-input")
	const value = searchInp.val()
	const type = searchInp.data("type")

	if (value) return 

	const url = type == "latino" ? "/latino/search/" : "/main/filter/"
	const query = `${url}?keywords=${encodeURIComponent(value)}`
	window.location.href = query 
}

function getRoomInputs() {
  const inputs = $(".watch-room-input")
  const data = {}

  inputs.each((_, ele) => {
    const thisEle = $(ele)
    const name = thisEle.data("name")
    const value = thisEle.is(':checked') || $.trim(thisEle.val())  

    data[name] = value
  })

  return data
}

function createRoom() {
	data = getRoomInputs()
	const { room_name } = data

	if (room_name.length <= 10) {
		showAlert({ message: "room name should be atleast 10 characters long" })
		return
	}

	data.csrfmiddlewaretoken = csrfToken

	$.ajax({
	    data,
	    url: "/user/ajax/post/make_watch_room/",
	    type: 'POST',
	    beforeSend: function() {
	    	showLoader()
	    },
	    success: (response) => {
        const { message, room_id } = response
				showAlert({ message })
				closeLoader()
				// window.location.replace(`/watch2gather/${room_id}`)
	    },
	    error: (error) => {
	    	const { message } = error.responseJSON
				showAlert({ message })
				closeLoader()
    	}	
	});

}
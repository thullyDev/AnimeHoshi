(function () {
	$(".watch-room-search").change(function () {
		const thisEle = $(this)
		const value = thisEle.val()


		if (!value) return 

		const url = "/watch_rooms/"
		const query = `${url}?keywords=${encodeURIComponent(value)}`

		window.location.href = query 
	})
})();

function get_rooms_views() {
	
}



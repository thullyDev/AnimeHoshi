(function () {
	const searchInp = $(".search-input")
	$(".menu-btn").click(() => showCloseEle(".mobile-viewer-con", "slide"));
	$(".search-btn").click(() => search())
	searchInp.change(() => search())

	function search() {
		const value = searchInp.val()
		const type = searchInp.data("type")

		if (value) return 

		const url = type == "latino" ? "/latino/search/" : "/main/filter/"
		const query = `${url}?keywords=${encodeURIComponent(originalString)}`
		window.location.href = query 
	}
})();

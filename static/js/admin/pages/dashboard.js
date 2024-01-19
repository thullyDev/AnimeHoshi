(function () {
	$(".table-search-btn").click(function() {
		searchTable(this)
	})
	const searchTableInput = $(".table-search")
	searchTableInput.change(function() {
		searchTable(this)
	})

	function searchTable(ele) {
		const type = $(ele).data("type")
		const value = $(`.table-search[data-type="${type}"]`).val()
		if (!value) return 
		const query = encodeURI(value)
    	window.location.replace(`/admin/dashboard/?${type}_keywords=${query}`);
	}
})();


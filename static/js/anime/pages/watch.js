(function () {
	$(".server-link-con").click(function() {
		const thisEle = $(this)
		const link = thisEle.data("link")
		loadPlayer(link)
	});
})();


function loadPlayer(link) {
	const iframeHtml = `<iframe src="${link}" data-src="${link}" frameborder="0" class="player"></iframe>`
	$(".iframe-con").html(iframeHtml)
}

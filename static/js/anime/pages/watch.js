(function () {
	$(".server-link-con").click(function() {
		const thisEle = $(this)
		const link = thisEle.data("link")
		loadPlayer(link)
	});

	$(".mobile-iframe-toggle-btn, .iframe-toggle-btn").click(() => showCloseEle(".inner-chat-frame-con", "slide"));

	$(".code-inp-submit-btn").click(function() {
		const thisEle = $(this)
		const codeInp = $(".code-inp")
		const code = codeInp.val()

		if(code == "") return 

		roomCode = code

		$('.chat-frame')[0]?.contentWindow.setupRoom();
	});
})();

function openCloseRoomCodeModal () {
	showCloseEle(".code-modal-con", "fade")
}

function loadPlayer(link) {
	const iframeHtml = `<iframe src="${link}" data-src="${link}" frameborder="0" class="player"></iframe>`
	$(".iframe-con").html(iframeHtml)
}

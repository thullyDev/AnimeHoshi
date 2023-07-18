$(() => {
  const get_landing_data = () => {
    const page_loader_wrapper = $("#page_loader_wrapper");
	const search_inp = $("#search");
    const render_landing_data = (list_data) => {
		let search_links_html = `<span id="top_search_label_wrapper">Top searches: </span>`
		
		for (let i=0; i < list_data.length; i++) {
			if (i == 20) break
			const item = list_data[i]
			const search_anime_title = `${item.title.substring(0, 20)}...  ` 
			search_links_html += `
				<span class="top_search_link_wrapper">
					<a href="/watch/${item.slug}" id="top_search_link">
						${search_anime_title}
					</a>
				</span>
			`
		}
		
		document.getElementById("inner_top_search_links_wrapper").innerHTML = search_links_html
	};
		
	search_inp.change(function() {
	  const val = $(this).val()

	  if (val != "") window.location.replace(`/browsing?keyword=${encodeURI(val)}&type=&status=&season=&language=&sort=default&year=&genre=&page=`);
	});

    $.ajax({
      type: "post",
      url: "/get_landing_data",
      data: {
        csrfmiddlewaretoken: csrf_token,
      },
      success: (res) => {
        const res_data = JSON.parse(res);
		console.log(res_data)

        res_data.status_code == 200
          ? render_landing_data(res_data.popular_data)
          : console.log("something went wrong getting landing data...");

        page_loader_wrapper.css("display", "none");
      },
    });
  };

  get_landing_data();

  $("#mobile_nav_wrapper>#menu_icon_wrapper>#menu_btn").click((event) => {
    event.stopPropagation();
    wrapper_act("menu_nav_wrapper");
  });
});

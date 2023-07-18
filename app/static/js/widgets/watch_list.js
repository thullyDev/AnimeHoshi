const get_watch_list_data = () => {
  const render_watch_list = (list_data, is_user) => {
    const animes_wrapper = document.getElementById("watch_list_inner_wrapper");
    const watch_list_label_wrapper = document.getElementById(
      "watch_list_label_wrapper"
    );
    let animes_html = "";
    list_data.forEach((item) => {
		const sub_html = !item.ticks.sub ? '' : `<p class="anime_lang_type  sub_type">${item.ticks.sub}</p>`
		const dub_html = !item.ticks.dub ? '' : `<p class="anime_lang_type  dub_type">${item.ticks.dub}</p>`
		const eps_html = !item.ticks.eps ? '' : `<p class="anime_lang_eps">${item.ticks.eps}</p>`
		
      anime_html = `
      <div  class="anime_wrapper" data-gga="true" data-slug="${item.slug}">
        <a href="/watch/${item.slug}">
            <div class="anime_cover_wrapper">
                <div class="anime_img_details_cover_wrapper">
                    <div class="anime_img_cover_wrapper">
                        <img src="${
                          item.image_url
                        }" alt="anime_img_cover" class="anime_img_cover">
                    </div>
                    <div class="anime_details_cover_wrapper">
                        <div class="anime_types_wrapper">
                            <div class="anime_types_eps_wrapper">
							    ${sub_html}
							    ${dub_html}
                            </div>
                            <p class="anime_watch_type">
                              ${item.type}${eps_html}
                            </p>
                        </div>
                    </div>
                </div>
                <div class="anime_name_cover">
                  ${item.title.substring(0, 20)}...
                </div>
            </div>
        </a>
        <div class="anime_info_wrapper" >
          <div class="anime_info_loader_wrapper">
            <div class="loader_two_wrapper">
              <div class="loader_two"></div>
            </div>
          </div>
        </div>
      </div>
      `;
      animes_html += anime_html;

    });

	animes_wrapper.innerHTML = animes_html;
    watch_list_label_wrapper.textContent =
      is_user == true ? "Watch list animes" : "Popular animes";
  };
  $.ajax({
    type: "post",
    url: "/get_watch_list_data",
    data: {
      csrfmiddlewaretoken: csrf_token,
    },
    success: (res) => {
      const res_data = JSON.parse(res);

      res_data.status_code == 200
        ? render_watch_list(res_data.watch_list_data, res_data.is_user)
        : console.log("something went wrong getting watch list data...");
    },
  });
};

get_watch_list_data();

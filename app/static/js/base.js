let view_port = "";
const fade_speed = 250;

const get_anime_info = async (slug, is_for_gogoanime) => {
  if (is_for_gogoanime) {
    const api_url = `https://godsapi.onrender.com/anime/1/${slug}`;
    const response = await fetch(api_url);
    const res_data = await response.json();
    let genres_text = "";

    for (let i = 0; i < res_data.genres.length; i++) {
      const genre = res_data.genres[i];
      if (i == 0) genres_text += `${genre}`;
      else genres_text += `, ${genre}`;
    }

    const data = {
      title: res_data.animeTitle,
      genres: genres_text,
      other_names: res_data.otherNames,
      release_date: res_data.releasedDate,
      status: res_data.status,
      synopsis: res_data.synopsis,
      total_episodes: res_data.totalEpisodes,
      type: res_data.type,
    };

    return data;
  }
};

const add_to_list = async (slug, list) => {
  const url = `/add_to_list/${list}/${slug}`;
  const response = await fetch(url);
  const raw_res_data = await response.json();
  const res_data = JSON.parse(raw_res_data.replace(/'/g, '"'));
  
  if (res_data.status_code == 503) render_authentication("login")
  if (res_data.status_code == 200) show_alert(res_data.message);
};

$(window).click(function () {
  switch (page) {
    case "watch":
      act_wrapper("#anime_sub_dub_btns_wrapper");
      act_wrapper("#anime_eps_btns_wrapper");
      break;
    case "browsing":
      act_wrapper("#genre_inner_filter_item_wrapper");
      act_wrapper("#type_inner_filter_item_wrapper");
      act_wrapper("#season_inner_filter_item_wrapper");
      act_wrapper("#year_inner_filter_item_wrapper");
      act_wrapper("#status_inner_filter_item_wrapper");
      act_wrapper("#language_inner_filter_item_wrapper");
      break;
    case "landing":
      act_wrapper("#menu_nav_wrapper");
      break;
  }

  // act_wrapper("#menu");
});

const act_wrapper = (wrapper_id) => {
  const wrapper = $(wrapper_id);
  const open = wrapper.data("open");

  if (open == true) wrapper.fadeOut(() => wrapper.data("open", false));
};

const get_view_port = () => {
  const display_viewer = $("#viewer").css("display");

  if (display_viewer == "none") view_port = "desktop";
  else view_port = "mobile";
};

const show_alert = (msg) => {
  const alert_box = $("#alert_box");
  alert_box.text(msg);

  alert_box.css("display", "flex");
  setTimeout(() => alert_box.fadeOut(), 5000);
};

const wrapper_act = (wrapper_id) => {
  const wrapper = $(`#${wrapper_id}`);
  const wrapper_apper = () => {
    wrapper.data("open", true);
    wrapper.slideDown(fade_speed);
  };

  const wrapper_disapear = () => {
    wrapper.data("open", false);
    wrapper.slideUp(fade_speed);
  };

  const is_wrapper_open = wrapper.data("open");

  if (!is_wrapper_open) wrapper_apper(wrapper_id);
  else wrapper_disapear(wrapper_id);
};

const get_trending_data = async () => {
  if (page == "alert") return null;
  const render_top_trending = (list_data) => {
    const chunk_size = 10;

    for (let i = 0; i < list_data.length; i += chunk_size) {
      let top_animes_html = "";
      const wrapper_id =
        i == 0
          ? "top_day_wrapper"
          : i == 10
          ? "top_week_wrapper"
          : "top_month_wrapper";
      const chunk = list_data.slice(i, i + chunk_size);

      let count = 1;
      chunk.forEach((item) => {
        let class_type = "";

        if (count == 1) class_type = " first_top_animes_item";
        else if (count == 2) class_type = " second_top_animes_item";
        else if (count == 3) class_type = " third_top_animes_item";
		
		let top_anime_html = ""
		
		if (count == 1) {
			 top_anime_html = `
			  <li class="top_animes_item${class_type}">
			  <div class="first_image_outter_wrapper">
				<img width="100px" src="${item.image_url}" alt="${
			  item.title
			}" class="top_anime_img first_image">
			  </div>
			  <div class="top_anime_wrapper first_text_wrapper" data-slug="${
				item.slug
			  }" data-gga="false">
			  <div class="top_anime_num_wrapper">
				${count}
			  </div>
			  <div class="top_anime_info_wrapper">
				  <div class="top_anime_name_wrapper">
				  <a href="/watch/${item.slug}" class="top_anime_link">
					${item.title.substring(0, 20)}...
				  </a>
				  </div>
				  <div class="top_anime_small_details_wrapper">
					  <div class="top_anime_views_wrapper">
						  <i class="fa fa-eye" aria-hidden="true"></i>
						  ${item.watched}
					  </div>
				  </div>
			  </div>
		  </div> 
		  </li>
	  `;
		} else {
			top_anime_html = `
			  <li class="top_animes_item${class_type}">
			  <div class="top_anime_wrapper" data-slug="${
				item.slug
			  }" data-gga="false">
			  <div class="top_anime_num_wrapper">
				${count}
			  </div>
			  <div class="top_anime_img_wrapper">
				  <img width="100px" src="${item.image_url}" alt="${
			  item.title
			}" class="top_anime_img">
			  </div>
			  <div class="top_anime_info_wrapper">
				  <div class="top_anime_name_wrapper">
				  <a href="/watch/${item.slug}" class="top_anime_link">
					${item.title.substring(0, 20)}...
				  </a>
				  </div>
				  <div class="top_anime_small_details_wrapper">
					  <div class="top_anime_views_wrapper">
						  <i class="fa fa-eye" aria-hidden="true"></i>
						  ${item.watched}
					  </div>
				  </div>
			  </div>
		  </div> 
		  </li>
	  `;
		}
        
        // const top_anime_html = `
          // <li class="top_animes_item${class_type}">
          // <div class="top_anime_wrapper" data-slug="${
            // item.slug
          // }" data-gga="false">
          // <div class="top_anime_num_wrapper">
            // ${count}
          // </div>
          // <div class="top_anime_img_wrapper">
              // <img width="100px" src="${item.image_url}" alt="${
          // item.title
        // }" class="top_anime_img">
          // </div>
          // <div class="top_anime_info_wrapper">
              // <div class="top_anime_name_wrapper">
              // <a href="/watch/${item.slug}" class="top_anime_link">
                // ${item.title.substring(0, 20)}...
              // </a>
              // </div>
              // <div class="top_anime_small_details_wrapper">
                  // <div class="top_anime_views_wrapper">
                      // <i class="fa fa-eye" aria-hidden="true"></i>
                      // ${item.watched}
                  // </div>
              // </div>
          // </div>
      // </div> 
      // </li>
  // `;
        top_animes_html += top_anime_html;
        count++;
      });

      const top_wrapper = document.getElementById(wrapper_id);
      top_wrapper.innerHTML = `
        <ul>
          ${top_animes_html}
        </ul>
    `;
    }
  };

  $.ajax({
    type: "post",
    url: "/get_trending_data",
    data: {
      csrfmiddlewaretoken: csrf_token,
    },
    success: (res) => {
      const res_data = JSON.parse(res);

      res_data.status_code == 200 && res_data.top_animes_enabled == true
        ? render_top_trending(res_data.trending_data)
        : console.log("something went wrong getting trending data...");

      const date_btns = $(".date_btns");
      date_btns.click(async function () {
        const this_ele = $(this);
        const toggle = this_ele.data("toggle");
        date_btns.removeClass("active_ele");
        this_ele.addClass("active_ele");

        $(`.top_wrapper`).removeClass("active_top_wrapper");
        $(`#top_${toggle}_wrapper`).addClass("active_top_wrapper");
      });
    },
  });
};

const show_popup = () => {
  if (is_popup_avl != true) return null;
  if (ad_cooldowned != true) return null;
  if (page_ads == "False") return null;
  if (is_vip == "True") return null;

  $(".outter_popup_ad_wrapper").fadeIn();
  ad_cooldowned = false;
};

if (is_popup_avl == true && page_ads == "True") {
  setInterval(function () {
    ad_cooldowned = true;
  }, 60000 * 10); // 10 minutes *after ten minutes ad_cooldowned resets
}

get_view_port();
if (page != "watch" && page != "landing" && page != "profile")
  get_trending_data();

$("#popup_close_btn").click(() => $(".outter_popup_ad_wrapper").fadeOut());

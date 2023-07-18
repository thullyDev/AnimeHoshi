$(() => {
  const page_loader_wrapper = $("#page_loader_wrapper");
  /* 
	const change_username = function (new_username) {
		  $.ajax({
			type: "post",
			url: "/change_user_details",
			data: {
			  csrfmiddlewaretoken: csrf_token,
			  type: "username",
			  user_input: new_username,
			},
			success: async (res) => {
			  const res_data = JSON.parse(res);
			  
			  if (res_data.status_code == 200) document.getElementById("username_label").textContent = res_data.data.username;
			  else show_alert(res_data.message)
			},
		  });
	}
	*/

  const chop_list = (list, chop_size) => {
    const values = Object.values(list);
    let list_final = [];
    let counter = 0;
    let portion = {};

    for (let key in list) {
      if (counter !== 0 && counter % chop_size === 0) {
        list_final.push(portion);
        portion = {};
      }
      portion[key] = values[counter];
      counter++;
    }
    list_final.push(portion);

    return list_final;
  };
  const delete_list_item = async (type, slug) => {
    const anime_loader = $(
      `.anime_loader[data-type="${type}"][data-slug="${slug}"]`
    );
    anime_loader.css("display", "flex");
    const url = encodeURI(`/delete_list_item/${type}/${slug}`);
    const res_data = await fetch(url);
    const data = await res_data.json();

    if (type == "watch") {
      delete watch_dict[slug];
      watch_list = chop_list(watch_dict, 18);
      render_list(type, watch_list[watch_current_page - 1], current_view_type);
    } else {
      delete likes_dict[slug];
      likes_list = chop_list(likes_dict, 18);
      const temp_data = likes_list[likes_current_page - 1];
      render_list(type, likes_list[likes_current_page - 1], current_view_type);
    }
    anime_loader.css("display", "none");
  };
  
  const render_list = (type, data, view_type) => {
    let list_html = "";
    current_view_type = view_type;
	
    switch (view_type) {
      case "all":
        for (const key in data) {
          const item = data[key];
          list_html += `
						<div class="other_anime_wrapper" data-slug="${
              item.animeId
            }" data-type="${type}">
							  <a href="/watch/${encodeURI(
                  item.animeTitle
                )}?gga=false" class="other_anime_link">
								<div class="other_item_image_wrapper">
								  <img src="${item.animeImg}" alt="${
            item.animeTitle
          } cover image" class="other_item_image" />
								</div>
								<div class="other_item_details_wrapper">
								  <div class="other_name_des_wrapper">
									<p class="other_item_name">${item.animeTitle.substring(0, 15)}...</p>
								  </div>
								</div>
							  </a>
							   <button data-slug="${
                   item.animeId
                 }" data-type="${type}" type="button" class="delete_btn" >
								<img src="https://thullydev.github.io/thullyDev/as2anime_static/main/static/images/trash.svg" width="20px" height="20px" alt="delete icon" class="delete_icon">
							  </button>
							  <div class="anime_loader" data-type="${type}" data-slug="${item.animeId}">
								  <div class="loader_two_wrapper">
								    <div class="loader_two"></div>
								  </div>
							  </div>
							</div>	
					`;
        }
        break;
      case "unwatched":
        for (const key in data) {
          const item = data[key];
          const watch_status = item.watch_status;

          if (watch_status == undefined) {
            list_html += `
							<div class="other_anime_wrapper" data-slug="${
                item.animeId
              }" data-type="${type}">
							  <a href="/watch/${encodeURI(
                  item.animeTitle
                )}?gga=false" class="other_anime_link">
								<div class="other_item_image_wrapper">
								  <img src="${item.animeImg}" alt="${
              item.animeTitle
            } cover image" class="other_item_image" />
								</div>
								<div class="other_item_details_wrapper">
								  <div class="other_name_des_wrapper">
									<p class="other_item_name">${item.animeTitle.substring(0, 15)}...</p>
								  </div>
								</div>
							  </a>
							   <button data-slug="${
                   item.animeId
                 }" data-type="${type}" type="button" class="delete_btn" >
								<img src="https://thullydev.github.io/thullyDev/as2anime_static/main/static/images/trash.svg" width="20px" height="20px" alt="delete icon" class="delete_icon">
							  </button>
							  <div class="anime_loader" data-type="${type}" data-slug="${item.animeId}">
								  <div class="loader_two_wrapper">
								    <div class="loader_two"></div>
								  </div>
							  </div>
							</div>	
						`;
          }
        }
        break;
      case "watched":
        for (const key in data) {
          const item = data[key];
          const watch_status = item.watch_status;			

          if (watch_status == "watched") {
            list_html += `
							<div class="other_anime_wrapper" data-slug="${
                item.animeId
              }" data-type="${type}">
							  <a href="/watch/${encodeURI(
                  item.animeTitle
                )}?gga=false" class="other_anime_link">
								<div class="other_item_image_wrapper">
								  <img src="${item.animeImg}" alt="${
              item.animeTitle
            } cover image" class="other_item_image" />
								</div>
								<div class="other_item_details_wrapper">
								  <div class="other_name_des_wrapper">
									<p class="other_item_name">${item.animeTitle.substring(0, 15)}...</p>
								  </div>
								</div>
							  </a>
							   <button data-slug="${
                   item.animeId
                 }" data-type="${type}" type="button" class="delete_btn" >
								<img src="https://thullydev.github.io/thullyDev/as2anime_static/main/static/images/trash.svg" width="20px" height="20px" alt="delete icon" class="delete_icon">
							  </button>
							  <div class="anime_loader" data-type="${type}" data-slug="${item.animeId}">
								  <div class="loader_two_wrapper">
								    <div class="loader_two"></div>
								  </div>
							  </div>
							</div>
						`;
          }
        }
        break;
      case "watching":
        for (const key in data) {
          const item = data[key];
          const watch_status = item.watch_status;

          if (watch_status == "watching") {
            list_html += `
							<div class="other_anime_wrapper" data-slug="${
                item.animeId
              }" data-type="${type}">
							  <a href="/watch/${encodeURI(
                  item.animeTitle
                )}?gga=false" class="other_anime_link">
								<div class="other_item_image_wrapper">
								  <img src="${item.animeImg}" alt="${
              item.animeTitle
            } cover image" class="other_item_image" />
								</div>
								<div class="other_item_details_wrapper">
								  <div class="other_name_des_wrapper">
									<p class="other_item_name">${item.animeTitle.substring(0, 15)}...</p>
								  </div>
								</div>
							  </a>
							   <button data-slug="${
                   item.animeId
                 }" data-type="${type}" type="button" class="delete_btn" >
								<img src="https://thullydev.github.io/thullyDev/as2anime_static/main/static/images/trash.svg" width="20px" height="20px" alt="delete icon" class="delete_icon">
							  </button>
							  <div class="anime_loader" data-type="${type}" data-slug="${item.animeId}">
								  <div class="loader_two_wrapper">
								    <div class="loader_two"></div>
								  </div>
							  </div>
							</div>
						`;
          }
        }
        break;
    }
    document.getElementById(
      `text_nav_view_label_wrapper`
    ).textContent = `${type} list`;
	
    if (list_html) {
      document.getElementById(`view_wrapper`).innerHTML = list_html;
    } else {
      document.getElementById(`view_wrapper`).innerHTML = `
				<div id="empty_list_wrapper">
					<div id="empty_list_image_wrapper">
						<img src="https://thullydev.github.io/thullyDev/as2anime_static/main/static/images/empty_list_image.png" width="20px" height="20px" alt="empty list alert image" class="empty_list_image">
					</div>
					<div id="empty_list_text_wrapper">Nothing yet...</div>
				</div>
			`;
    }
    $(".view_sort_wrapper>.view_btns_wrapper").removeClass("active_text_ele");
    $(
      `.view_sort_wrapper>.view_btns_wrapper[data-type="${view_type.toLowerCase()}"]`
    ).addClass("active_text_ele");

    if (type == "likes") {
      const veiw_toggle_btn = $(".veiw_toggle_btn");
      veiw_toggle_btn.data("type", "watch");
      veiw_toggle_btn.text("Watch");
    } else {
      const veiw_toggle_btn = $(".veiw_toggle_btn");
      veiw_toggle_btn.data("type", "likes");
      veiw_toggle_btn.text("Likes");
    }

    $(".delete_btn").click(function () {
      const this_ele = $(this);
      const type = this_ele.data("type");
      const slug = this_ele.data("slug");
      delete_list_item(type, slug);
    });
  };
  const get_profile_data = () => {
    $.ajax({
      type: "post",
      url: "/get_profile_data",
      data: {
        csrfmiddlewaretoken: csrf_token,
      },
      success: async (res) => {
        const res_data = JSON.parse(res);
        const render_profile_data = (data) => {
          profile_image_html =
            data.profile_image == "None"
              ? `<img src="${data.default_image}" alt="account image" id="profile_account_image">${vip_logo_html}`
              : `<img src="${data.profile_image}" alt="account image" id="profile_account_image">${vip_logo_html}`;
          document.getElementById("account_profile_image_wrapper").innerHTML =
            profile_image_html;
          document.getElementById("username_label").textContent = data.username;
          document.getElementById("email_label").textContent = data.email;
        };

        switch (res_data.status_code) {
          case 200:
            render_profile_data(res_data.data);
            const view_type = "all"; // TODO: get the default current_page_type from cookies
            const temp_watch_list = chop_list(res_data.data.watch_list, 18);
            const temp_likes_list = chop_list(res_data.data.likes_list, 18);
            current_page_type = "likes"; // TODO: get the default current_page_type from cookies
            current_page_type == "watch"
              ? render_list(current_page_type, temp_watch_list[0], view_type)
              : render_list(current_page_type, temp_likes_list[0], view_type);
            watch_list = temp_watch_list;
            likes_list = temp_likes_list;
            watch_dict = res_data.data.watch_list;
            likes_dict = res_data.data.likes_list;
            watch_pages = temp_likes_list.length;
            likes_pages = temp_likes_list.length;
            page_loader_wrapper.css("display", "none");
            break;
          case 403:
            delete_all_cookies();
            window.location.replace("/?login_redirect=true");
            break;
          default:
            show_alert(res_data.message);
        }
      },
    });
  };
  
  const search_list = (list, key_word, type) => {
	const filter_matches = (text, list) => {
		return list.filter((e) => e.includes(text.toLowerCase()))
	}
    let filtered_list = filter_matches(key_word, list);
    let temp_dict = {};

    for (let i = 0; i < filtered_list.length; i++) {
      const item = filtered_list[i];
      temp_dict[item] = type == "watch" ? watch_dict[item] : likes_dict[item];
    }

    if (!temp_dict.length) render_list(type, temp_dict, "all");
  };

  get_profile_data();

  $(".veiw_toggle_btn").click(function () {
    const this_ele = $(this);
    const type = this_ele.data("type");
    let list_html = "";
    current_page_type = type;
    const data = type == "likes" ? likes_list[0] : watch_list[0];

    for (const key in data) {
      const item = data[key];
      list_html += `
				<div class="other_anime_wrapper" data-slug="${
          item.animeId
        }" data-type="${type}">
				  <a href="/watch/${encodeURI(
            item.animeTitle
          )}?gga=false" class="other_anime_link">
					<div class="other_item_image_wrapper">
					  <img src="${item.animeImg}" alt="${
        item.animeTitle
      } cover image" class="other_item_image" />
					</div>
					<div class="other_item_details_wrapper">
					  <div class="other_name_des_wrapper">
						<p class="other_item_name">${item.animeTitle.substring(0, 20)}...</p>
					  </div>
					</div>
				  </a>
				   <button data-slug="${
             item.animeId
           }" data-type="${type}" type="button" class="delete_btn" >
					<img src="https://thullydev.github.io/thullyDev/as2anime_static/main/static/images/trash.svg" width="20px" height="20px" alt="delete icon" class="delete_icon">
				  </button>
				  <div class="anime_loader" data-type="${type}" data-slug="${item.animeId}">
					  <div class="loader_two_wrapper">
						<div class="loader_two"></div>
					  </div>
				  </div>
				</div>	
			`;
    }
    document.getElementById(
      `text_nav_view_label_wrapper`
    ).textContent = `${type} list`;
    document.getElementById(`view_wrapper`).innerHTML = list_html;
    $(".view_sort_wrapper>.view_btns_wrapper").removeClass("active_text_ele");
    $(`.view_sort_wrapper>.view_btns_wrapper[data-type="all"]`).addClass(
      "active_text_ele"
    );

    if (type == "likes") {
      this_ele.data("type", "watch");
      this_ele.text("watch");
    } else {
      this_ele.data("type", "likes");
      this_ele.text("likes");
    }
  });

  $(".view_sort_wrapper>.view_btns_wrapper").click(function () {
    const this_ele = $(this);
    const type = this_ele.data("type");
    const data = current_page_type == "likes" ? likes_list[0] : watch_list[0];
    render_list(current_page_type, data, type);
  });

  $("#list_search").change(function () {
    const this_ele = $(this);
    const key_word = this_ele.val();
    const list =
      current_page_type == "likes"
        ? Object.keys(likes_dict)
        : Object.keys(watch_dict);

    if (key_word != "") search_list(list, key_word, current_page_type);
  });

  $("#list_search_btn").click(function () {
    const key_word = $("#list_search").val();
    const list =
      current_page_type == "likes"
        ? Object.keys(likes_dict)
        : Object.keys(watch_dict);

    if (key_word != "") search_list(list, key_word, current_page_type);
  });

  $(".next_previous_btns").click(function () {
    const this_ele = $(this);
    const type = this_ele.data("type");

    if (current_page_type == "likes") {
      const current_page = likes_current_page;
      const num_of_items = likes_list.length;

      if (num_of_items <= 1) show_alert("this is the only page");
      else {
        if (type == "next") {
          const data = likes_list[current_page];

          render_list(current_page_type, data, current_view_type);

          if (num_of_items > current_page) likes_current_page++;
        } else {
          const data = likes_list[current_page - 1];

          render_list(current_page_type, data, current_view_type);

          if (1 != current_page) likes_current_page--;
        }
      }
    } else {
      let current_page = watch_current_page;
      const num_of_items = watch_list.length;

      if (num_of_items <= 1) show_alert("This is the only page");
      else {
        if (type == "next") {
          const data = watch_list[current_page];

          render_list(current_page_type, data, current_view_type);

          if (num_of_items > current_page) watch_current_page++;
        } else {
          const data = watch_list[current_page - 1];

          render_list(current_page_type, data, current_view_type);

          if (1 != current_page) watch_current_page--;
        }
      }
    }
  });
});

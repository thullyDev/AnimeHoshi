$(() => {
  const page_loader_wrapper = $("#page_loader_wrapper");
  const player_loader_wrapper = $("#player_loader_wrapper");
  let next_ready = true
  let episode_number = 1
  let default_server_id = null
  let default_type = null
  let current_column = null
  
  $('#player_iframe_wrapper, .server_btns').click(() => show_popup())
  
  const get_episode = (ep_num) => {
	  for (let i = 0; i < episode_list.length; i++) {
		  const item = episode_list[i]
		  
		  if (parseInt(item.episode_number) == ep_num) {
			  return item
		  }
	  }
	  
	  return null
  }
  
  const render_trending = (list_data) => {
    const trending_animes_list_wrapper = document.getElementById(
      "trending_animes_list_wrapper"
    );
    let trending_animes_html = "";

    list_data.forEach((item) => {
      trending_animes_html += `
        <div class="trending_animes_item">
          <a class="trending_anime_link_wrapper" href="/watch/${
            item.slug
          }">
            <div class="trending_anime_img_wrapper">
                <img width="100px" src="${item.image_url}" alt="${
        item.title
      }" class="trending_anime_img">
            </div>
            <div class="trending_anime_info_wrapper">
                <div class="trending_anime_name_wrapper">
                ${item.title.substring(0, 20)}
                </div>
                <div class="trending_other_anime_info_wrapper">
                  <div class="trending_anime_rating_wrapper">
                      ${item.type}
                  </div>
                  <div class="trending_anime_year_wrapper">
                      ${item.durataion}
                  </div>
                </div>
            </div>
            </a> 
        </div>
  `;
    });

    trending_animes_list_wrapper.innerHTML = `
        ${trending_animes_html}
    `;
  };

  const render_related = (list_data) => {
    const related_animes_list_wrapper = document.getElementById(
      "related_animes_list_wrapper"
    );
    let related_animes_html = "";

    list_data.forEach((item) => {
      related_animes_html += `
        <div class="related_animes_item">
          <a class="related_anime_link_wrapper" href="/watch/${item.slug}">
            <div class="related_anime_img_wrapper">
                <img width="100px" src="${item.image_url}" alt="${
        item.title
      }" class="related_anime_img">
            </div>
            <div class="related_anime_info_wrapper">
                <div class="related_anime_name_wrapper">
                ${item.title.substring(0, 15)}...
                </div>
            </div>
            </a> 
        </div>
  `;
    });

    related_animes_list_wrapper.innerHTML = `
        ${related_animes_html}
    `;
  };
  
  const render_episodes = () => {
	if (episode_list.length == 0) window.location.replace("/alert?message=The%20first%20episode%20hasn%27t%20not%20come%20out%20yet&sub_message=please%20wait%20for%20it%20to%20be%20air");

    const chunk_size = 100;
    let count = 1;
    let open_btn_html = "";
    let eps_column_html = "";
    let open_btns_html = "";

    for (let i = 0; i <= episode_list.length; i += chunk_size) {
      const chunk = episode_list.slice(i, i + chunk_size);

      const chunk_id =
        episode_list.length <= 100
          ? `${count}_${episode_list.length}`
          : `${count}_${count + chunk.length}`;

      if (count == 1)
        open_btn_html = `<button id="anime_eps_open_btn">${chunk_id.replace(
          "_",
          " - "
        )}</button>`;

      open_btns_html += `
        <div class="anime_eps_btn_wrapper">
          <button data-column="${chunk_id}" class="anime_eps_btn">
            ${chunk_id.replace("_", " - ")}
          </button>
        </div>
      `;

      let eps_btns_html = "";
      chunk.forEach((item) => {
        eps_btns_html += `<button data-episode-id="${item.episode_id}" data-episode-slug="${item.episode_slug}" data-episode="${item.episode_number}" id="${item.episode_number}" class="anime_ep_btn" data-type="episode" type="button">${item.episode_number}</button>`;
      });

      eps_column_html +=
        count == 1
          ? `<div id="${chunk_id}" class="eps_column_wrapper scroll_wrapper active_eps_column_wrapper">${eps_btns_html}</div>`
          : `<div id="${chunk_id}" class="eps_column_wrapper scroll_wrapper">${eps_btns_html}</div>`;

      if (count == 1) current_column = chunk_id;
      count += chunk_size;
    }

	document.getElementById("anime_eps_label_btns_wrapper").innerHTML =
      open_btn_html;
    document.getElementById("anime_eps_btns_wrapper").innerHTML =
      open_btns_html.replace("undefined", "");
    document.getElementById("anime_episodes_btns_wrapper").innerHTML =
      eps_column_html;
	  
	$(".next_prev_btn").click(function () {
		const this_ele = $(this)
		const type = this_ele.data("type") //? 1 = next and 2 = previous
		
		if (type == 1) {
			const play_episode = get_episode(episode_number + 1)
			
			if (!play_episode) {
				show_alert("no more episodes")
				return null
			}				
			
			load_episode(play_episode.episode_id, play_episode.episode_number)
			return null
		}
		
		
		if (type == 2) {
			const play_episode = get_episode(episode_number - 1)
			
			if (!play_episode) return null
			
			load_episode(play_episode.episode_id, play_episode.episode_number)
			return null
		}
	})

	  $(".anime_ep_btn").click(function() {
		  const this_ele = $(this)
		  const source = this_ele.data("src")
		  const ep_id = this_ele.data("episode-id")
		  const ep_num = this_ele.data("episode")
		  // const slug = this_ele.data("episode-slug")
		  
		  const temp_data = {
			  last_ep: ep_num,
			  default_server_id: default_server_id,
			  default_type: default_type,
		  }
		  data[anime_slug] = temp_data
		  set_cookie("history", JSON.stringify(data), 365)
		  
		  load_episode(ep_id, ep_num)
	  })
	  
    $(".anime_eps_btn").click(function () {
      const this_ele = $(this);
      const column_id = this_ele.data("column");

      column_id == current_column
        ? show_alert("already showing")
        : show_column(column_id);
    });
	  
    $("#anime_eps_open_btn").click(function(event) {
      event.stopPropagation();

      const anime_eps_btns_wrapper = $("#anime_eps_btns_wrapper");
      const open = anime_eps_btns_wrapper.data("open");

      open == false
        ? anime_eps_btns_wrapper.fadeIn(() =>
            anime_eps_btns_wrapper.data("open", true)
          )
        : anime_eps_btns_wrapper.fadeOut(() =>
            anime_eps_btns_wrapper.data("open", false)
          );
    });
	
	
    $("#anime_eps_nav_inp").on("keyup input", function () {
      const val = $(this).val();
      const eps_column_wrappers =
        document.getElementsByClassName("eps_column_wrapper");

      if (val != "") {
        const int_val = parseInt(val);

        for (let i = 0; i < eps_column_wrappers.length; i++) {
          const column_id = eps_column_wrappers[i].id;
          const small_int = parseInt(column_id.split("_")[0]);
          const large_int = parseInt(column_id.split("_")[1]);

          if (small_int <= int_val && large_int >= int_val)
            show_column(column_id, int_val);
        }
      } else {
        const anime_eps_btns = $(`.anime_ep_btn`);
        anime_eps_btns.removeClass("anime_ep_highlight_btn");
      }
    });
	
	
    const show_column = function(column_id, ep = null) {
      $(".eps_column_wrapper").removeClass("active_eps_column_wrapper");
      $(`#${column_id}`).addClass("active_eps_column_wrapper");
      current_column = column_id;
      $("#anime_eps_open_btn").text(column_id.replace("_", " - "))

      if (ep != null) {
        const anime_eps_btn = $(`.anime_ep_btn[data-episode="${ep}"]`);
        const anime_eps_btns = $(`.anime_ep_btn`);

        anime_eps_btns.removeClass("anime_ep_highlight_btn");
        anime_eps_btn.addClass("anime_ep_highlight_btn");
        document.getElementById(`${ep}`).scrollIntoView({
          behavior: "smooth",
          block: "nearest",
          inline: "start",
        });

        setTimeout(
          () => anime_eps_btn.removeClass("anime_ep_highlight_btn"),
          60000
        );
      }
    };
	  
	  next_episode = () => $(`.next_prev_btn[data-type="1"]`).click()
	  
	  const history = get_cookie("history")
	  const data = history ? JSON.parse(history) : JSON.parse("{}")
	  let anime_data = data[anime_slug]
	  if (!anime_data){
		  anime_data = {
			  last_ep: 1,
			  default_server_id: default_server_id,
			  default_type: default_type,
		  }
	  }
	  
	  const ep = anime_data.last_ep
	  ep ? $(`.anime_ep_btn[data-episode="${ep}"]`).click() : $(`.anime_ep_btn[data-episode="1"]`).click()
	  
  }
  
  const render_servers = async (episode_id, episode_number) => {
	  const uri = `https://godsapi.onrender.com/anime/3/servers/${episode_id}`
	  const response = await fetch(uri);
	  const response_data = await response.json();
	  const servers = response_data.data.servers

	  let sub_html = ""
	  for(let i = 0; i < servers.sub_servers.length; i++) {
		  const item = servers.sub_servers[i]

		  if (item.server_id == "4" || item.server_id == "1") {
			  sub_html += `
			  <button
				  data-src="/stream/${item.source_id}?title=${encodeURIComponent(anime_title)}&episode=${episode_number}&type=${item.type}&image=${anime_image_url}&mute=${mute}&auto_next=${auto_next}&autostart=${autostart}&auto_skip_intro=${auto_skip_intro}&auto_skip_outro=${auto_skip_outro}"
				  data-server-name="${item.server_name}"
				  data-server-id="${item.server_id}"
				  data-source-id="${item.source_id}"
				  data-type="${item.type}"
				  class="server_btns"
				>
				${item.server_name}
			  </button>
			  `
		  }
	  }
	  
	  let dub_html = ""
	  for(let i = 0; i < servers.dub_servers.length; i++) {
		  const item = servers.dub_servers[i]
		  
		  if (item.server_id == "4" || item.server_id == "1") {
			  dub_html += `
			  <button
				  data-src="/stream/${item.source_id}?title=${encodeURIComponent(anime_title)}&episode=${episode_number}&type=${item.type}&image=${anime_image_url}&mute=${mute}&auto_next=${auto_next}&autostart=${autostart}&auto_skip_intro=${auto_skip_intro}&auto_skip_outro=${auto_skip_outro}"
				  data-server-name="${item.server_name}"
				  data-server-id="${item.server_id}"
				  data-source-id="${item.source_id}"
				  data-type="${item.type}"
				  class="server_btns"
				>
				${item.server_name}
			  </button>
			  `
		  }
	  }
	  
	  $(".servers_btns_inner_wrapper[data-type='sub']").html(sub_html)
	  $(".servers_btns_inner_wrapper[data-type='dub']").html(dub_html)
	  
	  if (sub_html != "") $(".servers_btns_outter_wrapper[data-type='sub']").css("display", "flex")
	  if (dub_html != "") $(".servers_btns_outter_wrapper[data-type='dub']").css("display", "flex")
		  
	  const history = get_cookie("history")
	  const data = history ? JSON.parse(history) : JSON.parse("{}")
  
	  $(".server_btns").click(function() {
		  const this_ele = $(this)
		  const source = this_ele.data("src")
		  default_server_id = this_ele.data("server-id")
		  default_type = this_ele.data("type")
		  $(`.server_btns`).removeClass("active_ele")
		  $(`#episode_text`).text("episode " + episode_number)
		  this_ele.addClass("active_ele")
		  const temp_data = {
			  last_ep: episode_number,
			  default_server_id: default_server_id,
			  default_type: default_type,
		  }
		  data[anime_slug] = temp_data
		  set_cookie("history", JSON.stringify(data), 365)
		  
		  document.getElementById("player_iframe_wrapper").innerHTML = ` 
			<iframe
              src="${source}"
              scrolling="no"
              frameborder="0"
              id="player_iframe"
              allowfullscreen
              sandbox="allow-same-origin allow-scripts"
			></iframe>
		   `;
	  })
	  
	  const temp = data[anime_slug]
	  default_server_id = temp ? temp.default_server_id : null
	  default_type = temp ? temp.default_type : null
	  
	  if (!default_server_id) $(".server_btns:first-child").click()
	  else $(`.server_btns[data-server-id="${default_server_id}"][data-type="${default_type}"]`).click()

	  for(let i = 0; i < episode_number; i++) $(`.anime_ep_btn[data-episode="${i}"]`).addClass("inactive_ele").removeClass("active_ele")
	  
	  $(`.anime_ep_btn[data-episode="${episode_number}"]`).addClass("active_ele")
	  
	  document.getElementById(`${episode_number}`).scrollIntoView({
          behavior: "smooth",
          block: "nearest",
          inline: "start",
        });
  };
  
  const load_episode = async (ep_id, ep_num) => {
	  episode_number = parseInt(ep_num)

	  render_servers(ep_id, ep_num)
  }
  
    $("#more_synopsis").click(function () {
      const synopsis_text = $("#synopsis_text");
      const anime_synopsis_info_wrapper = $(".anime_synopsis_info_wrapper");
      const data_open = synopsis_text.data("open");

      const open_more_synopsis = () => {
        synopsis_text.data("open", true);
        $(this).text("less");
        synopsis_text.css({
          overflow: "visible",
          "white-space": "normal",
          "text-overflow": "clip",
        });
        anime_synopsis_info_wrapper.css("display", "block");
      };
      const close_more_synopsis = () => {
        synopsis_text.data("open", false);
        $(this).text("more");
        synopsis_text.css({
          overflow: "hidden",
          "white-space": "nowrap",
          "text-overflow": "ellipsis",
        });
        anime_synopsis_info_wrapper.css("display", "flex");
      };

      data_open != true ? open_more_synopsis() : close_more_synopsis();
    });

  const user_settings = get_cookie("user_settings")
  let data
  
  if (!user_settings) {
	 data = JSON.parse("{}")
  } else data = JSON.parse(user_settings)
  
  auto_next = data.auto_next == "False" || data.auto_next == "True" ? data.auto_next : "False"
  autostart = data.autostart == "False" || data.autostart == "True" ? data.autostart : "False"
  auto_skip_intro = data.auto_skip_intro == "False" || data.auto_skip_intro == "True" ? data.auto_skip_intro : "False"
  auto_skip_outro = data.auto_skip_outro == "False" || data.auto_skip_outro == "True" ? data.auto_skip_outro : "False"
  mute = data.mute == "False" || data.mute == "True" ? data.mute : "False"
  
  set_cookie("user_settings", JSON.stringify({
	  auto_next,
	  autostart,
	  auto_skip_intro,
	  auto_skip_outro,
	  mute,
  }), 365)
	  
  $.ajax({
    type: "post",
    url: "/get_watch_data",
    data: {
      csrfmiddlewaretoken: csrf_token,
      genres: JSON.stringify(genres),
    },
    success: async (res) => {
      const res_data = JSON.parse(res);
      const related_data = res_data.related_data;
      const trending_data = res_data.trending_data;
	  
	  render_episodes()
	  
      related_data.status_code == 200
        ? render_related(related_data.related_data)
        : console.log("something went wrong getting related data...");

      trending_data.status_code == 200
        ? render_trending(trending_data.current_top_airing_data)
        : console.log("something went wrong getting trending data...");

      page_loader_wrapper.css("display", "none");
    },
  });
  
  $(".radio_btn").click(function() {
	  const this_ele = $(this)
	  const is_checked = this_ele.is(":checked");
	  const id = this_ele.data("id");
	  
	  if (id == "mute" ||  
		  id == "auto_next" ||  
		  id == "autostart" ||  
		  id == "auto_skip_intro" ||  
		  id == "auto_skip_outro") {
			  const user_settings = get_cookie("user_settings")
			  let data
			  
			  if (!user_settings) {
				 data = JSON.parse("{}")
			  } else data = JSON.parse(user_settings)
			  
			  if(is_checked) {
				  switch(id) {
					  case "mute": 
						mute = "True"
					  break
					  case "auto_next": 
						auto_next = "True"
					  break
					  case "autostart": 
						autostart = "True"
					  break
					  case "auto_skip_intro": 
						auto_skip_intro = "True"
					  break
					  case "auto_skip_outro": 
						auto_skip_outro = "True"
					  break
				  }
			  } else {
				  switch(id) {
					  case "mute": 
						mute = "False"
					  break
					  case "auto_next": 
						auto_next = "False"
					  break
					  case "autostart": 
						autostart = "False"
					  break
					  case "auto_skip_intro": 
						auto_skip_intro = "False"
					  break
					  case "auto_skip_outro": 
						auto_skip_outro = "False"
					  break
				  }
			  }
			  
			  data.mute = mute
			  data.auto_next = auto_next
			  data.autostart = autostart
			  data.auto_skip_intro = auto_skip_intro
			  data.auto_skip_outro = auto_skip_outro
			  
			  $(`.anime_ep_btn[data-episode="${episode_number}"]`).click()
			  set_cookie("user_settings", JSON.stringify(data), 365)
		  } else {
			  switch(id) {
				  case "likes_list": 
					add_to_list(anime_slug, 'likes')
				  break
				  case "watch_list": 
					add_to_list(anime_slug, 'watch')
				  break
			  }
			  
		  }
  })
});

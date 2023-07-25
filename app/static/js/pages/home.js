const next_slider = () => {
  const slider = $("#slider_list_wrapper");
  const slider_children = slider.children();
  const first_slider = slider_children.first();
  const current_slider = $(".active_slider_item");
  const next_slider = current_slider.next();

  if (next_slider.length != 0) {
    current_slider.fadeOut(fade_speed, () => {
      current_slider.removeClass("active_slider_item");
      next_slider.addClass("active_slider_item");

      $(".active_slider_item").fadeIn(fade_speed);
    });
  } else {
    current_slider.fadeOut(fade_speed, () => {
      current_slider.removeClass("active_slider_item");
      first_slider.addClass("active_slider_item");
      $(".active_slider_item").fadeIn(fade_speed);
    });
  }
};

const prev_slider = () => {
  const slider = $("#slider_list_wrapper");
  const last_slider = slider.children().last();
  const current_slider = $(".active_slider_item");
  const prev_slider = current_slider.prev();

  if (prev_slider.length) {
    current_slider.fadeOut(fade_speed, () => {
      current_slider.removeClass("active_slider_item");
      prev_slider.addClass("active_slider_item");

      $(".active_slider_item").fadeIn(fade_speed);
    });
  } else {
    current_slider.fadeOut(fade_speed, () => {
      current_slider.removeClass("active_slider_item");
      last_slider.addClass("active_slider_item");

      $(".active_slider_item").fadeIn(fade_speed);
    });
  }
};

const get_home_data = () => {
  const render_slider = (data) => {
    let animes_html = ""
    for(let i = 0; i < data.length; i ++) {
      const item = data[i]

      animes_html +=  `
        <li class="slide_item" data-anime="${item.slug}">
          <div class="slide_wrapper">
            <div class="slide_poster_wrapper">
              <img src="${item.image_url}" alt="${item.title}" class="slide_poster">
            </div>
            <div class="slide_info_wrapper">
              <div class="inner_info_wrapper">
                <div class="des_wrapper">
                  <p>${item.description}</p>
                </div>
                <div class="title_wrapper">
                  <p>${item.title}</p>
                </div>
                <div class="watch_link_wrapper">
                  <a href="/watch/spn/${item.slug}" class="watch_link">
                    watch
                  </a>
                </div>
              </div>
            </div>
          </div>
        </li>
      `
    }

    $(`#slider`).html(animes_html)
  };

  const render_animes = (data, wrapper) => {
    let animes_html = ""
    for(let i = 0; i < data.length; i ++) {
      const item = data[i]
      const title = item.title.length > 30 ? `${item.title.substring(0, 30)}...` : item.title
      animes_html +=  `
      <div class="anime_wrapper" data-slug="${item.title}">
        <a href="/watch/eng/${item.slug}" class="anime_watch_link">
          <div class="inner_anime_wrapper">
            <div class="anime_cover_wrapper">
              <img src="${item.image_url}" alt="${item.title}" class="anime_cover">
            </div>
            <div class="anime_title_wrapper">
              <p class="anime_title">
                ${title}
              </p>
            </div>
          </div>
        </a>
      </div>
      `
    }

    $(`.inner_animes_wrapper[data-wrapper="${wrapper}"]`).html(animes_html)
  };

  $.ajax({
    type: "post",
    url: "/ajax/get_home_data",
    data: {
      csrfmiddlewaretoken: csrf_token,
    },
    beforeSend: () => {
      page_loader_wrapper.addClass("active_loader")
    },
    success: (res) => {
      const res_data = JSON.parse(res);
      const slider_data = res_data.slider_data
      const recent_data = res_data.recent_data
      const recent_latino_data = res_data.recent_latino_data
      const specials_data = res_data.specials_data
      const movies_data = res_data.movies_data

      slider_data.status_code == 200 ? render_slider(slider_data.data) : console.log("some went wrong with data...")
      recent_data.status_code == 200 ? render_animes(recent_data.data, "recent_episodes") : console.log("some went wrong with data...")
      recent_latino_data.status_code == 200 ? render_animes(recent_latino_data.data, "recent_latino_episodes") : console.log("some went wrong with data...")
      specials_data.status_code == 200 ? render_animes(specials_data.data, "specials") : console.log("some went wrong with data...")
      movies_data.status_code == 200 ? render_animes(movies_data.data, "movies") : console.log("some went wrong with data...")

      page_loader_wrapper.removeClass("inactive_loader")
    },
  });
};

get_home_data();

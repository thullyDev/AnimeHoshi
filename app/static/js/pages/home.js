let page_toggle = "sub";
let page_source = "gogoanime";
let page_url = "https://as2vid.co.in/recent-release?type=1";
let page_number = 1;
let second_half_open = false;

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

const render_recent = (list_data, source) => {
  second_half_open = false;
  const first_animes_wrapper = document.getElementById(
    "first_half_animes_wrapper"
  );
  const second_animes_wrapper = document.getElementById(
    "second_half_animes_wrapper"
  );
  let first_animes_html = "";
  let second_animes_html = "";
  let anime_html = "";
  let count = 1;

  if (source == "jikan") {
    list_data.forEach((item) => {
      if (item.season != null && item.year != null) {
        anime_html = `
        <div  class="anime_wrapper" data-gga="false" data-slug="${item.slug}">
          <a href="/watch/${encodeURI(item.title)}?ep=${
          item.episode
        }&gga=false">
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
                                  <p class="anime_lang_type  ${item.subOrDub.toLowerCase()}_type">
                                    ${item.subOrDub}
                                  </p>
                                  <p class="anime_lang_eps">
                                    ${item.episode}
                                  </p>
                              </div>
                              <p class="anime_season">
                                ${item.season}  ${item.year}
                              </p>
                              <p class="anime_watch_type">
                                ${item.watch_type}
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
      } else {
        anime_html = `
        <div  class="anime_wrapper" data-gga="true" data-slug="${item.slug}">
          <a href="/watch/${encodeURI(item.title)}?ep=${
          item.episode
        }&gga=false">
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
                                  <p class="anime_lang_type  ${item.subOrDub.toLowerCase()}_type">
                                    ${item.subOrDub}
                                  </p>
                                  <p class="anime_lang_eps">
                                    ${item.episode}
                                  </p>
                              </div>
                              <p class="anime_watch_type">
                                ${item.watch_type}
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
      }

      if (count <= 10) first_animes_html += anime_html;
      else second_animes_html += anime_html;

      count++;
    });
  } else {
    list_data.forEach((item) => {
      anime_html = `
      <div  class="anime_wrapper" data-gga="true" data-slug="${item.slug}">
        <a href="/watch/${encodeURI(item.title)}?ep=${item.episode}&gga=false">
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
                                <p class="anime_lang_type  ${item.subOrDub.toLowerCase()}_type">
                                  ${item.subOrDub}
                                </p>
                                <p class="anime_lang_eps">
                                  ${item.episode}
                                </p>
                            </div>
                            <p class="anime_watch_type">
                              ${item.watch_type}
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

      if (count <= 10) first_animes_html += anime_html;
      else second_animes_html += anime_html;

      count++;
    });
  }

  first_animes_wrapper.style.display = "flex";
  second_animes_wrapper.style.display = "none";
  first_animes_wrapper.innerHTML = first_animes_html;
  second_animes_wrapper.innerHTML = second_animes_html;
};

const render_schedule = (list_data) => {
  const render_anime_schedule_wrapper = (list, schedule_wrapper_id) => {
    const schedule_wrapper = document.getElementById(schedule_wrapper_id);
    let schedule_anime_html = "";
    for (let i = 0; i < list.length; i++) {
      // TODO: convert the time and day to users local time
      const item = list[i];
      schedule_anime_html += `
      <div data-day="${item.day}" class="schedule_anime_wrapper">
          <div class="schedule_time_name_wrapper">
            <div class="schedule_anime_time_wrapper">${item.time}</div>
            <div class="schedule_anime_name_wrapper">${item.title}</div>
          </div>
          <div class="schedule_anime_episode_wrapper">
              <a href="watch/${encodeURI(item.title)}?ep=${
        item.episode
      }&gga=false" class="schedule_anime_link">
                <p>
                Episode ${item.episode}
                </p>
                <i class="fa fa-play" aria-hidden="true"></i>
              </a>
          </div>
      </div> 

      `;
    }

    schedule_wrapper.innerHTML = schedule_anime_html;
  };

  const chunk_size = 10;
  let count = 1;

  for (let i = 0; i < list_data.length; i += chunk_size) {
    const chunk = list_data.slice(i, i + chunk_size);

    if (count == 1)
      render_anime_schedule_wrapper(chunk, "first_schedule_wrapper");
    else render_anime_schedule_wrapper(chunk, "second_schedule_wrapper");

    count++;
  }
};

const get_home_data = () => {
  const page_loader_wrapper = $("#page_loader_wrapper");
  const render_slider = (list_data) => {
    const slider_inner_wrapper = document.getElementById(
      "slider_inner_wrapper"
    );
    let slider_html = ``;
    let count = 0;
    let slider_class_type = "";

    list_data.forEach((item) => {
      slider_class_type = count == 0 ? " active_slider_item" : "";
      const image_url =
        item.banner_image != null ? item.banner_image : item.cover_image;
      const slug = encodeURI(item.title.toLowerCase());
      const slider_anime_title =
        item.title.length >= 40
          ? item.title.substring(0, 40) + "..."
          : item.title;
      const sliders_html = `<li class="slider_item${slider_class_type}">
					<div class="slider_img_wrapper">
                      <img src="${image_url}" alt="${
        item.title
      }" class="slider_slider">
					</div>
					<div class="slider_info_wrapper">  
						<div class="inner_slider_info_wrapper">
							<div class="slider_title">${slider_anime_title}</div>
							<div class="slider_details_wrapper">
								<div class="slider_season"><i class="fas fa-play-circle"></i> ${item.season} ${
        item.year
      } Anime </div>
								<div class="slider_year"><i class="fas fa-calendar"></i>${item.year}</div>
								<div class="slider_type">${item.type}</div>
								<div class="slider_status">${item.status.toLowerCase()}</div>
								<div class="slider_des">${item.description.substring(0, 100)}...</div>
							</div>
							<div class="slider_watch_btns_wrapper">
								<a href="/watch/${encodeURI(item.title)}&gga=false" class="slider_watch_link">
								<i class="fas fa-play-circle"></i>Watch Now</a>
							</div>
						</div>
					</div>
				</li>`;
      slider_html += sliders_html;
      count++;
    });

    const slider_inner_html = slider_html;
    const temp = `<ul id="slider_list_wrapper">${slider_inner_html}</ul>`;
    slider_inner_wrapper.innerHTML = temp;
    const prev_btn = document.getElementById("prev_btn");
    const next_btn = document.getElementById("next_btn");
    prev_btn.addEventListener("click", () => prev_slider());
    next_btn.addEventListener("click", () => next_slider());
    setInterval(() => next_slider(), 7000);
  };

  const day = new Date().getDay();

  $.ajax({
    type: "post",
    url: "/get_home_data",
    data: {
      csrfmiddlewaretoken: csrf_token,
      day: day,
    },
    success: (res) => {
      const res_data = JSON.parse(res);
      const slider_data = res_data.slider_data;
      const recent_data = res_data.recent_data;
      const schedule_data = res_data.schedule_data;

      slider_data.status_code == 200 && slider_data.slider_enabled == true
        ? render_slider(slider_data.slider_data)
        : console.log(
            "something went wrong getting slider data or the slider has been disabled"
          );

      recent_data.status_code == 200
        ? render_recent(recent_data.recent_data)
        : console.log("something went wrong getting recent data...");

      schedule_data.status_code == 200 && schedule_data.schedule_enabled == true
        ? render_schedule(schedule_data.schedule_data)
        : console.log(
            "something went wrong getting schedule data or the schedule has been disabled"
          );

      page_loader_wrapper.css("display", "none");
    },
  });
};

const render_coming_data = async (coming_wrapper_id) => {
  const render_premiere = (list_data) => {
    let animes_list = [];
    let animes_html = "";
    const premieres_coming_wrapper = document.getElementById(
      "premieres_coming_wrapper"
    );

    const chunk_size = 20;
    for (let i = 0; i < list_data.length; i += chunk_size) {
      chunk = list_data.slice(i, 5);
      animes_list.push(chunk);
      break;
    }

    for (let i = 0; i < animes_list[0].length; i++) {
      const item = animes_list[0][i];
      const anime_img = `https://simkl.in/posters/${item.poster}_m.webp`;

      animes_html += `
        <div
          class="list_anime_wrapper"
          data-slug="${item.title}"
          data-gga="false"
        >
        <a href="/watch/${encodeURI(
          item.title
        )}?gga=false" class="list_anime_link">
          <div class="list_anime_img_wrapper">
            <img
              width="100px"
              src="${anime_img}"
              alt="${item.title}"
              class="list_anime_img"
            />
          </div>
          <div class="list_anime_info_wrapper">
            <div class="list_anime_name_wrapper">
              ${item.title.substring(0, 25)}...
            </div>
            <div class="list_anime_top_info_wrapper premiere_info_wrapper">
              <div class="list_anime_anime_type_wrapper">${
                item.anime_type
              }</div>
              <div class="list_anime_year_wrapper">${item.year}</div>
            </div>
          </div>
          </a>
        </div>
      `;
    }

    premieres_coming_wrapper.innerHTML = animes_html;
  };
  const render_upcoming = (list_data) => {
    let animes_html = "";
    const upcoming_coming_wrapper = document.getElementById(
      "upcoming_coming_wrapper"
    );

    for (let i = 0; i < list_data.length; i++) {
      const item = list_data[i];

      animes_html += `
        <div
          class="list_anime_wrapper"
          data-slug="${item.title}"
          data-gga="false"
        >
        <a href="/watch/${encodeURI(
          item.title
        )}?gga=false" class="list_anime_link">
          <div class="list_anime_img_wrapper">
            <img
              width="100px"
              src="${item.images.jpg.large_image_url}"k
              alt="${item.title}"
              class="list_anime_img"
            />
          </div>
          <div class="list_anime_info_wrapper">
            <div class="list_anime_name_wrapper">
              ${item.title}
            </div>
            <div class="list_anime_top_info_wrapper">
              <div class="list_anime_anime_type_wrapper">${item.type}</div>
              <div class="list_anime_source_wrapper">${item.source}</div>
            </div>
            <div class="list_anime_info_status_wrapper">
              <div class="list_anime_status_wrapper">${item.status}</div>
            </div>
          </div>
          </a>
        </div>
      `;
    }

    upcoming_coming_wrapper.innerHTML = animes_html;
  };
  const render_complete = (list_data) => {
    let animes_html = "";
    const complete_coming_wrapper = document.getElementById(
      "complete_coming_wrapper"
    );

    for (let i = 0; i < list_data.length; i++) {
      const item = list_data[i];
      const studio_name = item.studios[0].name;

      animes_html += `
        <div
          class="list_anime_wrapper"
          data-slug="${item.title}"
          data-gga="false"
        >
        <a href="/watch/${encodeURI(
          item.title
        )}?gga=false" class="list_anime_link">
          <div class="list_anime_img_wrapper">
            <img
              width="100px"
              src="${item.images.jpg.large_image_url}"k
              alt="${item.title}"
              class="list_anime_img"
            />
          </div>
          <div class="list_anime_info_wrapper">
            <div class="list_anime_name_wrapper">
              ${item.title}
            </div>
            <div class="list_anime_top_info_wrapper">
              <div class="list_anime_anime_type_wrapper">${item.type}</div>
              <div class="list_anime_studio_name_wrapper">${studio_name}</div>
              <div class="list_anime_source_wrapper">${item.source}</div>
            </div>
            <div class="list_anime_info_status_wrapper">
              <div class="list_anime_status_wrapper">${item.status}</div>
            </div>
          </div>
          </a>
        </div>
      `;
    }

    complete_coming_wrapper.innerHTML = animes_html;
  };

  const api_url = `/get_coming_data/${coming_wrapper_id}`;
  const response = await fetch(api_url);
  const response_data = await response.json();
  const res_data = JSON.parse(response_data);

  if (res_data.coming_section_enabled == true) {
    if (coming_wrapper_id == "premieres") render_premiere(res_data.data);
    else if (coming_wrapper_id == "complete")
      render_complete(res_data.data.data);
    else render_upcoming(res_data.data.data);
  }
};

const get_coming_data = async () => {
  render_coming_data("premieres");
  render_coming_data("upcoming");
  render_coming_data("complete");
};

const process_toggle_data = (res_data, source) => {
  let data = [];

  if (source == "gogoanime") {
    const raw_data = res_data;
    for (i = 0; i < raw_data.length; i++) {
      const item = raw_data[i];
      const temp = {
        slug: item.animeId,
        image_url: item.animeImg,
        title: item.animeTitle,
        episode: item.episodeNum,
        subOrDub: item.subOrDub,
        watch_type: "tv",
      };
      data.push(temp);
    }
  } else {
    const raw_data = res_data.data;

    for (i = 0; i < raw_data.length; i++) {
      const item = raw_data[i];
      const temp = {
        slug: item.title,
        image_url: item.images.jpg.large_image_url,
        title: item.title,
        episode: item.episodes,
        season: item.season,
        year: item.year,
        watch_type: item.type.toLowerCase(),
        subOrDub: "sub",
      };
      data.push(temp);
    }
  }

  return data;
};

get_home_data();
get_coming_data();

$(() => {
  const toggle_link = $(".toggle_link");
  const prev_toggle_btn = $(".prev_toggle_btn");
  const next_toggle_btn = $(".next_toggle_btn");
  const coming_toggle_btns = $(".coming_toggle_btns");
  const schedule_days = $(".schedule_days");
  const show_btn = $("#show_btn");

  toggle_link.click(async function () {
    const this_ele = $(this);
    const source = this_ele.data("source");
    const api_url = this_ele.data("url");
    const toggle = this_ele.data("toggle");
    const response = await fetch(api_url);
    const res_data = await response.json();
    const data = process_toggle_data(res_data, source);
    page_source = source;
    page_toggle = toggle;
    page_url = api_url;
    page_number = 1;

    render_recent(data, source);
  });

  prev_toggle_btn.click(async function () {
    if (second_half_open == false) {
      if (page_number > 1) {
        page_number--;
        const api_url = `${page_url}&page=${page_number}`;
        const response = await fetch(api_url);
        const res_data = await response.json();
        const data = process_toggle_data(res_data, page_source);
        render_recent(data, page_source, page_number);
        next_toggle_btn.click();
      }
    } else {
      second_half_open = false;
      document.getElementById("first_half_animes_wrapper").style.display =
        "flex";
      document.getElementById("second_half_animes_wrapper").style.display =
        "none";
    }
  });

  next_toggle_btn.click(async function () {
    if (second_half_open == true) {
      page_number++;
      const api_url = `${page_url}&page=${page_number}`;
      const response = await fetch(api_url);
      const res_data = await response.json();
      const data = process_toggle_data(res_data, page_source);
      render_recent(data, page_source);
    } else {
      second_half_open = true;
      document.getElementById("first_half_animes_wrapper").style.display =
        "none";
      document.getElementById("second_half_animes_wrapper").style.display =
        "flex";
    }
  });

  coming_toggle_btns.click(async function () {
    const this_ele = $(this);
    const wrapper_id = this_ele.data("wrapper");
    const coming_wrapper = $(`#${wrapper_id}_wrapper`);
    coming_wrapper.siblings().removeClass("active_section_wrapper");
    coming_wrapper.addClass("active_section_wrapper");
  });

  schedule_days.click(async function () {
    const this_ele = $(this);
    const day = this_ele.data("day");
    this_ele.siblings().removeClass("active_schedule_day");
    this_ele.addClass("active_schedule_day");
    $.ajax({
      type: "post",
      url: "/get_schedule_data",
      data: {
        csrfmiddlewaretoken: csrf_token,
        day: day,
      },
      beforeSend: () => {
        //todo: do something here i dont know what do
      },
      success: (res) => {
        const res_data = JSON.parse(res);
        const schedule_data = res_data.schedule_data;

        res_data.status_code == 200
          ? render_schedule(schedule_data)
          : console.log("something went wrong getting schedule data...");
      },
    });
  });

  show_btn.click(async function () {
    const this_ele = $(this);
    const wrapper_is_open = this_ele.data("open");
    const second_schedule_wrapper = $("#second_schedule_wrapper");

    if (!wrapper_is_open) {
      second_schedule_wrapper.css("display", "block");
      this_ele.data("open", true);
    } else {
      second_schedule_wrapper.css("display", "none");
      this_ele.data("open", false);
    }
  });
});

setInterval(() => {
  const current_tokyo_date_time = new Date().toLocaleString("en-US", {
    timeZone: "Asia/Tokyo",
  });
  const temp_list = current_tokyo_date_time.replace(",", "").split(" ");
  const tokyo_date_now = temp_list[0];
  const tokyo_time_now = temp_list[1];
  const date_time_string = ` - Asia/Tokyo: ${tokyo_date_now} ${tokyo_time_now}`;
  const inner_time_date_wrapper = document.getElementById(
    "inner_time_date_wrapper"
  );
  if (home_schedule == "True")
    inner_time_date_wrapper.textContent = date_time_string;
}, 1000);

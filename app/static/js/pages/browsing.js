$(() => {
  const page_loader_wrapper = $("#page_loader_wrapper");

  const get_browsing_data = (data) => {
    const render_browsing = (list_data) => {
      let animes_html = "";
      const anime_list = list_data.anime_list;
      const animes_length = anime_list.length;
      const style = animes_length < 10 ? "display: inline-block;" : "";
      pages = list_data.pages;

      for (let i = 0; i < animes_length; i++) {
        const item = anime_list[i];
        anime_types_html = "";
        anime_eps_html = "";

        const list_length = item.attributes.length;
        for (let j = 0; j < list_length; j++) {
          const attr = item.attributes[j];
          const temp = list_length - 1;

          j != list_length - 1
            ? (anime_types_html += `<p class="anime_type  ${attr.toLowerCase()}_type">${attr}</p>`)
            : (anime_eps_html += `<p class="anime_eps">${attr}</p>`);
        }

        const anime_html = `
          <div  class="anime_wrapper" data-gga="false" data-slug="${
            item.slug
          }" style="${style}">
            <a class="anime_link" href="/watch/${item.slug}">
                <div class="anime_cover_wrapper">
                    <div class="anime_img_details_cover_wrapper">
                        <div class="anime_img_cover_wrapper">
                            <img src="${item.image_url}" alt="${
          item.title
        }" class="anime_img_cover">
                        </div>
                        <div class="anime_details_cover_wrapper">
                          <div class="anime_types_wrapper">
                              <div class="anime_types_details_wrapper">
                                ${anime_types_html}
                              </div>
                              ${anime_eps_html}
                          </div>
                      </div>
                    </div>
                    <div class="anime_name_cover">
                      ${item.title.substring(0, 20)}...
                    </div>
                </div>
            </a>
          </div>
          `;

        animes_html += anime_html;
      }

      document.getElementById("inner_anime_browsing_wrapper").innerHTML =
        animes_html;

      document.getElementById(
        "page_label"
      ).textContent = `${current_page} of ${pages}`;
    };

    const render_top_airing = (list_data) => {
      let animes_html = "";
      const current_top_anime_wrapper = document.getElementById(
        "current_top_anime_wrapper"
      );

      for (let i = 0; i < list_data.length; i++) {
        const item = list_data[i];

        animes_html += `
          <div
            class="list_anime_wrapper"
            data-slug="${item.slug}"
            data-gga="false"
          >
          <a href="/watch/${item.slug}" class="list_anime_link">
            <div class="list_anime_img_wrapper">
              <img
                width="100px"
                src="${item.image_url}"
                alt="${item.title}"
                class="list_anime_img"
              />
            </div>
            <div class="list_anime_info_wrapper">
              <div class="list_anime_name_wrapper">
                ${item.title.substring(0, 25)}...
              </div>
              <div class="list_anime_info_status_wrapper">
                <div class="list_anime_status_wrapper">
                  <p class="list_eps">
                    ${item.episode} episodes
                  </p>
                </div>
              </div>
            </div>
            </a>
          </div>
          `;
      }

      current_top_anime_wrapper.innerHTML = animes_html;
    };

    $.ajax({
      type: "post",
      url: "/get_browsing_data",
      data: {
        csrfmiddlewaretoken: csrf_token,
        data: JSON.stringify(data),
      },
      beforeSend: () => {
        page_loader_wrapper.css("display", "flex");
      },
      success: (res) => {
        const res_data = JSON.parse(res);
        const browsing_data = res_data.browsing_data;
        // const current_top_airing_data = res_data.current_top_airing_data;

        browsing_data.status_code == 200
          ? render_browsing(browsing_data.browsing_data)
          : console.log("something went wrong getting trending data...");
        /*
        current_top_airing_data.status_code == 200
          ? render_top_airing(current_top_airing_data.current_top_airing_data)
          : console.log("something went wrong getting trending data...");
		*/

        page_loader_wrapper.css("display", "none");
      },
    });
  };

  const query_string =
    window.location.search != ""
      ? window.location.search
      : "?keyword=&type=&status=&season=&language=&sort=default&year=&genre=&page=";
  const url_params = new URLSearchParams(query_string);
  const keyword = url_params.get("keyword");
  const type = url_params.get("type");
  const status = url_params.get("status");
  const language = url_params.get("language");
  const sort = url_params.get("sort");
  const year = url_params.get("year");
  const season = url_params.get("season");
  const genre = url_params.get("genre");
  const page = url_params.get("page");

  get_browsing_data({
    keyword,
    type,
    status,
    language,
    sort,
    year,
    genre,
    page,
    season,
  });

  $(".filter_act_btn").click(function (event) {
    event.stopPropagation();
    const this_ele = $(this);
    const item = this_ele.data("item");
    const inner_wrapper = $(`#${item}_inner_filter_item_wrapper`);
    const open = inner_wrapper.data("open");

    $(`.inner_filter_item_wrapper`).fadeOut(function () {
      $(this).data("open", false);
    });

    open == false
      ? inner_wrapper.fadeIn(() => inner_wrapper.data("open", true))
      : inner_wrapper.fadeOut(() => inner_wrapper.data("open", false));
  });

  $(
    ".item_check_input, .check_inner_mark, .check_outter_mark, .outter_item_wrapper, .filter_item, .inner_filter_item_wrapper>ul"
  ).click(function (event) {
    event.stopPropagation();
  });

  // document.querySelector('input[name="gender"]:checked');

  $("#filter_btn").click(() => {
    let count = 0;
    const filter_input = document.getElementById("filter_inp");
    const checked_genre_inputs = $(".genre_check_input:checked");
    const checked_type_inputs = $(".type_check_input:checked");
    const checked_season_inputs = $(".seasons_check_input:checked");
    const checked_years_inputs = $(".years_check_input:checked");
    const checked_status_inputs = $(".status_check_input:checked");
    const checked_language_inputs = $(".language_check_input:checked");

    filter_keyword = filter_input.value;
    genre_values = "";
    type_values = "";
    season_values = "";
    years_values = "";
    status_values = "";
    language_values = "";

    count = 0;
    checked_genre_inputs.each(function () {
      const index = $(this).val();
      genre_values += count != 0 ? " " + index : index;
      count++;
    });

    count = 0;
    checked_type_inputs.each(function () {
      const index = $(this).val();
      type_values += count != 0 ? " " + index : index;
      count++;
    });

    count = 0;
    checked_years_inputs.each(function () {
      const index = $(this).val();
      years_values += count != 0 ? " " + index : index;
      count++;
    });

    count = 0;
    checked_season_inputs.each(function () {
      const index = $(this).val();
      season_values += count != 0 ? " " + index : index;
      count++;
    });

    count = 0;
    checked_language_inputs.each(function () {
      const index = $(this).val();
      season_values += count != 0 ? " " + index : index;
      count++;
    });

    count = 0;
    checked_status_inputs.each(function () {
      const index = $(this).val();
      status_values += count != 0 ? " " + index : index;
      count++;
    });

    const data = {
      keyword: filter_keyword,
      type: encodeURI(type_values),
      season: encodeURI(season_values),
      year: encodeURI(years_values),
      status: encodeURI(status_values),
      language: encodeURI(language_values),
      sort: "default",
      genre: encodeURI(genre_values),
      page: current_page,
    };
    get_browsing_data(data);
  });

  $(".page_act_btn").click(function () {
    const this_ele = $(this);
    const type = this_ele.data("type");

    if (type == 1) {
      if (current_page > 1) {
        const page = current_page--;
        const data = {
          keyword: keyword,
          type: encodeURI(type_values),
          season: encodeURI(season_values),
          year: encodeURI(years_values),
          status: encodeURI(status_values),
          language: encodeURI(language_values),
          sort: "default",
          genre: encodeURI(genre_values),
          page: page,
        };
        get_browsing_data(data);
      }
    } else if (type == 2) {
      const page = current_page++;
      if (pages > page) {
        const data = {
          keyword: keyword,
          type: encodeURI(type_values),
          season: encodeURI(season_values),
          year: encodeURI(years_values),
          status: encodeURI(status_values),
          language: encodeURI(language_values),
          sort: "default",
          genre: encodeURI(genre_values),
          page: page,
        };
        get_browsing_data(data);
      }
    }
  });

  $(".page_inp_btn").click(() => {
    const page = parseInt($("#page_inp").val());
    const data = {
      keyword: keyword,
      type: encodeURI(type_values),
      season: encodeURI(season_values),
      year: encodeURI(years_values),
      status: encodeURI(status_values),
      language: encodeURI(language_values),
      sort: "default",
      genre: encodeURI(genre_values),
      page: page,
    };
    get_browsing_data(data);
  });
});

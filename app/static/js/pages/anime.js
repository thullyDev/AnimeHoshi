$(() => {
  let is_form = false;
  let is_edit = false;
  let slider_id = "";
  const loader_wrapper = $(`#page_loader_wrapper`);

  $(".anime_slider_buttons").click(function () {
    const this_ele = $(this);
    const act = this_ele.data("act");
    const id = this_ele.data("id");

    if (act == "delete") {
      $.ajax({
        type: "post",
        url: "/save_site_settings",
        data: {
          csrfmiddlewaretoken: csrf_token,
          type: "delete_slider",
          data: JSON.stringify({ id }),
        },
        beforeSend: () => {
          loader_wrapper.css("display", "flex");
        },
        success: (res) => {
          const res_data = JSON.parse(res);

          if (res_data.status_code == 200) {
            $(`.anime_slider_item[data-id="${id}"]`).remove();
            slider_length--;
            if (slider_length == 0)
              $(`.table_wrapper`).html(
                `<div class="empty_anime_slider_wrapper">No Slider Animes</div>`
              );
          } else show_alert(res_data.message);
          loader_wrapper.css("display", "none");
        },
      });
    } else if (act == "edit") {
      is_edit = true;
      slider_id = this_ele.data("id");
      const title = this_ele.data("title");
      const year = this_ele.data("year");
      const season = this_ele.data("season");
      const country = this_ele.data("country");
      const duration = this_ele.data("duration");
      const description = this_ele.data("description");
      const status = this_ele.data("realise-date");
      const banner_image = this_ele.data("banner-image");
      const cover_image = this_ele.data("cover-image");
      const value_dict = {
        title,
        year,
        season,
        country,
        duration,
        description,
        status,
      };

      $(".banner_image").data("value", banner_image);
      $(".cover_image").data("value", cover_image);
      $(".banner_image").attr("src", banner_image);
      $(".cover_image").attr("src", cover_image);

      for (const [key, val] of Object.entries(value_dict)) {
        const input_ele = $(`.settings_input[data-value="${key}"]`);
        console.log({ key, val, input_ele });
        input_ele.data("value", key);
        input_ele.val(val);
      }

      const outter_anime_slider_wrapper = $(".outter_anime_slider_wrapper");
      const slider_form_wrapper = $("#slider_form_wrapper");
      const speed = 200;

      if (is_form == false) {
        outter_anime_slider_wrapper.fadeOut(speed, () =>
          slider_form_wrapper.fadeIn(speed)
        );
        is_form = true;
      } else {
        slider_form_wrapper.fadeOut(speed, () =>
          outter_anime_slider_wrapper.fadeIn(speed)
        );
        is_form = false;
      }
    }
  });

  $(".enable_disabel_radio").change(function () {
    const this_ele = $(this);
    const value = this_ele.data("value");

    $.ajax({
      type: "post",
      url: "/save_site_settings",
      data: {
        csrfmiddlewaretoken: csrf_token,
        type: "anime_slider_toggle",
        data: JSON.stringify({ value }),
      },
      beforeSend: () => {
        loader_wrapper.css("display", "flex");
      },
      success: (res) => {
        const res_data = JSON.parse(res);
        loader_wrapper.css("display", "none");
        show_alert(res_data.message);
      },
    });
  });

  $("#add_new").click(function () {
    const outter_anime_slider_wrapper = $(".outter_anime_slider_wrapper");
    const slider_form_wrapper = $("#slider_form_wrapper");
    const speed = 200;

    if (is_form == false) {
      outter_anime_slider_wrapper.fadeOut(speed, () =>
        slider_form_wrapper.fadeIn(speed)
      );
      is_form = true;
    } else {
      slider_form_wrapper.fadeOut(speed, () =>
        outter_anime_slider_wrapper.fadeIn(speed)
      );
      is_form = false;
    }
  });

  $("#close_auth_icon").click(function () {
    const outter_anime_slider_wrapper = $(".outter_anime_slider_wrapper");
    const slider_form_wrapper = $("#slider_form_wrapper");
    const speed = 200;

    if (is_form == true) {
      outter_anime_slider_wrapper.fadeOut(speed, () =>
        slider_form_wrapper.fadeIn(speed)
      );
      is_form = false;
    } else {
      slider_form_wrapper.fadeOut(speed, () =>
        outter_anime_slider_wrapper.fadeIn(speed)
      );
      is_form = true;
    }
  });

  $(".save_btn").click(() => {
    const banner_image = $(".banner_image").data("value");
    const cover_image = $(".cover_image").data("value");
    let data = {};

    $(".settings_input").each(function () {
      const this_ele = $(this);
      const value = this_ele.data("value");
      data[value] = this_ele.val();
    });

    if (
      Object.keys(data).length == 8 &&
      banner_image != "" &&
      cover_image != ""
    ) {
      data["banner_image"] = banner_image;
      data["cover_image"] = cover_image;
      data["id"] = slider_id;
      const type = is_edit == true ? "edit_slider" : "anime_slider";
      is_edit = false;
      $.ajax({
        type: "post",
        url: "/save_site_settings",
        data: {
          csrfmiddlewaretoken: csrf_token,
          type: type,
          data: JSON.stringify({ data }),
        },
        beforeSend: () => {
          loader_wrapper.css("display", "flex");
        },
        success: (res) => {
          const res_data = JSON.parse(res);

          if (res_data.status_code == 200) {
            $(".cover_image").attr(
              "src",
              "https://raw.githubusercontent.com/thullyDev/as2anime_static/main/static/images/default.jpg"
            );
            $(".banner_image").attr(
              "src",
              "https://raw.githubusercontent.com/thullyDev/as2anime_static/main/static/images/default.jpg"
            );
            $(".cover_image").data("value", "");
            $(".banner_image").data("value", "");

            $(".settings_input").each(function () {
              $(this).val("");
            });
          }

          loader_wrapper.css("display", "none");

          show_alert(res_data.message);
        },
      });
    } else show_alert("Missing Inputs...");
  });
});

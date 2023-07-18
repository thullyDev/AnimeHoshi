$(() => {
  const loader_wrapper = $(`#page_loader_wrapper`);
  const color_inp = $(".color_input");
  const preview_color = () => {
    color_inp.each(function () {
      const this_ele = $(this);
      const id = this_ele.data("id");
      const color = this_ele.val().replace("#", "");
      this_ele.val(color);

      $(`.color_preview[data-id="${id}"]`).css("backgroundColor", `#${color}`);
    });
  };

  preview_color();

  color_inp.on("keyup input", function () {
    const val = $(this).val();

    if (
      val.length == 3 ||
      val.length == 4 ||
      val.length == 6 ||
      val.length == 7 ||
      val.length == 8 ||
      val.length == 9 ||
      val.length == 10
    )
      preview_color();
  });

  $(".reset_colors").click(() => {
    const reset_colors = {
      primary_color: "181414",
      secondary_color: "dadada",
      secondary_highlight_color: "202020",
      third_color: "cb0000",
      accent_color: "969696",
      highlight_color: "252525",
      highlight_accent_color: "cb000070",
    };

    for (const [key, value] of Object.entries(reset_colors)) {
      $(`.color_input[data-id="${key}"]`).val(value);
    }
  });

  $(".save_btn").click(() => {
    const title = $('input[name="title"]').val();
    const description = $('input[name="description"]').val();
    const donate = $('input[name="donate"]').val();
    const facebook = $('input[name="facebook"]').val();
    const twitter = $('input[name="twitter"]').val();
    const discord = $('input[name="discord"]').val();
    const reddit = $('input[name="reddit"]').val();
    const instagram = $('input[name="instagram"]').val();
    const home_notice = $.trim($('textarea[data-id="home_notice"]').val());
    const watch_notice = $.trim($('textarea[data-id="watch_notice"]').val());
    const primary_color = $('input[data-id="primary_color"]').val();
    const secondary_color = $('input[data-id="secondary_color"]').val();
    const secondary_highlight_color = $(
      'input[data-id="secondary_highlight_color"]'
    ).val();
    const third_color = $('input[data-id="third_color"]').val();
    const accent_color = $('input[data-id="accent_color"]').val();
    const highlight_color = $('input[data-id="highlight_color"]').val();
    const highlight_accent_color = $(
      'input[data-id="highlight_accent_color"]'
    ).val();
    const as2server_name = $('input[data-id="as2server_name"]').val();
    let redirect_url = $.trim($('input[data-id="redirect_url"]').val());
    const contact_us = $.trim($('textarea[data-id="contact_us"]').val());
    const recaptcha_site_key = $.trim(
      $('input[data-id="recaptcha_site_key"]').val()
    );
    const recaptcha_secrete_key = $.trim(
      $('input[data-id="recaptcha_secrete_key"]').val()
    );
    const google_verification_code = $.trim(
      $('input[data-id="google_verification_code"]').val()
    );
    const bing_verification_code = $.trim(
      $('input[data-id="bing_verification_code"]').val()
    );
    const yandex_verification_code = $.trim(
      $('input[data-id="yandex_verification_code"]').val()
    );
    const backup_server_name = $('input[data-id="backup_server_name"]').val();
    const swipe_servers = $("input.radio_btn").is(":checked");

    if (redirect_url == "") redirect_url = "/";

    let site_data = {
      title,
      description,
      donate,
      facebook,
      twitter,
      discord,
      reddit,
      instagram,
      home_notice,
      watch_notice,
      primary_color,
      secondary_color,
      secondary_highlight_color,
      third_color,
      accent_color,
      highlight_color,
      highlight_accent_color,
      as2server_name,
      backup_server_name,
      redirect_url,
      contact_us,
      recaptcha_site_key,
      recaptcha_secrete_key,
      bing_verification_code,
      google_verification_code,
      yandex_verification_code,
      swipe_servers,
    };

    $(".image_preview_wrapper").each(function () {
      const this_ele = $(this);
      const id = this_ele.attr("for");
      site_data[id] = $(`.image_preview[data-id="${id}"]`).attr("src");
    });

    $.ajax({
      type: "post",
      url: "/save_site_settings",
      data: {
        csrfmiddlewaretoken: csrf_token,
        type: "general_settings",
        data: JSON.stringify({ site_data }),
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
});

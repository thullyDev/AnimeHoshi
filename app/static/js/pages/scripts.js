$(() => {
  const loader_wrapper = $(`#page_loader_wrapper`);
  $(".save_btn").click(() => {
    let site_scripts = {};

    $(".scripts_input").each(function () {
      const this_ele = $(this);
      const id = this_ele.data("id");
      const ad = this_ele.data("ad");

      if (ad == true) {
        const temp_fluid = $(`.radio_btn[data-id="${id}"]`).is(":checked");
        const temp_height = $(`.ad_height_input[data-id="${id}"]`).val();
        const height = temp_height == "" ? 0 : temp_height;
        const fluid = height == 0 ? true : false;
        const script = $.trim(this_ele.val());
        const values = {
          script,
          height,
          fluid,
        };
        site_scripts[id] = values;
      } else {
        const script = $.trim(this_ele.val());
        site_scripts[id] = script;
      }
    });

    $.ajax({
      type: "post",
      url: "/save_site_settings",
      data: {
        csrfmiddlewaretoken: csrf_token,
        type: "scripts",
        data: JSON.stringify({ site_scripts }),
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

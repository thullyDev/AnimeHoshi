const search_btn = document.getElementById("search_btn");
const apper_search_btn = $("#apper_search_btn");
const search_inp = $("#search");
const search_view_all_wrapper = $("#search_view_all_wrapper");
const search = document.getElementById("search");
const search_items_wrapper = document.getElementById("search_items_wrapper");
const search_list_wrapper = document.getElementById("search_list_wrapper");
const search_loader_wrapper = document.getElementById("search_loader_wrapper");
const cancel_btn = document.getElementById("cancel_btn");
const close_btn = document.getElementById("close_btn");

const render_search_results = async (val) => {
  cancel_btn.style.display = "inline";
  search_items_wrapper.style.display = "block";
  search_loader_wrapper.style.display = "flex";
  const response = await fetch(`https://godsapi.onrender.com/anime/2/results?keyword=${encodeURI(val)}`);
  const res_data = await response.json();
  const results = res_data.data.results
  
  let animes_html = `
    <div id="search_loader_wrapper">
        <div class="loader_two_wrapper">
            <div class="loader_two"></div>
        </div>
    </div>`;
  results.forEach((item) => {
    animes_html += `
        <li class="search_item_wrapper">
          <a href="/watch/${item.slug}" class="search_link">
            <div class="search_item_image_wrapper">
              <img src="${item.image_url}" alt="${item.title} cover image" class="search_item_image" />
            </div>
            <div class="search_item_details_wrapper">
              <div class="search_name_des_wrapper">
                <p class="search_item_name">${item.title}</p>
              </div>
              <div class="search_item_anime_info_wrapper">
                <ul>
                  <li class="search_item_status">
                  ${item.type}
                  </li>
                </ul>
              </div>
            </div>
          </a>
        </li>
    `;
  })

  search_loader_wrapper.style.display = "none";
  search_list_wrapper.innerHTML = animes_html;
};

search_inp.on("keyup input", () => {
  const val = search.value;

  if (val != "") render_search_results(val);
});

search_view_all_wrapper.click(function () {
  const this_ele = $(this);
  const open = this_ele.data("open");

  if (open === false) {
    search_list_wrapper.style.maxHeight = "515px";
    search_list_wrapper.style.overflowY = "auto";
    this_ele.text("view less");
    this_ele.data("open", true);
  } else {
    search_list_wrapper.style.maxHeight = "285px";
    search_list_wrapper.style.overflowY = "hidden";
    this_ele.text("view all");
    this_ele.data("open", false);
  }
});

search_btn.addEventListener("click", function () {
	const val = search.value;

	if (val != "") {
		window.location.replace(
		  `/browsing?keyword=${encodeURI(
			val
		  )}&type=&status=&season=&language=&sort=default&year=&genre=&page=`
		);
	}
});

cancel_btn.addEventListener("click", () => {
  search_items_wrapper.style.display = "none";
  cancel_btn.style.display = "none";
  search_inp.value = "";

  if (view_port == "mobile") disappear_search_wrapper();
});

close_btn.addEventListener("click", () => {
  search_items_wrapper.style.display = "none";
  cancel_btn.style.display = "none";
  search_inp.value = "";

  if (view_port == "mobile") disappear_search_wrapper();
});

apper_search_btn.click(function () {
  const is_open = $(this).data("open");

  if (!is_open) appear_search_wrapper();
  else disappear_search_wrapper();
});

const appear_search_wrapper = () => {
  $("#title_wrapper").fadeOut();
  $("#top_nav").fadeOut();
  apper_search_btn.fadeOut(() => {
    $("#search_wrapper").fadeIn();
    $("#close_btn").fadeIn();
  });
  apper_search_btn.data("open", true);
};

const disappear_search_wrapper = () => {
  $("#close_btn").fadeOut();
  $("#search_wrapper").fadeOut(() => {
    apper_search_btn.fadeIn();
    $("#title_wrapper").fadeIn();
    $("#top_nav").fadeIn();
  });
  apper_search_btn.data("open", false);
};

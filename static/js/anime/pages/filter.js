(function () {
  $(".apply-btn").click(function () {
    const data = getfilterInput()
    const url = buildUrl(data)
    window.location.href = url;
  });
})();

function buildUrl(params) {
    const query = new URLSearchParams(params).toString();
    return `/${type}/filter/${query ? `?${query}` : ''}`;
}

function getfilterInput() {
  const selectInputs = $(".filter-select")
  const data = {}

  selectInputs.each((_, ele) => {
    const thisEle = $(ele)
    const name = thisEle.data("type")
    let value = $.trim(thisEle.val())
    value = value == "None" ? "" : value

    data[name] = value
  })

  return data
}
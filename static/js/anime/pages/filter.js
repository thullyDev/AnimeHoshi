(function () {
	data = getfilterInput
})();


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
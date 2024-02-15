const print = (message) => console.log(message)

function showAlert({ message, timeOut = 3500 } = {}) { // 3.5 secs
  const alertBox = $(".alert-box");

  alertBox.text(message).fadeIn();

  setTimeout(() => {
    alertBox.fadeOut(() => {
      alertBox.text("");
    });
  }, timeOut);
}

function showLoader({ selector=".page-loader" } = {}) {
    const loader = $(selector) 
    loader.css("display", "flex").hide().fadeIn()
}

function removeEle(id) {
    $(`*[data-id="${id}"]`).fadeOut().remove()
}

function closeLoader({ selector=".page-loader" } = {}) {
    const loader = $(selector) 
    loader.fadeOut()
}

function redirect({ path=null } = {}) {
    const location = window.location
    !path ? location.reload() : location.replace(path)
}

function showCloseEle(showele_key, animate="fade") {
    const showEle = $(showele_key)
    const showEleIsOpen = showEle.data("open")
 
    if (animate == "slide") {
        !showEleIsOpen ?
          showEle.css("display", "flex").hide().slideDown().data("open", true) :
          showEle.slideUp().data("open", false) 
          return
    }
    !showEleIsOpen ?
      showEle.css("display", "flex").hide().fadeIn().data("open", true) :
      showEle.fadeOut().data("open", false) 
  }


function getInputs(selector) {
  const selectInputs = $(selector)
  const data = {}

  selectInputs.each((_, ele) => {
    const thisEle = $(ele)
    const name = thisEle.data("key")
    let value = $.trim(thisEle.val())
    value = value == "None" ? "" : value

    data[name] = value
  })

  return data
}

function isValidEmail(email) {
    const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    return emailRegex.test(email);
}

function addToList(slug, watchType) {
    $.ajax({
      url: "/user/ajax/post/add/list/",
      type: 'POST',
      data: {
          slug: slug,
          watch_type: watchType,
          csrfmiddlewaretoken: csrfToken,
      },
      beforeSend: function() {
        showLoader()
      },
      success: (response) => {
          const { message } = response
          showAlert({ message })
          closeLoader()
      },
      error: (error) => {
        const { message } = error.responseJSON
        showAlert({ message })
        closeLoader()
      }
  });
}

$(".add-to-list-btn").click(function() {
  const thisEle = $(this)
  const slug = thisEle.data("slug")
  const type = thisEle.data("type")
  addToList(slug, type)
});
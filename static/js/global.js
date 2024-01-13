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

function closeLoader({ selector=".page-loader" } = {}) {
    const loader = $(selector) 
    loader.fadeOut()
}

function redirect({ path=null } = {}) {
    const location = window.location
    !path ? location.reload() : location.replace(path)
}
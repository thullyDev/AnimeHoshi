const show_alert = (msg) => {
  const alert_box = $("#alert_box");
  alert_box.text(msg);

  alert_box.css("display", "flex");
  setTimeout(() => alert_box.fadeOut(), 5000);
};

const authenticate = async (data) => {
  await $.ajax({
    type: "post",
    url: "/admin_authenticate",
    data: {
      csrfmiddlewaretoken: csrf_token,
      data: JSON.stringify(data),
    },
    success: (res) => {
      const res_data = JSON.parse(res);
	  show_alert(res_data.message)
	  show_alert(res_data.message)
	  
	  res_data.status_code == 200 && window.location.replace("/as2_admin/dashboard");
    },
  });
};

$("#login_btn").click(function () {
	const email = $("#email").val()
	const password = $("#password").val()

	if (email != "" && password != "") authenticate({ email, password }) 
	else show_alert("Missings inputs...")
});


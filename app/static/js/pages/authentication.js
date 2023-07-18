let user_email = "";

const authenticate = async (auth, data) => {
  const auth_load_wrapper = $("#auth_loader_wrapper");
  let auth_response = {};

  await $.ajax({
    type: "post",
    url: "/authenticate",
    data: {
      csrfmiddlewaretoken: csrf_token,
      auth: auth,
      data: JSON.stringify(data),
    },
    beforeSend: () => {
      auth_load_wrapper.css("display", "flex");
    },
    success: (res) => {
      const res_data = JSON.parse(res);

      auth_response = res_data;
      auth_load_wrapper.css("display", "none");
    },
    error: function (jqXHR, textStatus, errorThrown) {
      if (jqXHR.status == 403) {
        show_alert("reload after logout...");
        window.location.reload();
      } else {
        show_alert("Unexpected error.");
      }
    },
  });

  return auth_response;
};

function set_cookie(name, value, days) {
  let expires = "";
  if (days) {
    const date = new Date();
    date.setTime(date.getTime() + days * 24 * 60 * 60 * 1000);
    expires = "; expires=" + date.toUTCString();
  }
  document.cookie = name + "=" + (value || "") + expires + "; path=/";
}

function get_cookie(name) {
  let nameEQ = name + "=";
  let ca = document.cookie.split(";");
  for (let i = 0; i < ca.length; i++) {
    let c = ca[i];
    while (c.charAt(0) == " ") c = c.substring(1, c.length);
    if (c.indexOf(nameEQ) == 0) return c.substring(nameEQ.length, c.length);
  }
  return null;
}

const set_user = async (data, msg) => {
  set_cookie("user_email", data.email, 365);
  set_cookie("temporary_id", data.temporary_id, 365);
  set_cookie("username", data.username, 365);
  show_alert(msg);
  $(`#outter_auth_wrapper`).fadeOut();
};

function delete_all_cookies() {
  const cookies = document.cookie.split(";");

  for (let i = 0; i < cookies.length; i++) {
    const cookie = cookies[i];
    const eqPos = cookie.indexOf("=");
    const name = eqPos > -1 ? cookie.substr(0, eqPos) : cookie;
    document.cookie = name + "=;expires=Fri, 21 Jun 2002 00:00:00 GMT";
  }
}

const logout = () => {
  delete_all_cookies();
  show_alert("User has logged out");
  window.location.reload();
};

const show_auth_wrapper = (wrapper_id) => {
  $(`.auth_block_wrapper`).css("display", "none");
  $(`#${wrapper_id}`).css("display", "flex");
};

const show_other_auth_wrapper = (wrapper_id) => {
  $(`#outter_auth_wrapper`).fadeOut();
  $("#outter_auth_wrapper").css("display", "flex");
  $(`#${wrapper_id}`).css("display", "flex");
  $(`#outter_auth_wrapper`).fadeIn();
};

const show_renew = (email) => {
  show_auth_wrapper("renew_password_wrapper");
  $("#renew_btn").click(async () => {
    const password = document.getElementById("renew_password").value;
    const confirm = document.getElementById("renew_confirm").value;

    const auth_response = await authenticate("renew", {
      password,
      confirm,
      email,
    });

    auth_response.status_code != 200
      ? show_alert(auth_response.message)
      : set_user(auth_response.data, auth_response.message);
  });
};

const show_verify = (data, auth_type) => {
  const email = data.email;
  user_email = email;
  show_auth_wrapper("verify_wrapper");
};

const render_authentication = (type) => {
  type == "login"
    ? show_other_auth_wrapper("login_wrapper")
    : show_other_auth_wrapper("signup_wrapper");

  $(".auth_btn").click(function () {
    const this_ele = $(this);
    const auth = this_ele.data("auth");
    const login = async () => {
      const email = document.getElementById("login_email").value;
      const password = document.getElementById("login_password").value;

      if (email == "" || password == "") {
        show_alert("Missing inputs...");
        return null;
      }

      const auth_response = await authenticate(auth, {
        email,
        password,
      });

      auth_response.status_code != 200
        ? show_alert(auth_response.message)
        : set_user(auth_response.data, auth_response.message);
    };
    const signup = async () => {
      const username = document.getElementById("username").value;
      const email = document.getElementById("email").value;
      const password = document.getElementById("password").value;
      const confirm = document.getElementById("confirm").value;

      if (recaptcha_valid === "True") {
        const token = grecaptcha.getResponse();

        if (token.length == 0) {
          show_alert("please verify you are humann!");
          return null;
        }

        if (username == "" || email == "" || password == "" || confirm == "") {
          show_alert("Missing inputs...");
          return null;
        }

        if (password != confirm) {
          show_alert("password and confirm do not match...");
          return null;
        }

        if (password < 8) {
          show_alert("atleast 8 characters for the password");
          return null;
        }

        const data = {
          username,
          email,
          password,
          confirm,
          token,
        };

        const auth_response = await authenticate(auth, data);

        auth_response.status_code != 200
          ? show_alert(auth_response.message)
          : show_verify(auth_response.data);
      } else {
        const token = null;

        if (username == "" || email == "" || password == "" || confirm == "") {
          show_alert("Missing inputs...");
          return null;
        }

        if (password != confirm) {
          show_alert("password and confirm do not match...");
          return null;
        }

        if (password < 8) {
          show_alert("atleast 8 characters for the password");
          return null;
        }

        const data = {
          username,
          email,
          password,
          confirm,
          token,
        };

        const auth_response = await authenticate(auth, data);

        auth_response.status_code != 200
          ? show_alert(auth_response.message)
          : show_verify(auth_response.data);
      }
    };

    auth == "login" ? login() : signup();
  });

  $("#verify_btn").click(() => {
    const verify = (email, code) => {
      const auth_type = "verify";
      $.ajax({
        type: "post",
        url: "/authenticate",
        data: {
          csrfmiddlewaretoken: csrf_token,
          auth: auth_type,
          data: JSON.stringify({
            email,
            code,
            auth_type,
          }),
        },
        success: (res) => {
          const res_data = JSON.parse(res);

          if (res_data.status_code == 200)
            res_data.data.auth == "signup"
              ? set_user(res_data.data, res_data.message)
              : show_renew(res_data.data.email);
          else show_alert(res_data.message);
        },
      });
    };
    const code = document.getElementById("verify_inp").value;
    const email = user_email;

    verify(email, code);
  });

  $("#recover_btn").click(() => {
    const forgot_password = (email, code) => {
      const auth_type = "forgot_password";
      $.ajax({
        type: "post",
        url: "/authenticate",
        data: {
          csrfmiddlewaretoken: csrf_token,
          auth: auth_type,
          data: JSON.stringify({
            email,
            auth_type,
          }),
        },
        success: (res) => {
          const res_data = JSON.parse(res);

          if (res_data.status_code == 200) show_verify(res_data.data);
          else show_alert(res_data.message);
        },
      });
    };
    const code = document.getElementById("verify_inp").value;
    const email = document.getElementById("verificaiton_email").textContent;
    forgot_password(email, code);
  });

  $("#forgot_link").click(() => show_auth_wrapper("forgot_wrapper"));
  $("#signup_link").click(() => show_auth_wrapper("signup_wrapper"));
  $("#login_link").click(() => show_auth_wrapper("login_wrapper"));
  $("#close_auth_btn").click(() => {
    $("#outter_auth_wrapper").fadeOut();
    $(".auth_block_wrapper").fadeOut();
  });
};

const check_authentication = () => {
  const user_email = get_cookie("user_email");
  return user_email == null ? false : true;
};

$(() => {
  $(".auth_btn_wrapper").click(function () {
    const this_ele = $(this);
    const type = this_ele.data("type");
    const outter_auth_wrapper = $(".outter_auth_wrapper");
    const is_auth = check_authentication();
    is_auth == false ? render_authentication(type) : logout();
  });
  const url_params = new URLSearchParams(window.location.search);
  const login_redirect = url_params.get("login_redirect");
  const is_auth = check_authentication();
  is_auth == false
    ? $("#menu_account_details_wrapper>.auth_btn_wrapper").html(
        'Login <img src="https://raw.githubusercontent.com/thullyDev/as2anime_static/main/static/images/login.svg" width="15px" height="15px" alt="" class="footer_socials">'
      )
    : $("#menu_account_details_wrapper>.auth_btn_wrapper").html(
        'Logout <img src="https://raw.githubusercontent.com/thullyDev/as2anime_static/main/static/images/login.svg" width="15px" height="15px" alt="" class="footer_socials">'
      );
  is_auth == false
    ? $("#mobile_nav_wrapper>.auth_btn_wrapper").html("Login")
    : $("#mobile_nav_wrapper>.auth_btn_wrapper").html("Logout");
  is_auth == false
    ? $("#mobile_nav_wrapper>.auth_btn_wrapper").html("Login")
    : $("#mobile_nav_wrapper>.auth_btn_wrapper").html("Logout");

  if (login_redirect != null || login_redirect == true)
    if (is_auth == false) render_authentication("login");
});

(function () {
})();
// room_id = data.room_id
// user_id = data.user_id
// display_name = data.display_name
// token = data.token
// message = data.message

const sendMsg = (data) => {
	const { room_id, user_id, display_name, message } = data 
}

const deleteMsg = () => { 
}

const editMsg = () => { 
}

const updateToken = (token) => setCookie("token", token, 1);
const deleteToken = () => deleteCookie("token");
const getToken = () => {
	return getCookie("token")
}

function sendToChatAjax(data, endpoint, action_type) {
	const actions = {
		send,
		edit,
		delete,
	}
    $.ajax({
      data,
      url: liveChatBase + endpoint,
      type: 'POST',
      success: (response) => {
      	const { data } = response
        const action = actions[action_type]
        action(data)
      },
      error: (error) => {
        const { message } = error.responseJSON
        showAlert({ message })
      }
  });
}
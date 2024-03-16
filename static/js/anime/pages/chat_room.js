(function () {
	$(".msg-box").click(function() {
		const thisEle = $(this)
		const message_id = thisEle.data("data-message-id")
		deleteMsg({ message_id: message_id })
	})

	// $(".send-msg-box").change(() => sendMsg())
	$(".send-msg-btn").click(() => sendMsg())

	setupRoom()
})();
const sendMsg = () => {
	const value = $(".send-msg-box").val()
	const data = {
		message: value,
	}

if (userName !== "None") {
    data.display_name = userName;
}

	sendToChatAjax(data, "/room/message/send", "send") 
}
function setupRoom() {
	getRoomCode()
	if (!roomCode) {
		console.log("no room code")
		return
	} 
  $.ajax({
	  url: liveChatBase + "/room/",
	  type: 'POST',
	  headers: {
	    'accept': 'application/json',
	    'Content-Type': 'application/json'
	  },
	  data: JSON.stringify({
	  	room_id: roomId,
	  	room_code: roomCode,
	  }),
    success: (response) => {
    	const { data } = response
    	const { messages } = data

    	for(let i = 0; i < messages.length; i++) {
    		const message = messages[i]
      	message.message_id = i

      	if (message.deleted) continue;

      	renderMsgEle(message)

    	}
    },
    error: (error) => {
      const { message } = error.responseJSON
      showAlert({ message })
    }
	});
}
const deleteMsg = (data) => sendToChatAjax(data, "/room/message/delete", "delete")
const updateToken = (token) => setCookie("token", token, 1);
const deleteToken = () => deleteCookie("token");
const getToken = () => getCookie("token")

function renderMsgEle(data) {
	const { display_name, user_id, message, message_id, room_id, created_at } = data

	const profileEle = profileImg ? 
		`<img class="avatar-img" src="${profileImg}" alt="${display_name}">` : 
		`<i class="avatar-img fa fa-user" title="${display_name}"><i/>`
	const messageEle = `
		<span class="msg-box" data-user-id="${user_id}" data-message-id="${message_id}" data-room-id="${room_id}">
			<div class="user-avatar-con">
				${profileEle}
			</div>
			<div class="user-msg-info-con">
				<div class="user-info-con">
					<span class="user-name">
						${display_name}
					</span>
					<span class="user-msg-time-box">
						${created_at}
					</span>
				</div>
				<div class="user-msg-con">
					${message}
				</div>
			</div>
		</span>
	`
	$('.chat-msgs-box').append(messageEle);
}


            // message_data = {
            //     "display_name": user_data.get("display_name"),
            //     "user_id": user_data.get("user_id"),
            //     "created_at": get_current_date(),
            //     "message": message,
            //     "deleted": False,
            // }


function deleteMsgEle(data) {
	const { message_id } = data
	$(`.msgs-box[data-message-id="${message}"]`).fadeOut().remove();
}

const actions = {
	send: renderMsgEle,
	delete: deleteMsgEle,
}

function sendToChatAjax(data, endpoint, action_type) {
	data.token = getToken()
	data.user_id = userLiveChatId 
	data.room_id = roomId
	data.room_code = roomCode

	console.log({ data })

  $.ajax({
	  url: liveChatBase + endpoint,
	  type: 'POST',
	  headers: {
	    'accept': 'application/json',
	    'Content-Type': 'application/json'
	  },
	  data: JSON.stringify(data),
    success: (response) => {
    	const { data } = response
    	console.log({ response })
      const action = actions[action_type]
			updateToken(data.token)
      action(data)
    },
    error: (error) => {
      const { message } = error.responseJSON
      showAlert({ message })
    }
	});
}
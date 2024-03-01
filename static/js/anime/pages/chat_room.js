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

function sendMsgEle(data) {
	// const messageEle = `
	// 	<span class="msg-box">
	// 		<div class="user-avatar-con">
	// 			<img class="avatar-img" src="https://img.flawlessfiles.com/_r/100x100/100/avatar/demon_splayer/File11.jpg" alt="user">
	// 		</div>
	// 		<div class="user-msg-info-con">
	// 			<div class="user-info-con">
	// 				<span class="user-name">
	// 					james
	// 				</span>
	// 				<span class="user-msg-time-box">
	// 					2023/10/05, 09:30
	// 				</span>
	// 			</div>
	// 			<div class="user-msg-con">
	// 				hello
	// 			</div>
	// 		</div>
	// 	</span>
	// `
}

function editMsgEle(data) {
}

function deleteMsgEle(data) {
}

function sendToChatAjax(data, endpoint, action_type) {
	const actions = {
		send: sendMsgEle,
		edit: editMsgEle,
		delete: deleteMsgEle,
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
$(() => {
	let is_form = false
	let is_edit = false
	const loader_wrapper = $(`#page_loader_wrapper`)
	const users_list = Object.keys(users_dict)
		
	$(".admin_users_search").on("keyup input", function() {	
		const this_ele = $(this)
		const val = this_ele.val();
		const mode = this_ele.data("mode")
		const render_search_results = (results, mode) => {
		  let items_html = ``;
		  
		  for (let i = 0; i < results.length; i++) {
			const email = results[i];
			const username = users_dict[email].username
			
			items_html += `
				<li><a href="#${email}"><span class="item email_tab">${email}</span><span class="item username_tab">${username}</span></li>
			`;
		  }
		  
		  items_html != `` ? $(`.admin_items_wrapper[data-mode="${mode}"`).html($.trim(items_html)) : $(`.admin_items_wrapper[data-mode="${mode}"`).html($.trim(`<li style="text-align: center;">No Results</li>`))
		}

		if (val != "") {
		  let results = users_list.filter(item => item.toLowerCase().includes(val))
		  render_search_results(results, mode);
		}
	});
	
	$(".user_act_buttons").click(function() {
		const this_ele = $(this)
		const type = this_ele.data("type")
		
		if (type != "edit") {
			const email = this_ele.data("email")
					
			$.ajax({
			  type: "post",
			  url: "/act_user",
			  data: {
				csrfmiddlewaretoken: csrf_token,
				type: type,
				email: email,
			  },
			  beforeSend: () => {
				loader_wrapper.css("display", "flex");
			  },
			  success: (res) => {
				  const res_data = JSON.parse(res)
				  if(res_data.status_code == 200) {
					  if(type == "delete") $(`.user_wrapper[data-email="${email}"]`).remove()
					  else window.open('/profile', '_blank');
				  }
				  else show_alert(res_data.message)
				  loader_wrapper.css("display", "none");
			  },
			});
		} else {
			const user_form_wrapper = $("#user_form_wrapper")
			const users_wrapper = $("#users_wrapper")
			const raw_values = this_ele.data("values")
			const values = JSON.parse(raw_values.replace('True', "true").replace(/'/g, '"'))
			const profile_image = values.profile_image
			const id = values.email_hash_code
			const username = values.username
			const password = values.password
			$(".save_btn").data("id", id)
			$(".profile_image").attr("src", profile_image)
			$('.username_input').val(username)
			$('.password_input').val(password)
			
			users_wrapper.fadeOut(() => {
				user_form_wrapper.fadeIn()
			});
		}
	})
	
	$(".vip_check").change(function() {
		const this_ele = $(this)
		const email = this_ele.data("email")
		const value = this_ele.is(':checked');
		
		$.ajax({
		  type: "post",
		  url: "/save_site_settings",
		  data: {
			csrfmiddlewaretoken: csrf_token,
			type: "change_vip",
			data: JSON.stringify({email, value}),
		  },
		  beforeSend: () => {
			loader_wrapper.css("display", "flex");
		  },
		  success: (res) => {
			  const res_data = JSON.parse(res)
			  
			  if (res_data.status_code == 200) $(`.date_wrapper[data-email="${email}"]`).text(res_data.data.vip_expiration)
			  
			  loader_wrapper.css("display", "none");
			  
			  show_alert(res_data.message)
		  },
		});
	})
	
	$("#close_auth_icon").click(function() {
		console.log("clicked")
		const user_form_wrapper = $("#user_form_wrapper")
		const users_wrapper = $("#users_wrapper")
		user_form_wrapper.fadeOut(() => {
			users_wrapper.fadeIn()
		});
	})
	
	$(".save_btn").click(function() {
		const this_ele = $(this)
		const user_form_wrapper = $("#user_form_wrapper")
		const users_wrapper = $("#users_wrapper")
		const id = this_ele.data("id")
		const profile_image = $(".profile_image").attr("src")
		const username = $('.username_input').val()
		const password = $('.password_input').val()
		const values = {profile_image, username, password, id}
		this_ele.data("id", "")
		
		$.ajax({
		  type: "post",
		  url: "/save_site_settings",
		  data: {
			csrfmiddlewaretoken: csrf_token,
			type: "edit_user",
			data: JSON.stringify(values),
		  },
		  beforeSend: () => {
			loader_wrapper.css("display", "flex");
		  },
		  success: (res) => {
			  const res_data = JSON.parse(res)
				user_form_wrapper.fadeOut(() => {
					users_wrapper.fadeIn()
				});
			  loader_wrapper.css("display", "none");
			  
			  show_alert(res_data.message)
		  },
		});
	})
	
})
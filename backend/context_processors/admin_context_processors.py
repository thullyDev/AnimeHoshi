def global_static_data(request):
	data = {
		"admin_menu_items": [
			  {
			    "path": "/admin/dashboard",
			    "label": "dashboard",
			    "icon": "fas fa-tachometer-alt",
			  },
			  {
			    "path": "/admin/scripts",
			    "label": "scripts",
			    "icon": "fas fa-code",
			  },
			  {
			    "path": "/admin/general",
			    "label": "general",
			    "icon": "fas fa-sliders-h",
			  },
			  {
			    "path": "/admin/advance",
			    "label": "advance",
			    "icon": "fas fa-cogs",
			  },
			  {
			    "path": "/admin/admins",
			    "label": "admins",
			    "icon": "fas fa-user-cog",
			  },
		]
	}
	return data

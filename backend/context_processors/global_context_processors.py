from datetime import datetime
from functools import lru_cache


def global_static_data(request):
	admin_menu_items = [
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
	tioanime_queries = {
		"genres": [
			{"value": "None", "name": "None"},
		    {"value": "accion", "name": "Acción"},
		    {"value": "artes-marciales", "name": "Artes Marciales"},
		    {"value": "aventura", "name": "Aventuras"},
		    {"value": "carreras", "name": "Carreras"},
		    {"value": "ciencia-ficcion", "name": "Ciencia Ficción"},
		    {"value": "comedia", "name": "Comedia"},
		    {"value": "demencia", "name": "Demencia"},
		    {"value": "demonios", "name": "Demonios"},
		    {"value": "deportes", "name": "Deportes"},
		    {"value": "drama", "name": "Drama"},
		    {"value": "ecchi", "name": "Ecchi"},
		    {"value": "escolares", "name": "Escolares"},
		    {"value": "espacial", "name": "Espacial"},
		    {"value": "fantasia", "name": "Fantasía"},
		    {"value": "harem", "name": "Harem"},
		    {"value": "historico", "name": "Histórico"},
		    {"value": "infantil", "name": "Infantil"},
		    {"value": "josei", "name": "Josei"},
		    {"value": "juegos", "name": "Juegos"},
		    {"value": "magia", "name": "Magia"},
		    {"value": "mecha", "name": "Mecha"},
		    {"value": "militar", "name": "Militar"},
		    {"value": "misterio", "name": "Misterio"},
		    {"value": "musica", "name": "Música"},
		    {"value": "parodia", "name": "Parodia"},
		    {"value": "policia", "name": "Policía"},
		    {"value": "psicologico", "name": "Psicológico"},
		    {"value": "recuentos-de-la-vida", "name": "Recuentos de la vida"},
		    {"value": "romance", "name": "Romance"},
		    {"value": "samurai", "name": "Samurai"},
		    {"value": "seinen", "name": "Seinen"},
		    {"value": "shoujo", "name": "Shoujo"},
		    {"value": "shounen", "name": "Shounen"},
		    {"value": "sobrenatural", "name": "Sobrenatural"},
		    {"value": "superpoderes", "name": "Superpoderes"},
		    {"value": "suspenso", "name": "Suspenso"},
		    {"value": "terror", "name": "Terror"},
		    {"value": "vampiros", "name": "Vampiros"},
		    {"value": "yaoi", "name": "Yaoi"},
		    {"value": "yuri", "name": "Yuri"}
		 ], 
		 "status": [
			    {"value": "None", "name": "None"},
			    {"value": "2", "name": "Finalizado"},
			    {"value": "1", "name": "En emisión"},
			    {"value": "3", "name": "Próximamente"}
			],
		 "types": [
			    {"value": "None", "name": "None"},
			    {"value": "0", "name": "TV"},
			    {"value": "1", "name": "Película"},
			    {"value": "2", "name": "OVA"},
			    {"value": "3", "name": "Especial"}
			],
		 "year": get_years(),
	}
	latanime_queries = {
		"genres": [
			{"value": "None", "name": "None"},
		    {"value": "accion", "name": "Acción"},
		    {"value": "aventura", "name": "Aventura"},
		    {"value": "carreras", "name": "Carreras"},
		    {"value": "ciencia-ficcion", "name": "Ciencia Ficción"},
		    {"value": "comedia", "name": "Comedia"},
		    {"value": "cyberpunk", "name": "Cyberpunk"},
		    {"value": "deportes", "name": "Deportes"},
		    {"value": "drama", "name": "Drama"},
		    {"value": "ecchi", "name": "Ecchi"},
		    {"value": "escolares", "name": "Escolares"},
		    {"value": "fantasia", "name": "Fantasía"},
		    {"value": "gore", "name": "Gore"},
		    {"value": "harem", "name": "Harem"},
		    {"value": "horror", "name": "Horror"},
		    {"value": "josei", "name": "Josei"},
		    {"value": "lucha", "name": "Lucha"},
		    {"value": "magia", "name": "Magia"},
		    {"value": "mecha", "name": "Mecha"},
		    {"value": "militar", "name": "Militar"},
		    {"value": "misterio", "name": "Misterio"},
		    {"value": "musica", "name": "Música"},
		    {"value": "parodias", "name": "Parodias"},
		    {"value": "psicologico", "name": "Psicológico"},
		    {"value": "recuerdos-de-la-vida", "name": "Recuerdos de la vida"},
		    {"value": "seinen", "name": "Seinen"},
		    {"value": "shojo", "name": "Shojo"},
		    {"value": "shonen", "name": "Shonen"},
		    {"value": "sobrenatural", "name": "Sobrenatural"},
		    {"value": "vampiros", "name": "Vampiros"},
		    {"value": "yaoi", "name": "Yaoi"},
		    {"value": "yuri", "name": "Yuri"},
		    {"value": "latino", "name": "Latino"},
		    {"value": "espacial", "name": "Espacial"},
		    {"value": "historico", "name": "Histórico"},
		    {"value": "samurai", "name": "Samurai"},
		    {"value": "artes-marciales", "name": "Artes Marciales"},
		    {"value": "demonios", "name": "Demonios"},
		    {"value": "romance", "name": "Romance"},
		    {"value": "dementia", "name": "Dementia"},
		    {"value": "policia", "name": "Policía"},
		    {"value": "castellano", "name": "Castellano"},
		    {"value": "historia-paralela", "name": "Historia paralela"},
		    {"value": "aenime", "name": "Aenime"},
		    {"value": "donghua", "name": "Donghua"},
		    {"value": "blu-ray", "name": "Blu-ray"},
		    {"value": "monogatari", "name": "Monogatari"},
		    {"value": "suspenso", "name": "Suspenso"}
		 ],
		 "alphabet_options": [
			{"value": "None", "name": "None"},
		    {"value": "09", "name": "0-9"},
		    {"value": "A", "name": "A"},
		    {"value": "B", "name": "B"},
		    {"value": "C", "name": "C"},
		    {"value": "D", "name": "D"},
		    {"value": "E", "name": "E"},
		    {"value": "F", "name": "F"},
		    {"value": "G", "name": "G"},
		    {"value": "H", "name": "H"},
		    {"value": "I", "name": "I"},
		    {"value": "J", "name": "J"},
		    {"value": "K", "name": "K"},
		    {"value": "L", "name": "L"},
		    {"value": "M", "name": "M"},
		    {"value": "N", "name": "N"},
		    {"value": "O", "name": "O"},
		    {"value": "P", "name": "P"},
		    {"value": "Q", "name": "Q"},
		    {"value": "R", "name": "R"},
		    {"value": "S", "name": "S"},
		    {"value": "T", "name": "T"},
		    {"value": "U", "name": "U"},
		    {"value": "V", "name": "V"},
		    {"value": "W", "name": "W"},
		    {"value": "X", "name": "X"},
		    {"value": "Y", "name": "Y"},
		    {"value": "Z", "name": "Z"}
		],
		"types": [
			{"value": "None", "name": "None"},
		    {"value": "anime", "name": "Anime"},
		    {"value": "ova", "name": "Ova"},
		    {"value": "Película", "name": "Película"},
		    {"value": "especial", "name": "Especial"},
		    {"value": "corto", "name": "Corto"},
		    {"value": "ona", "name": "Ona"},
		    {"value": "donghua", "name": "Donghua"},
		    {"value": "sin-censura", "name": "Sin Censura"},
		    {"value": "preestreno", "name": "PREESTRENO"},
		    {"value": "pelicula-1080p", "name": "Pelicula 1080p"},
		    {"value": "latino", "name": "Latino"},
		    {"value": "Película Latino", "name": "Pelicula Latino"},
		    {"value": "castellano", "name": "Castellano"},
		    {"value": "Película Castellano", "name": "Pelicula Castellano"},
		    {"value": "ova-latino", "name": "Ova Latino"},
		    {"value": "ova-castellano", "name": "Ova Castellano"},
		    {"value": "latino-sin-censura", "name": "Latino Sin Censura"},
		    {"value": "live-action", "name": "Live Action"},
		    {"value": "Cartoon", "name": "Cartoon"},
		    {"value": "catalan", "name": "Catalán"}
		 ],
		"year": get_years(),
	}

	auths = {
		"signup": [
			{
				"input": "text",
				"key": "user",
				"icon": "fas fa-user",
			},
			{
				"input": "text",
				"key": "email",
				"icon": "fas fa-envelope",
			},
			{
				"input": "password",
				"key": "confirm",
				"icon": "fas fa-key",
			},
			{
				"input": "password",
				"key": "password",
				"icon": "fas fa-key",
			},
		],
		"login": [
			{
				"input": "text",
				"key": "email",
				"icon": "fas fa-envelope",
			},
			{
				"input": "password",
				"key": "password",
				"icon": "fas fa-key",
			},
		],
		"forgot_password": [
			{
				"input": "text",
				"key": "email",
				"icon": "fas fa-envelope",
			},
		],
		"resend": [
			{
				"input": "text",
				"key": "email",
				"icon": "fas fa-envelope",
			},
		],
		"verify": [
			{
				"input": "text",
				"key": "code",
				"icon": "fas fa-key",
			},
		],
		"renew_password": [
			{
				"input": "password",
				"key": "confirm",
				"icon": "fas fa-key",
			},
			{
				"input": "password",
				"key": "password",
				"icon": "fas fa-key",
			},
		],
	}
	data = {
		"admin_menu_items": admin_menu_items,
		"tioanime_queries": tioanime_queries,
		"latanime_queries": latanime_queries,
		"auths": auths,
	}
	return data

@lru_cache(maxsize=None)
def get_years(start_year=1950):
    current_year = datetime.now().year
    years = [ {"value": i, "name": i} for i in range(current_year, start_year - 1, -1) ]
    return years
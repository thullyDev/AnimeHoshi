  const schedule_swiper = new Swiper("#schedule_swiper", {
	direction: "horizontal",
	loop: true,
	slidesPerView: 5,
	spaceBetween: 20,
	navigation: {
	  nextEl: ".swiper-button-next",
	  prevEl: ".swiper-button-prev",
	},
	breakpoints: {
	  200: {
		slidesPerView: 3,
	  },
	  500: {
		slidesPerView: 4,
	  },
	  800: {
		slidesPerView: 5,
	  },
	},
  });

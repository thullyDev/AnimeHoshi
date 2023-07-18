//*** change yourdomain.in to your domain

const disqus_config = function () {
  this.page.url = `https://yourdomain.in/watch/${anime_id}/`;
  this.page.identifier = anime_id;
};

//? DON'T EDIT THE BLOCK OF CODE BELOW
(function () {
  const d = document,
    s = d.createElement("script");
  s.src = "https://test-cznbonimn3.disqus.com/embed.js";
  s.setAttribute("data-timestamp", +new Date());
  (d.head || d.body).appendChild(s);
})();
//? DON'T EDIT THE BLOCK OF CODE ABOVE

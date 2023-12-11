const pages = [
    "dashboard", 
    "general",
    "advance",
    "scripts",
    "admins",
  ]

const admin_routes = [];

for (const page of pages) {
  admin_routes.push({ 
    match: `/admin/${page}`, 
    load: `/src/pages/index.astro` 
    // load: `/src/pages/admin/{page}.astro` 
  })
}

console.log(admin_routes)

export default admin_routes

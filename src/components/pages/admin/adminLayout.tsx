import React, { useEffect } from "react";
import AdminFooter from "../../sections/adminFooter/adminFooter";
import Header from "../../sections/adminHeader/adminHeader";
import Menu from "../../sections/menu/menu";
import "./styles/adminLayout.scss";



interface AdminLayoutProps {
  element: React.ReactNode;
  title: string;
}

const menu_items = [
  {
    path: "/admin/dashboard",
    label: "dashboard",
    icon: "fas fa-tachometer-alt",
  },
  {
    path: "/admin/scripts",
    label: "scripts",
    icon: "fas fa-code",
  },
  {
    path: "/admin/general",
    label: "general",
    icon: "fas fa-sliders-h",
  },
  {
    path: "/admin/advance",
    label: "advanced",
    icon: "fas fa-cogs",
  },
  {
    path: "/admin/admins",
    label: "admins",
    icon: "fas fa-user-cog",
  },
];

const AdminLayout: React.FC<AdminLayoutProps> = ({ element, title }) => {
  useEffect(() => {
    document.title = `${title} | Admin Panel` || "Admin Panel";
  }, [title])
  ;
  const style_import = title.charAt(0).toLowerCase() + title.slice(1) + ".scss"

  remove_stylesheets(style_import)

  import(`./styles/${style_import}`);

  return (
    <>
      <div className="page-content">
        <div className="side-bar-con">
          <Menu items={menu_items}></Menu>
        </div>
        <div className="right-con">
          <Header></Header>
          <main className="main-content">
            <h2 className="page-label">{title}</h2>
            {element}
          </main>
        </div>
        <AdminFooter></AdminFooter>
      </div>
    </>
  );
};

function remove_stylesheets(title: string) {
  const stylesheets = document.querySelectorAll('style');
  stylesheets.forEach((stylesheet) => {
    const rawhref = stylesheet.getAttribute('data-vite-dev-id')

    if (!rawhref) return null

    const href_list = rawhref.split("/")
    const current_style = href_list[href_list.length - 1]


    const styles =  [ "adminLayout.scss", title ]

    if (!styles.includes(current_style)) {
      // @ts-ignore
      // stylesheet.parentNode.removeChild(stylesheet);
    }
  });
}


export default AdminLayout;

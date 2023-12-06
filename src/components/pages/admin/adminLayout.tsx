import React, { useEffect } from "react";
import AdminFooter from "../../sections/adminFooter/adminFooter";
import Header from "../../sections/adminHeader/adminHeader";
import Menu from "../../sections/menu/menu";
import "./adminLayout.scss";

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
  }, [title]);

  return (
    <>
      <div className="page-content">
        <div className="side-bar-con">
          <Menu items={menu_items}></Menu>
        </div>
        <div className="right-con">
          <Header></Header>
          <main className="main-content">{element}</main>
          <AdminFooter></AdminFooter>
        </div>
      </div>
    </>
  );
};

export default AdminLayout;

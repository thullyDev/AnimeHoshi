import React from "react";
import Title from "../../widgets/title/title";
import Nav from "../../widgets/nav/nav";
import Search from "../../widgets/search/search";
import MenuBtn from "../../widgets/menuBtn/menuBtn";
import Account from "../../widgets/account/account";

const AdminHeader = () => {
  return (
    <header className="main-header">
      <div className="header-viewer-con desktop-viewer-con">
        <MenuBtn></MenuBtn>
        <Search></Search>
        <Account></Account>
      </div>
    </header>
  );
};

export default AdminHeader;

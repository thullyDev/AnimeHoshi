import React, { Component } from "react";
import Header from "../../sections/header/header";
import footer from "../../sections/footer/footer";
import Menu from "../../sections/menu/menu";
import Main from "../main";

class Home extends Component {
  render() {
    return (
      <>
        <Menu />
        <Header />
        <Main />
        <footer />
      </>
    );
  }
}

export default Home;

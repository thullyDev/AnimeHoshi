import React, { Component } from 'react';
import Title from "../../widgets/title/title"
import Nav from "../../widgets/nav/nav"
import Search from "../../widgets/search/search"
import MenuBtn from "../../widgets/menuBtn/menuBtn"

export class Header extends Component {
  render() {
    return (
      <>
         <header className="page_header">
          <div className="top_side">
            <MenuBtn/>
            <Title/>
            <Search/>
            <Nav/>
          </div>
          <div className="bottom_side">
            <div className="mobile_search_wrapper">
              <Search/>
            </div>
          </div>
        </header>
      </>
    );
  }
}


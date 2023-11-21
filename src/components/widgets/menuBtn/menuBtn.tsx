import React, { Component } from "react";

class MenuBtn extends Component {
  render() {
    return (
      <>
        <div className="menu_btn_wrapper">
          <button type="button" className="menu_btn">
            <img src="/static/images/menu_bars.svg" alt="menu" />
          </button>
        </div>
      </>
    );
  }
}

export default MenuBtn;

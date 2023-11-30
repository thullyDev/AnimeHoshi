import React, { Component } from "react";

class MenuBtn extends Component {
  render() {
    return (
      <>
        <div className="menu-btn-con">
          <button type="button" className="menu-btn">
            <i class="fas fa-bars"></i>
          </button>
        </div>
      </>
    );
  }
}

export default MenuBtn;

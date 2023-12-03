import React, { Component } from "react";

export class Title extends Component {
  render() {
    return (
      <>
        <div className="title-con">
          <a href="/" className="home-link title-link">
            <img className="site-logo" src="/static/images/site-logo.png" alt="AnimeHoshi logo" width="100" />
          </a>
        </div>
      </>
    );
  }
}

export default Title;

import React, { Component } from "react";

export class Title extends Component {
  render() {
    return (
      <>
        <div className="title_wrapper">
          <a href="/" className="title_link">
            {/*<img div="title_logo" src="/static/images/title_logo.png" alt="AnimeHoshi logo" />*/}
            Title goes here
          </a>
        </div>
      </>
    );
  }
}

export default Title;
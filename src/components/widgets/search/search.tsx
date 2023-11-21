import React, { Component } from "react";

class Search extends Component {
  render() {
    return (
      <>
        <div className="outter_search_wrapper">
          <div className="search_wrapper">
            <div className="search_input_wrapper">
              <button type="button" className="search_btn">
                <img
                  src="/static/images/search.svg"
                  width="20px"
                  height="20px"
                  alt="close icon"
                  className="search_icon"
                />
              </button>
              <input className="search_input" placeholder="search anime..." type="query" name="search" />
              <a href="/" className="filter_link">
                <img src="/static/images/filter.svg" width="20px" height="20px" alt="filter" /> filter
              </a>
            </div>
            <div className="search_items_wrapper">
              <div className="search_loader_wrapper">
                <div className="loader_two_wrapper">
                  <div className="loader_two"></div>
                </div>
              </div>
              <ul className="search_list_wrapper"></ul>
              <a href="/home" className="search_view_all_wrapper" data-open="false">
                view all
              </a>
            </div>
          </div>
        </div>
      </>
    );
  }
}

export default Search;

import React, { Component } from "react";


            // <li className="menu_item">
            //   <a href="/home" className="menu_item_link">
            //     Home
            //   </a>
            // </li>
            // <li className="menu_item">
            //   <a href="/latino-filter?p=1" className="menu_item_link">
            //     Latino
            //   </a>
            // </li>
            // <li className="menu_item">
            //   <a href="/filter?p=1&type=1" className="menu_item_link">
            //     TV
            //   </a>
            // </li>
            // <li className="menu_item">
            //   <a href="/filter?p=1&type=2" className="menu_item_link">
            //     Movies
            //   </a>
            // </li>
            // <li className="menu_item">
            //   <a href="/filter?p=1&type=3" className="menu_item_link">
            //     Ova
            //   </a>
            // </li>
            // <li className="menu_item">
            //   <a href="/filter?p=1&type=4" className="menu_item_link">
            //     Special
            //   </a>
            // </li>
            // <li className="menu_item">
            //   <a href="/filter?p=1&status=1" className="menu_item_link">
            //     Airing
            //   </a>
            // </li>
            // <li className="menu_item">
            //   <a href="/filter?p=1&status=2" className="menu_item_link">
            //     Complete
            //   </a>
            // </li>
            // <li className="menu_item">
            //   <a href="/filter?p=1&status=3" className="menu_item_link">
            //     Upcoming
            //   </a>
            // </li>

            
                    // <li className="genre">
                    //   <a href="/filter?p=1&genre=accion" className="genre_link">
                    //     accion
                    //   </a>
                    // </li>
                    // <li className="genre">
                    //   <a href="/filter?p=1&genre=accion" className="genre_link">
                    //     accion
                    //   </a>
                    // </li>
                    // <li className="genre">
                    //   <a href="/filter?p=1&genre=accion" className="genre_link">
                    //     accion
                    //   </a>
                    // </li>
                    // <li className="genre">
                    //   <a href="/filter?p=1&genre=accion" className="genre_link">
                    //     accion
                    //   </a>
                    // </li>
                    // <li className="genre">
                    //   <a href="/filter?p=1&genre=accion" className="genre_link">
                    //     accion
                    //   </a>
                    // </li>
                    // <li className="genre">
                    //   <a href="/filter?p=1&genre=accion" className="genre_link">
                    //     accion
                    //   </a>
                    // </li>
                    // <li className="genre">
                    //   <a href="/filter?p=1&genre=accion" className="genre_link">
                    //     accion
                    //   </a>
                    // </li>
                    // <li className="genre">
                    //   <a href="/filter?p=1&genre=accion" className="genre_link">
                    //     accion
                    //   </a>
                    // </li>
                    // <li className="genre">
                    //   <a href="/filter?p=1&genre=accion" className="genre_link">
                    //     accion
                    //   </a>
                    // </li>
                    // <li className="genre">
                    //   <a href="/filter?p=1&genre=accion" className="genre_link">
                    //     accion
                    //   </a>
                    // </li>
                    // <li className="genre">
                    //   <a href="/filter?p=1&genre=accion" className="genre_link">
                    //     accion
                    //   </a>
                    // </li>
                    // <li className="genre">
                    //   <a href="/filter?p=1&genre=accion" className="genre_link">
                    //     accion
                    //   </a>
                    // </li>

class Menu extends Component {
  render() {
    return (
      <>
        <div className="menu_wrapper">
          <div className="menu_cb_wrapper">
            <span role="button" className="cb_button">
              close menu
            </span>
          </div>
          <ul>
            <li className="menu_item genre_item">
              <div className="outter_genres_wrapper">
                <div className="label_genre_wrapper">
                  Genres <i className="fa-solid fa-plus"></i>
                </div>
                <div className="genres_wrapper">
                  <ul>
                  </ul>
                </div>
              </div
            </li>
          </ul>
        </div>
      </>
    );
  }
}

export default Menu

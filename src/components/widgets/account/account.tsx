import { Component } from "react";

class Account extends Component {
  render() {
    return (
      <>
        <div className="outter-account-con">
          <div className="account-profile-image-con">
            <span role="button" className="account-btn actions-dropdown-btn">
              <img
                src="https://i.pinimg.com/564x/68/78/49/687849b7834fc551b823592e4abac45f.jpg"
                alt="user name"
                className="account-image"
                width="100"
              />
            </span>
          </div>
          <div className="actions-dropdown-menu">
            <ul>
              <li className="actions-items">
                <span role="button" className="action-btn logout-btn">
                  LOGOUT
                </span>
              </li>
              <li className="actions-items">
                <span role="button" className="action-btn reset-btn">
                  RESET
                </span>
              </li>
            </ul>
          </div>
        </div>
      </>
    );
  }
}

export default Account;

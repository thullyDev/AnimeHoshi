import React from "react";
import { Link } from 'react-router-dom';
import Title from "../../widgets/title/title";
import { SITE_NAME, SITE_EMAIL } from "../../../resources/config";

const pages =  [
  { path: '/filter', label: 'filter' },
  { path: '/home', label: 'home' },
  { path: '/', label: 'landing' },
  { path: '/#about', label: 'about us' },
];


const socials =  [
  { 
    path: 'https://reddit.com/', 
    label: 'reddit',
    icon: "fab fa-reddit"
   },
  { 
    path: 'https://twitter.com/', 
    label: 'twitter',
    icon: "fab fa-twitter"
   },
  { 
    path: 'https://discord.com/', 
    label: 'discord',
    icon: "fab fa-discord"
   },
  { 
    path: 'https://youtube.com/', 
    label: 'youtube',
    icon: "fab fa-youtube"
   },
];
 
// const SITE_EMAIL = "admin@animehoshi.com"
// const SITE_NAME = "AnimeHoshi"

const AdminFooter = () => {
  return (
    <footer className="main-footer">
      <div className="inner-con">
        <div className="title-con">
          <Title></Title>
        </div>
        <div className="middle-con">
          <div className="left-side">
            <div className="inner-con">
              <ul>
                {pages.map((item, index) => (
                  <li className="footer-page-links">
                    <Link key={index} to={item.path} className="menu-link">
                      {item.label}
                    </Link>
                  </li>              
                ))}
              </ul>
            </div>
          </div>
          <div className="right-side">
            <div className="inner-con">
              <ul>
                {socials.map((item, index) => (
                  <li className="footer-links">
                    <Link key={index} to={item.path} className="menu-link">
                      {item.label} <i className={item.icon}></i>
                    </Link>
                  </li>              
                ))}
              </ul>
            </div>
          </div>
        </div>
        <div className="bottom-con">
          <div className="inner-con">
              <p>&copy; 2023 {SITE_NAME}. All rights reserved. | 
                <a href="#">Terms of Service</a> | 
                <a href="#">Privacy Policy</a>
              </p>
              <p>Contact: {SITE_EMAIL}</p>
          </div>
        </div>
      </div>
    </footer>
  );
};

export default AdminFooter;

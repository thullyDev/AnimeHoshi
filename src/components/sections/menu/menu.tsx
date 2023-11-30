import React from 'react';
import { Link } from 'react-router-dom';
import Title from '../../widgets/title/title';

const Menu = ({ items }) => {
  return (
    <>
      <div className="outer-menu-con">
        <Title />
        <div className="inner-menu-con">
          <ul>
            {items.map((item, index) => (
              <li className="menu-item">
                <Link key={index} to={item.path} className="menu-link">
                  {item.label}
                </Link>
              </li>              
            ))}
          </ul>
        </div>
      </div>
    </>
  );
};

export default Menu;

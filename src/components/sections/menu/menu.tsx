import { Link } from "react-router-dom";
import Title from "../../widgets/title/title";

interface MenuItem {
  path: string;
  label: string;
  icon: string;
}

interface MenuProps {
  items: MenuItem[];
}

const Menu: React.FC<MenuProps> = ({ items }) => {
  return (
    <>
      <div className="outer-menu-con">
        <Title />
        <div className="inner-menu-con">
          <ul>
            {items.map((item, index) => (
              <li key={index} className="menu-item">
                <Link to={item.path} className="menu-link">
                  <i className={item.icon} style={
                    {
                      margin: "5px",
                    }
                  }></i> 
                  <span className="menu-text">{item.label} </span>
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

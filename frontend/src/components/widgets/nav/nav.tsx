const Nav = () => (
  <>
    <nav className="header_nav">
      <div className="header_nav_wrapper">
        <div className="nav_item">
          <a href="/catalogue" className="nav_link">
            Catálogo
          </a>
        </div>
        <div className="nav_item">
          <a href="/donate" className="nav_link">
            donar
          </a>
        </div>
        <div className="nav_item">
          <a href="/random" className="nav_link">
            aleatorio
          </a>
        </div>
        <div className="nav_item">
          <a href="/watch_togather" className="nav_link">
            ver juntos
          </a>
        </div>
      </div>
    </nav>
  </>
);

export default Nav;

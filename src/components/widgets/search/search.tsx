import LoaderTwo from "../loaderTwo/loaderTwo";

const Search = () => (
  <>
    <div className="outter-search-con">
      <div className="search-con">
        <div className="search-input-con">
          <button type="button" className="search-btn">
            <i className="fas fa-search"></i>
          </button>
          <input className="search-input" placeholder="search anime..." type="query" name="search" />
        </div>
        <div className="search-items-con">
          <div className="search-loader-con">
            <LoaderTwo />
          </div>
          <ul className="search-list-con"></ul>
          <a href="/home" className="search-view-all-con" data-open="false">
            view all
          </a>
        </div>
      </div>
    </div>
  </>
);

export default Search;

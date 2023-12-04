import LoaderTwo from "../loaderTwo/loaderTwo";

const Search = () => (
  <>
    <div className="outter_search_wrapper">
      <div className="search_wrapper">
        <div className="search_input_wrapper">
          <button type="button" className="search_btn">
            <i className="fas fa-search"></i>
          </button>
          <input className="search_input" placeholder="search anime..." type="query" name="search" />
          <a href="/" className="filter_link">
            <i className="fas fa-filter"></i> filter
          </a>
        </div>
        <div className="search_items_wrapper">
          <div className="search_loader_wrapper">
            <LoaderTwo />
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

export default Search;

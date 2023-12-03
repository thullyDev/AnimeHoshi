import Table from "../../widgets/table/table";

const heads = ["poster", "title", "status"];

const AnalyticsAnimesTable = ({ items, pages }) => {
  const table_heads = heads.map((item, index) => (
    <th className="table-head users-head" key={index}>
      {item}
    </th>
  ));
  const table_items = items.map((item, index) => {
    return (
      <>
        <tr className="table-row anime-row" key={index}>
          <td className="table-item anime-item">
            <p className="profile-image-tick">
              <a href={`/ver/${item.slug}`} className="watch-link slug">
                <img src={item.poster_url} alt={item.title} title={item.title} className="poster-image" />
              </a>
            </p>
          </td>
          <td className="table-item anime-item">
            <p className="title-tick">{item.title}</p>
          </td>
          <td className="table-item anime-item">
            <p className={!item.deleted ? "status-tick active" : "status-tick remove"}>
              {!item.deleted ? "active" : "inactive"}
            </p>
          </td>
          <td className="table-item anime-item">
            <button className="table-btn disable" data-disabled={item.disabled} data-key={index}>
              disable
            </button>
          </td>
        </tr>
      </>
    );
  });
  const dot_style = {
    fontSize: "5px",
  };
  const dots = [];
  for (let i = 0; i <= 4; i++) {
    dots.push(
      <span key={i} className="pagination-span">
        <i style={dot_style} className="fas fa-circle"></i>
      </span>,
    );
  }

  return (
    <div className="table-con">
      <div className="table-label">
        <h3 className="label">Latest Animes</h3>
      </div>
      <Table heads={table_heads} items={table_items}></Table>
      <div className="tabel-pagination">
        <ul>
          {/*{pages.map}*/}
          <li className="pages-ticks">
            <button data-page={pages.page} className="pagination-btn page-btn">
              {pages.page}
            </button>
          </li>
          {dots.map((item, index) => item)}
          <li className="pages-ticks">
            <button data-page={pages.amount_pages} className="pagination-btn page-btn">
              {pages.amount_pages}
            </button>
          </li>
        </ul>
      </div>
    </div>
  );
};

export default AnalyticsAnimesTable;

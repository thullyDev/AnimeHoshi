import Table from "../../widgets/table/table";


interface Items {
  id: number;
  poster_url: string;
  title: string;
  slug: string;
  disabled: boolean;
}

interface Pages {
  amount_pages: number;
  page: number;
}

interface AnalyticsAnimesTableProps {
  items: Items[];
  pages: Pages;
}

const heads = ["poster", "title", "status"];


const AnalyticsAnimesTable: React.FC<AnalyticsAnimesTableProps> = ({ items, pages }) => {
  const table_heads = heads.map((item, index) => (
    <th className="table-head users-head" key={index}>
      {item}
    </th>
  ));
  const table_items = items.map((item, index) => {
    const { poster_url, title, slug, disabled } = item
    return (
      <>
        <tr className="table-row anime-row" key={index}>
          <td className="table-item anime-item">
            <p className="profile-image-tick">
              <a href={`/ver/${slug}`} className="watch-link slug">
                <img src={poster_url} alt={title} title={title} className="poster-image" />
              </a>
            </p>
          </td>
          <td className="table-item anime-item">
            <p className="title-tick">{title}</p>
          </td>
          <td className="table-item anime-item">
            <p className={!deleted ? "status-tick active" : "status-tick remove"}>
              {!deleted ? "active" : "inactive"}
            </p>
          </td>
          <td className="table-item anime-item">
            <button className="table-btn disable" data-disabled={disabled} data-key={index}>
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

  const { page, amount_pages } = pages

  return (
    <div className="table-con">
      <div className="table-label">
        <h3 className="label">Latest Animes</h3>
      </div>
      <Table heads={table_heads} items={table_items}></Table>
      <div className="tabel-pagination">
        <ul>
          <li className="pages-ticks">
            <button data-page={page} className="pagination-btn page-btn">
              {page}
            </button>
          </li>
          {dots.map((item) => item)}
          <li className="pages-ticks">
            <button data-page={amount_pages} className="pagination-btn page-btn">
              {amount_pages}
            </button>
          </li>
        </ul>
      </div>
    </div>
  );
};

export default AnalyticsAnimesTable;

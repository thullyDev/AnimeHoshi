import React from "react";
import Table from "../../../widgets/table/table";

interface Items {
  id: number;
  profile_image: string;
  username: string;
  email: string;
  deleted: boolean;
  disabled: boolean;
}

interface Pages {
  amount_pages: number;
  page: number;
}

interface AnalyticsUsersTableProps {
  items: Items[];
  pages: Pages;
}

const heads = ["profile_image", "username", "email", "status"];

const AnalyticsUsersTable: React.FC<AnalyticsUsersTableProps> = ({ items, pages }) => {
  const table_heads = heads.map((item, index) => (
    <th className="table-head users-head" key={index}>
      {item}
    </th>
  ));
  const table_items = items.map((item, index) => {
    const { id, profile_image, username, email, deleted, disabled } = item;
    return (
      <>
        <tr className="table-row user-row" key={index}>
          <td className="table-item user-item">
            <img src={profile_image} alt={username} title={username} className="profile-image" />
          </td>
          <td className="table-item user-item">
            <p className="username-tick">{username}</p>
          </td>
          <td className="table-item user-item">
            <p className="email-tick">{email}</p>
          </td>
          <td className="table-item user-item">
            <p className={!deleted ? "status-tick active" : "status-tick remove"}>{!deleted ? "active" : "inactive"}</p>
          </td>
          <td className="table-item user-item">
            <button className="table-btn disable" data-disabled={disabled} data-id={id} data-key={index}>
              disable
            </button>
          </td>
          <td className="table-item user-item">
            <button className="table-btn delete" data-deleted={deleted} data-id={id} data-key={index}>
              delete
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

  const { page, amount_pages } = pages;

  return (
    <div className="table-con users-table-con">
      <div className="table-label">
        <h3 className="label">Latest Users</h3>
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

export default AnalyticsUsersTable;

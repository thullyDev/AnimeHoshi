import Table from "../../../widgets/table/table";

interface Admins {
  id: number;
  profile_image: string;
  username: string;
  email: string;
  deleted: boolean;
}

interface AdminsTableProps {
  admins: Admins[];
}

const heads = [
  "profile", 
  "username", 
  "email", 
  "status",
  ];

const AdminsTable: React.FC<AdminsTableProps> = ({ admins }) => {
  const table_heads = heads.map((item) => (
    <th className="table-head admins-head">
      {item}
    </th>
  ));
  const table_admins = admins.map((item, index) => {
    const { profile_image, email, username, deleted } = item
    return (
      <>
        <tr className="table-row admin-row" key={index}>
          <td className="table-item admin-item">
            <p className="profile-image-tick">
              <img src={profile_image} alt={username} title={username} className="profile-image" />
            </p>
          </td>
          <td className="table-item admin-item">
            <p className="username-tick">{username}</p>
          </td>
          <td className="table-item admin-item">
            <p className="email-tick">{email}</p>
          </td>
          <td className="table-item admin-item">
            <p className={!deleted ? "status-tick active" : "status-tick remove"}>{!deleted ? "active" : "inactive"}</p>
          </td>
          <td className="table-item anime-item">
            <button className="table-btn disable" data-deleted={deleted} data-key={index}>
              delete
            </button>
          </td>
        </tr>
      </>
    );
  });


  return (
    <div className="table-con admins-table-con">
      <Table items={table_admins} heads={table_heads} ></Table>
    </div>
  );
};

export default AdminsTable;

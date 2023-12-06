import AdminsModal from "./AdminModal";
import AdminsTable from "./adminsTable";

const admins_count = 1;
const admins_items = [
  {
    id: 0,
    username: "animeGirl",
    email: "animegirl@gmail.com",
    profile_image: "https://i.pinimg.com/564x/07/d4/34/07d434bcb00e39c8e8d25df1cc89a333.jpg",
    deleted: false,
  },
  {
    id: 1,
    username: "animeBoy",
    email: "animeBoy@gmail.com",
    profile_image: "https://i.pinimg.com/236x/ef/e9/73/efe97322d26afdbb85e03c52b1db7c10.jpg",
    deleted: false,
  },
  {
    id: 2,
    username: "Megumi",
    email: "megumi@gmail.com",
    profile_image: "https://i.pinimg.com/736x/02/05/28/020528711a47abd638ed5ee670cc4705.jpg",
    deleted: false,
  },
  {
    id: 3,
    username: "Gojo",
    email: "gojo@gmail.com",
    profile_image: "https://i.pinimg.com/736x/50/c4/bd/50c4bdba9bbe22a46733edbdb55b65a2.jpg",
    deleted: false,
  },
  {
    id: 4,
    username: "Kenji",
    email: "kenji@gmail.com",
    profile_image: "https://i.pinimg.com/236x/85/42/bb/8542bb42f5e7369e953049fa14ba5170.jpg",
    deleted: false,
  },
  {
    id: 5,
    username: "sky",
    email: "sky@gmail.com",
    profile_image: "https://i.pinimg.com/236x/1d/da/d3/1ddad3615c85b90dccd31c2b5fbcb5a1.jpg",
    deleted: false,
  },
  {
    id: 6,
    username: "vi",
    email: "viCatlin@gmail.com",
    profile_image: "https://i.pinimg.com/236x/e5/60/0e/e5600eac05e07ae2e74492d5060130f0.jpg",
    deleted: false,
  },
  {
    id: 7,
    username: "jayce",
    email: "jayce@gmail.com",
    profile_image: "https://i.pinimg.com/236x/61/b9/59/61b9595898d45dd9e20261a5864455c6.jpg",
    deleted: false,
  },
  {
    id: 8,
    username: "jinx",
    email: "jinx@gmail.com",
    profile_image: "https://i.pinimg.com/236x/7b/48/e1/7b48e1b4561ab7962b582ca20f78e914.jpg",
    deleted: false,
  },
  {
    id: 9,
    username: "nightGirl",
    email: "nightGirl@gmail.com",
    profile_image: "https://i.pinimg.com/236x/79/94/e7/7994e7bfaa011c4c4d0675e09cea4d3a.jpg",
    deleted: false,
  },
];

const Admins = () => {
  return (
    <>
      <div className="inner-con inner-main-content">
        <div className="admins-con">
          <div className="admins-count-add-con">
            <div className="admins-count-con">
              <p className="admins-label">Admins:</p>
              <span className="admin-count">{admins_count}</span>
            </div>
            <div className="add-admin-btn-con">
              <button type="button" className="add-admin">
                Add Admin
              </button>
            </div>
          </div>
          <div className="admins-table-con">
            <AdminsTable admins={admins_items} />
          </div>
        </div>
        <AdminsModal />
      </div>
    </>
  );
};

export default Admins;

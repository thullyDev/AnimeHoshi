import AnalyticsCard from "./analyticsCard";
import AnalyticsUsersTable from "./analyticsUsersTable";
import AnalyticsAnimesTable from "./analyticsAnimesTable";

const analytics_items = [
  { numbers: 0, label: "Users" },
  { numbers: 0, label: "Admins" },
  { numbers: 0, label: "Weekly Views" },
  { numbers: 0, label: "Scripts" },
];

const users_items = [
  {
    id: 0,
    username: "animeGirl",
    email: "animegirl@gmail.com",
    profile_image: "https://i.pinimg.com/564x/07/d4/34/07d434bcb00e39c8e8d25df1cc89a333.jpg",
    deleted: false,
    disabled: false,
  },
  {
    id: 1,
    username: "animeBoy",
    email: "animeBoy@gmail.com",
    profile_image: "https://i.pinimg.com/236x/ef/e9/73/efe97322d26afdbb85e03c52b1db7c10.jpg",
    deleted: false,
    disabled: false,
  },
  {
    id: 2,
    username: "Megumi",
    email: "megumi@gmail.com",
    profile_image: "https://i.pinimg.com/736x/02/05/28/020528711a47abd638ed5ee670cc4705.jpg",
    deleted: false,
    disabled: false,
  },
  {
    id: 3,
    username: "Gojo",
    email: "gojo@gmail.com",
    profile_image: "https://i.pinimg.com/736x/50/c4/bd/50c4bdba9bbe22a46733edbdb55b65a2.jpg",
    deleted: false,
    disabled: false,
  },
  {
    id: 4,
    username: "Kenji",
    email: "kenji@gmail.com",
    profile_image: "https://i.pinimg.com/236x/85/42/bb/8542bb42f5e7369e953049fa14ba5170.jpg",
    deleted: false,
    disabled: false,
  },
  {
    id: 5,
    username: "sky",
    email: "sky@gmail.com",
    profile_image: "https://i.pinimg.com/236x/1d/da/d3/1ddad3615c85b90dccd31c2b5fbcb5a1.jpg",
    deleted: false,
    disabled: false,
  },
  {
    id: 6,
    username: "vi",
    email: "viCatlin@gmail.com",
    profile_image: "https://i.pinimg.com/236x/e5/60/0e/e5600eac05e07ae2e74492d5060130f0.jpg",
    deleted: false,
    disabled: false,
  },
  {
    id: 7,
    username: "jayce",
    email: "jayce@gmail.com",
    profile_image: "https://i.pinimg.com/236x/61/b9/59/61b9595898d45dd9e20261a5864455c6.jpg",
    deleted: false,
    disabled: false,
  },
  {
    id: 8,
    username: "jinx",
    email: "jinx@gmail.com",
    profile_image: "https://i.pinimg.com/236x/7b/48/e1/7b48e1b4561ab7962b582ca20f78e914.jpg",
    deleted: false,
    disabled: false,
  },
  {
    id: 9,
    username: "nightGirl",
    email: "nightGirl@gmail.com",
    profile_image: "https://i.pinimg.com/236x/79/94/e7/7994e7bfaa011c4c4d0675e09cea4d3a.jpg",
    deleted: false,
    disabled: false,
  },
];

const animes_items = [
  {
    id: 0,
    title: "Sousou no Frieren",
    slug: "sousou-no-frieren",
    poster_url: "https://cdn.myanimelist.net/images/anime/1015/138006.jpg",
    disabled: false,
  },
  {
    id: 1,
    title: "Sousou no Frieren 2",
    slug: "sousou-no-frieren-2",
    poster_url: "https://cdn.myanimelist.net/images/anime/1015/138006.jpg",
    disabled: false,
  },
  {
    id: 2,
    title: "Sousou no Frieren 3",
    slug: "sousou-no-frieren-3",
    poster_url: "https://cdn.myanimelist.net/images/anime/1015/138006.jpg",
    disabled: false,
  },
  {
    id: 3,
    title: "Sousou no Frieren 4",
    slug: "sousou-no-frieren-4",
    poster_url: "https://cdn.myanimelist.net/images/anime/1015/138006.jpg",
    disabled: false,
  },
  {
    id: 4,
    title: "Sousou no Frieren 5",
    slug: "sousou-no-frieren-5",
    poster_url: "https://cdn.myanimelist.net/images/anime/1015/138006.jpg",
    disabled: false,
  },
  {
    id: 5,
    title: "Sousou no Frieren 6",
    slug: "sousou-no-frieren-6",
    poster_url: "https://cdn.myanimelist.net/images/anime/1015/138006.jpg",
    disabled: false,
  },
  {
    id: 6,
    title: "Sousou no Frieren 7",
    slug: "sousou-no-frieren-7",
    poster_url: "https://cdn.myanimelist.net/images/anime/1015/138006.jpg",
    disabled: false,
  },
  {
    id: 7,
    title: "Sousou no Frieren 8",
    slug: "sousou-no-frieren-8",
    poster_url: "https://cdn.myanimelist.net/images/anime/1015/138006.jpg",
    disabled: false,
  },
  {
    id: 8,
    title: "Sousou no Frieren 9",
    slug: "sousou-no-frieren-9",
    poster_url: "https://cdn.myanimelist.net/images/anime/1015/138006.jpg",
    disabled: false,
  },
  {
    id: 9,
    title: "Sousou no Frieren 10",
    slug: "sousou-no-frieren-10",
    poster_url: "https://cdn.myanimelist.net/images/anime/1015/138006.jpg",
    disabled: false,
  },
];

const page = 1;
const amount_pages = 100;
const pages = {
  page,
  amount_pages,
};

const Dashboard = () => {
  return (
    <>
      <div className="inner-con inner-main-content">
        <div className="cards-con">
          {analytics_items.map((item, index) => (
            <AnalyticsCard label={item.label} numbers={item.numbers} key={index} />
          ))}
        </div>
        <div className="tables-con">
          <AnalyticsUsersTable pages={pages} items={users_items}></AnalyticsUsersTable>
          <AnalyticsAnimesTable pages={pages} items={animes_items}></AnalyticsAnimesTable>
        </div>
      </div>
    </>
  );
};

export default Dashboard;

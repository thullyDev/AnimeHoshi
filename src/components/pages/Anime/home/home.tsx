import Header from "../../sections/adminHeader/adminHeader";
// import Footer from "../../sections/footer/footer"; // Uncomment if you have a Footer component
// import Menu from "../../sections/menu/menu";

const Home = () => {
  return (
    <>
      <div className="side-bar-con">{/*<Menu></Menu>*/}</div>
      <div className="right-con">
        <Header></Header>
      </div>
    </>
  );
};

export default Home;

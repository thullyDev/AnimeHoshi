import React from "react";
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import AdminRouter from "./components/routers/adminRouter/adminRouter";

const App = () => {
  return (
    <Router>
      <Routes>
        <Route path="/admin/*" element={<AdminRouter />} />
        {/*<Route path="/user/*" element={<UserRouter />} />*/}
      </Routes>
    </Router>
  );
};

export default App;

import React from "react";
import { BrowserRouter as Router, Route, Routes } from "react-router-dom";
import AdminLayout from "../../layouts/adminLayout/adminLayout";
import Dashboard from "../../pages/dashboard/dashboard";
import Scripts from "../../pages/scripts/scripts";
import General from "../../pages/general/general";

const AdminRouter = () => {
  return (
    <>
      <Routes>
        <Route path="dashboard" element={<AdminLayout title="Dashboard" element={<Dashboard />} />} />
        <Route path="scripts" element={<AdminLayout title="Scripts" element={<Scripts />} />} />
        <Route path="general" element={<AdminLayout title="General Settings" element={<General />} />} />
      </Routes>
    </>
  );
};

export default AdminRouter;

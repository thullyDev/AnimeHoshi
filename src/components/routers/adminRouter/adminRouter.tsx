// @ts-ignore
import { BrowserRouter as Router, Route, Routes } from "react-router-dom";
// Rest of your code
import AdminLayout from "../../pages/admin/adminLayout";
import Dashboard from "../../pages/admin/dashboard/dashboard";
import Scripts from "../../pages/admin/scripts/scripts";
import General from "../../pages/admin/general/general";
import Advance from "../../pages/admin/advance/advance";
import Admins from "../../pages/admin/admins/admins";

const AdminRouter = () => {
  return (
    <>
      <Routes>
        <Route path="dashboard" element={<AdminLayout title="Dashboard" element={<Dashboard />} />} />
        <Route path="scripts" element={<AdminLayout title="Scripts" element={<Scripts />} />} />
        <Route path="general" element={<AdminLayout title="General" element={<General />} />} />
        <Route path="advance" element={<AdminLayout title="Advance" element={<Advance />} />} />
        <Route path="admins" element={<AdminLayout title="Admins" element={<Admins />} />} />
      </Routes>
    </>
  );
};

export default AdminRouter;

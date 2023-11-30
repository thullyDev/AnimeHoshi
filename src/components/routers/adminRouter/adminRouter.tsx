import React from 'react';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import Dashboard from '../../pages/dashboard/dashboard';
import AdminFooter from '../../sections/adminFooter/adminFooter';
import Header from '../../sections/adminHeader/adminHeader';
import Menu from '../../sections/menu/menu';

const menu_items = [
  { path: '/admin/dashboard', label: 'dashboard' },
  { path: '/admin/scripts', label: 'scripts' },
  { path: '/admin/users', label: 'users' },
  { path: '/admin/general', label: 'general' },
  { path: '/admin/advanced', label: 'advanced' },
];

const AdminRouter = () => {
  return (
    <>
      <main className="dark-theme">
        <div className="side-bar-con">
          <Menu items={menu_items}></Menu>
        </div>
        <div className="right-con">
          <Header></Header>
          <section className="main-content">
            <Routes>
              <Route path="dashboard" element={<Dashboard />} />
            </Routes>
          </section>
          <AdminFooter></AdminFooter>
        </div>
      </main>
    </>
  );
};

export default AdminRouter;

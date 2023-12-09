import React from "react";

interface TableProps {
  items: React.ReactNode;
  heads: React.ReactNode;
}

const Table: React.FC<TableProps> = ({ items, heads }) => {
  return (
    <table>
      <thead>
        <tr>{heads}</tr>
      </thead>
      <tbody>
        <tr>{items}</tr>
      </tbody>
    </table>
  );
};

export default Table;

interface TableProps {
  items: any;
  heads: any;
}

const Table: React.FC<TableProps>  = ({ items, heads }) => {
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

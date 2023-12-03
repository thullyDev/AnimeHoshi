const Table = ({ items, heads }) => {
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

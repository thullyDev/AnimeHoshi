import React from "react";

interface SaveBtnProps {
  className: string;
}

const SaveBtn: React.FC<SaveBtnProps> = ({ className }) => {
  return (
    <div className="save-btn-con">
      <button className={"save-btn " + className}>save</button>
    </div>
  );
};

export default SaveBtn;

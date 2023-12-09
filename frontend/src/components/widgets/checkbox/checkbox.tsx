import Input from "../input/input";

interface CheckBoxProps {
  className: string;
  value: boolean;
  name: string;
}

// css for the checkbox https://codepen.io/d3uceY/pen/GRzBRKB
const CheckBox: React.FC<CheckBoxProps> = ({ className, value, name }) => {
  return (
    <>
      <div className="checkbox-con">
        <Input type="checkbox" value={value} className={`checkbox ${className}`} name={name} id={`checkbox-${name}`} />
        <label htmlFor={`checkbox-${name}`}></label>
      </div>
    </>
  );
};

export default CheckBox;

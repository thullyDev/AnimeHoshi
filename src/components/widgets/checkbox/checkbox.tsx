import Input from "../input/input";

interface CheckBoxProps {
  className: string;
  value: boolean;
  key: number;
  name: string;
}

// css for the checkbox https://codepen.io/d3uceY/pen/GRzBRKB
const CheckBox: React.FC<CheckBoxProps> = ({ className, value, key, name }) => {
  return (
    <>
      <div className="checkbox-con">
        <Input type="checkbox" value={value} className={`checkbox ${className}`} name={name} id={`checkbox-${key}`} />
        <label htmlFor={`checkbox-${key}`}></label>
      </div>
    </>
  );
};

export default CheckBox;

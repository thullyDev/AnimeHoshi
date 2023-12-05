import Input from "../../../widgets/input/input";

interface SettingsInputFieldProps {
  id: any;
  value: string;
  type: string;
  name: string;
}

const SettingsInputField: React.FC<SettingsInputFieldProps> = ({ id, value, type, name }) => {
  return (
      <div className="settings-input-con">
        <Input className="settings-input" name={name} value={value} id={id} type={type} />
      </div>
    )
};

export default SettingsInputField;

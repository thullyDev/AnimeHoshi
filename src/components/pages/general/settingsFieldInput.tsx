interface SettingsInputFieldProps {
  id: string;
  value: string;
  type: string;
}

const SettingsInputField: React.FC<SettingsInputFieldProps> = ({ id, value, type }) => {
  let input_field =
    type == "field" ? (
      <textarea className="settings-input" data-changed="false" data-value={value} value={value} />
    ) : (
      <input className="settings-input" type={type} id={id} date-name={id} data-value={value} data-changed="false" />
    );

  return <div className="settings-input-con">{input_field}</div>;
};

export default SettingsInputField;

interface SettingsImageContainerProps {
  id: string;
  value: string; // Assuming value is also a string, adjust the type if it's different
}

const SettingsImageContainer: React.FC<SettingsImageContainerProps> = ({ id, value }) => {
  return (
    <div className="image-setting-con site-logo-setting-con">
      <div className="image-con">
        <img src={value} alt={id} className="settings-image" />
      </div>
    </div>
  );
};

export default SettingsImageContainer;

interface SettingsImageContainerProps {
  id: string;
  value: string;
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

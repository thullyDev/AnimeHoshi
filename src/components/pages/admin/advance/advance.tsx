import CheckBox from "../../../widgets/checkbox/checkbox";
import SaveBtn from "../saveBtn";

const settings = [
  { key: "maintanence", value: false },
  { key: "adblocker_detection", value: true },
  { key: "alert", value: true },
  { key: "authentication", value: true },
  { key: "anime", value: true },
  { key: "watch", value: true },
  { key: "watch_togather", value: true },
  { key: "user", value: true },
  { key: "schedule", value: true },
  { key: "features", value: true },
  { key: "footer", value: true },
  { key: "landing", value: true },
  { key: "donation", value: true },
  { key: "socials", value: true },
  { key: "contact", value: true },
  { key: "dark_mode", value: true },
];

const Advance = () => {
  return (
    <>
      <div className="inner-con inner-main-content">
        <div className="inputs-con">
          {settings.map((item) => {
            const { key, value } = item;

            return (
              <div className="input-con">
                <div className="setting-label-con">
                  <p className="setting-label">{key.replace("_", " ")}</p>
                </div>
                <CheckBox name={key} value={value} className="settings-input" />
              </div>
            );
          })}
        </div>
        <SaveBtn className="advance-save"></SaveBtn>
      </div>
    </>
  );
};

export default Advance;

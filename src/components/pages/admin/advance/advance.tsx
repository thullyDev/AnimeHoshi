import CheckBox from "../../../widgets/checkbox/checkbox";
// import Input from "../../../widgets/input/input";

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
];

const Advance = () => {
  return (
    <>
      <div className="inner-con inner-main-content">
        <div className="inputs-con">
          {settings.map((item, index) => {
            const { key, value } = item;

            return (
              <div className="input-con">
                <div className="setting-label-con">
                  <p className="setting-label">{key.replace("_", " ")}</p>
                </div>
                <CheckBox key={index} name={key} value={value} className="settings-input" />
              </div>
            );
          })}
        </div>
        <div className="save-btn-con">
          <button className="save-btn">save</button>
        </div>
      </div>
    </>
  );
};

export default Advance;

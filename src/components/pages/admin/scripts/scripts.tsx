import ScriptField from "./scriptField";
import { slugify } from "../../../../resources/utilities";

const head_scripts = [
  {
    label: "global head",
    value: "",
  },
  {
    label: "home head",
    value: "",
  },
  {
    label: "landing head",
    value: "",
  },
  {
    label: "filter head",
    value: "",
  },
  {
    label: "profile head",
    value: "",
  },
  {
    label: "anime head",
    value: "",
  },
  {
    label: "watch head",
    value: "",
  },
  {
    label: "watch_together_browsing head",
    value: "",
  },
  {
    label: "watch_together_anime head",
    value: "",
  },
];
const foot_scripts = [
  {
    label: "global foot",
    value: "",
  },
  {
    label: "home foot",
    value: "",
  },
  {
    label: "landing foot",
    value: "",
  },
  {
    label: "filter foot",
    value: "",
  },
  {
    label: "profile foot",
    value: "",
  },
  {
    label: "anime foot",
    value: "",
  },
  {
    label: "watch foot",
    value: "",
  },
  {
    label: "watch_together_browsing foot",
    value: "",
  },
  {
    label: "watch_together_anime foot",
    value: "",
  },
];
const ads_scripts = {
  global: [
    {
      label: "top_advertisement",
      value: "",
      height: "",
    },
    {
      label: "bottom_advertisement",
      value: "",
      height: "",
    },
  ],
  landing: [
    {
      label: "middle_advertisement",
      value: "",
      height: "",
    },
  ],
  watch: [
    {
      label: "under_player_advertisement",
      value: "",
      height: "",
    },
    {
      label: "under_suggestions_advertisement",
      value: "",
      height: "",
    },
  ],
};

const Scripts = () => {
  return (
    <>
      <div className="inner-con inner-main-content">
        <div className="scripts-container">
          <div className="outer-scripts-con">
            <div className="scripts-label-con">
              <p className="scripts-label">Head Scripts</p>
            </div>
            <div className="scripts-con head-scripts-con">
              {head_scripts.map((item, index) => (
                <ScriptField label={item.label} value={item.value} key={index}></ScriptField>
              ))}
            </div>
          </div>
          <div className="outer-scripts-con">
            <div className="scripts-label-con">
              <p className="scripts-label">Foot Scripts</p>
            </div>
            <div className="scripts-con foot-scripts-con">
              {foot_scripts.map((item, index) => (
                <ScriptField label={item.label} value={item.value} key={index}></ScriptField>
              ))}
            </div>
          </div>
          <div className="outer-scripts-con">
            <div className="scripts-label-con">
              <p className="scripts-label">Ads Scripts</p>
            </div>
            <div className="scripts-con foot-scripts-con">
              {Object.entries(ads_scripts).flatMap(([key, ads_items]) =>
                ads_items.map((item) => {
                  const { label, value, height } = item;
                  const show_label = key + "_" + label;

                  return (
                    <>
                      <ScriptField label={show_label} value={value}></ScriptField>
                      <div className="ad-fluid-input-con">
                        <div className="fluid-input-con">
                          <input
                            type="number"
                            value={height}
                            placeholder="height"
                            data-slug={slugify(show_label)}
                            className="fluid-input"
                          />
                        </div>
                      </div>
                    </>
                  );
                }),
              )}
            </div>
          </div>
        </div>
        <div className="scripts-save-btn-con save-btn-con">
          <button type="button" className="save" data-type="scripts">
            save{" "}
            <i
              className="fas fa-save"
              style={{
                fontSize: "15px",
                margin: "0 5px",
              }}
            ></i>
          </button>
        </div>
      </div>
    </>
  );
};

export default Scripts;

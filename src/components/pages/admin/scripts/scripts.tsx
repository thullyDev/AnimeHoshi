import ScriptField from "./scriptField";
import { slugify } from "../../../../resources/utilities";
import SaveBtn from "../saveBtn";

const head_scripts = [
  {
    label: "global_head",
    value: "",
  },
  {
    label: "home_head",
    value: "",
  },
  {
    label: "landing_head",
    value: "",
  },
  {
    label: "filter_head",
    value: "",
  },
  {
    label: "profile_head",
    value: "",
  },
  {
    label: "anime_head",
    value: "",
  },
  {
    label: "watch_head",
    value: "",
  },
  {
    label: "watch_together_browsing_head",
    value: "",
  },
  {
    label: "watch_together_anime_head",
    value: "",
  },
];
const foot_scripts = [
  {
    label: "global_foot",
    value: "",
  },
  {
    label: "home_foot",
    value: "",
  },
  {
    label: "landing_foot",
    value: "",
  },
  {
    label: "filter_foot",
    value: "",
  },
  {
    label: "profile_foot",
    value: "",
  },
  {
    label: "anime_foot",
    value: "",
  },
  {
    label: "watch_foot",
    value: "",
  },
  {
    label: "watch_together_browsing_foot",
    value: "",
  },
  {
    label: "watch_together_anime_foot",
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
                      <div className="ads-script-field-con">
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
                      </div>
                    </>
                  );
                }),
              )}
            </div>
          </div>
        </div>
        <SaveBtn className="script-save"></SaveBtn>
      </div>
    </>
  );
};

export default Scripts;

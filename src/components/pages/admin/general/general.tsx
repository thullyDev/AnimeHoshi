import SettingsImageContainer from "./settingsImageContainer";
import SettingsInputField from "./settingsFieldInput";
import SaveBtn from "../saveBtn";

const images = [
  {
    key: "site_logo",
    value: "/static/images/site-logo.png",
  },
  {
    key: "favicon_logo",
    value: "/static/images/favicon.png",
  },
  {
    key: "alert",
    value: "/static/images/gifs/alert.gif",
  },
  {
    key: "maintenance",
    value: "/static/images/gifs/maintenance.gif",
  },
  {
    key: "empty",
    value: "/static/images/gifs/empty.gif",
  },
];

const inputs = [
  {
    value: "AnimeHoshi",
    key: "site_name",
  },
  {
    value: "admin@animehoshi.com",
    key: "email",
  },
  {
    value: "Watch Anime On AnimeHoshi For No ads | AnimeHoshi",
    key: "title",
  },
  {
    value:
      "AnimeHoshi is a vibrant online platform offering a diverse collection of anime content for free streaming. With an extensive library spanning genres and popular titles, AnimeHoshi provides enthusiasts with an immersive experience. User-friendly navigation and high-quality playback make it a go-to destination for anime lovers seeking free, accessible entertainment.",
    key: "site_description",
    type: "field",
  },
];

const socials = [
  {
    value: "https://discord.com/",
    key: "discord",
  },
  {
    value: "https://twitter.com/",
    key: "twitter",
  },
  {
    value: "https://reddit.com/",
    key: "reddit",
  },
  {
    value: "https://ko-fi.com/",
    key: "donate",
  },
];

const General = () => {
  return (
    <>
      <div className="inner-con inner-main-content">
        <div className="text-inputs-con">
          {inputs.map((item, index) => {
            const { key, value, type } = item;
            return (
              <div key={index} className="text-input-con">
                <div className="settings-input-label-con">
                  <label htmlFor={key} className="label-con">
                    {key.replace("_", " ")}
                  </label>
                </div>
                <SettingsInputField type={type ?? "text"} name={key} id={index} value={value}></SettingsInputField>
              </div>
            );
          })}
        </div>
        <div className="images-settings-con">
          {images.map((item, index) => {
            const { key, value } = item;
            return (
              <div key={index} className="image-input-con">
                <label htmlFor={key} className="settings-input-label">
                  <span className="image-label">{key.replace("_", " ")}</span>
                  <SettingsImageContainer id={key} value={value}></SettingsImageContainer>
                </label>
                <SettingsInputField type="file" name={key} id={index} value={value}></SettingsInputField>
              </div>
            );
          })}
        </div>
        <div className="socials-settings-con">
          {socials.map((item, index) => {
            const { key, value } = item;
            return (
              <div key={index} className="text-input-con">
                <div className="settings-input-label-con">
                  <label htmlFor={key} className="label-con">
                    {key.replace("_", " ")}
                  </label>
                </div>
                <SettingsInputField type="text" name={key} id={index} value={value}></SettingsInputField>
              </div>
            );
          })}
        </div>
        <SaveBtn className="general-save"></SaveBtn>
      </div>
    </>
  );
};

export default General;

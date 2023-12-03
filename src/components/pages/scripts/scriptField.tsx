import { slugify } from "../../../resources/utilities";

const ScriptField = ({ label, value }) => {
  const slug = slugify(label);
  const valid_label = label.replaceAll("_", " ");
  return (
    <>
      <div className="field-con inner-con">
        <div className="field-label-con">
          <p className="field-label">{valid_label}</p>
        </div>
        <div className="field-text-con">
          <textarea className="field" data-slug={slug} value={value} />
        </div>
      </div>
    </>
  );
};

export default ScriptField;

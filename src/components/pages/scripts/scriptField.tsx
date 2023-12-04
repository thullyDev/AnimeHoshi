import React from "react";
import { slugify } from "../../../resources/utilities";

interface ScriptFieldProps {
  label: string;
  value: string;
}

const ScriptField: React.FC<ScriptFieldProps> = ({ label, value }) => {
  const slug = slugify(label);
  const valid_label = label.replace("_", " ");
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

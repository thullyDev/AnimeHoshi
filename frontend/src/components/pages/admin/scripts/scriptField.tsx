import React from "react";
import { slugify, replaceAll } from "../../../../resources/utilities";

interface ScriptFieldProps {
  label: string;
  value: string;
}

const ScriptField: React.FC<ScriptFieldProps> = ({ label, value }) => {
  const slug = slugify(label);
  const valid_label = replaceAll(label, "_", " ");
  return (
    <>
      <div className="field-con inner-con">
        <div className="field-label-con">
          <p className="field-label">{valid_label}</p>
        </div>
        <div className="field-text-con">
          <textarea className="field settings-input" data-name={slug} value={value} />
        </div>
      </div>
    </>
  );
};

export default ScriptField;

import { slugify } from "../../../resources/utilities";

interface InputProps {
  id: string;
  className: string;
  value: any;
  type: string;
  name: string;
}

const Input: React.FC<InputProps> = ({ className, type, value, id, name }) => {
  const slug = slugify(name)
  const input_field =
    type == "field" ? (
      <textarea className={className} data-changed="false" id={id} date-name={slug} data-value={value} value={value} />
    ) : (
      <input className={className} type={type} id={id} date-name={slug} data-value={value} data-changed="false" />
    );

  return input_field
};

export default Input;

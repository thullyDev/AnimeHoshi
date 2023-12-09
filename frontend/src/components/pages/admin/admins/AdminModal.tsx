import Input from "../../../widgets/input/input";
import Modal from "../../../widgets/modal/modal";
const AdminsModal = () => {
  const text = "Enter Site key to confirm";
  const html = (
    <div className="submit-con">
      <Input type="text" name="site-key-input" className="site-key-input" id="site-key-input" value="" />
      <button type="button" className="site-key-submit-btn">
        submit
      </button>
    </div>
  );

  return <Modal className="site-key-modal" text={text} html={html} />;
};

export default AdminsModal;

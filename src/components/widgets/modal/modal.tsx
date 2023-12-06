interface ModalProps {
  className: string;
  text: string;
  html: React.ReactNode;
}

const Modal: React.FC<ModalProps> = ({ className, text, html }) => {
  return (
    <div className={`${className} modal-con`}>
      <div className="text-con">
        <p className="text">{text}</p>
      </div>
      <div className="modal-html-con">{html}</div>
    </div>
  );
};

export default Modal;

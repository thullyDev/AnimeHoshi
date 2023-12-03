const AnalyticsCard = ({ label, numbers }) => {
  return (
    <div className={`analytic-card card ${label.replaceAll(" ", "-").toLowerCase()}`}>
      <div className="inner-con">
        <div className="left-side numbers-text-con">
          <span className="ticks-numbers">
            <p className="numbers">{numbers}</p>
          </span>
          <span className="ticks-label">
            <p className="label">{label}</p>
          </span>
        </div>
      </div>
    </div>
  );
};

export default AnalyticsCard;

interface AnalyticsCardProps {
  label: string;
  numbers: number;
}

const AnalyticsCard: React.FC<AnalyticsCardProps> = ({ label, numbers }) => {
  return (
    <div className={`analytic-card card ${label.replace(" ", "-").toLowerCase()}`}>
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

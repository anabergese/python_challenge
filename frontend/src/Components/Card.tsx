import React from "react";
import { ICardProps } from "../Types/TypesIndex";

const Card: React.FC<ICardProps> = ({ title, children }) => {
  return (
    <div className="column is-half">
      <div className="card">
        <p
          className="card-header-title has-background-warning has-text-black-ter is-capitalized"
          data-testid="card-title"
        >
          {title}
        </p>
        <div className="card-content">{children}</div>
      </div>
    </div>
  );
};

export default Card;

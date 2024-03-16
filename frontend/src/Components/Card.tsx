import React from "react";
import { ICardProps } from "../Types/TypesIndex";

const Card: React.FC<ICardProps> = ({
  title,
  children,
  columnClassName,
  cardClassName,
  headerClassName,
}) => {
  return (
    <div className={`column ${columnClassName}`}>
      <div className={`card ${cardClassName}`}>
        <p
          className={`is-capitalized ${headerClassName}`}
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

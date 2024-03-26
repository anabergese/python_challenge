/**
 * @jest-environment jsdom
 */

import React from "react";
import { render, screen } from "@testing-library/react";
import Card from "../Components/Card";

describe("Card component", () => {
  const title = "Test Title";
  const childrenContent = "Test Children Content";
  const columnClassName = "test-column-class";
  const cardClassName = "test-card-class";
  const headerClassName = "test-header-class";

  it("renders with correct title and children", () => {
    render(
      <Card
        title={title}
        columnClassName={columnClassName}
        cardClassName={cardClassName}
        headerClassName={headerClassName}
      >
        {childrenContent}
      </Card>
    );

    expect(screen.getByTestId("card-title").textContent).toBe(title);
    expect(screen.getByText(childrenContent).textContent).toBe(childrenContent);
  });
});

/**
 * @jest-environment jsdom
 */

import React from "react";
import { render, screen, waitFor } from "@testing-library/react";
import App from "../Components/App.tsx";

test("use jsdom in this test file", () => {
  const element = document.createElement("div");
  expect(element).not.toBeNull();
});

test("renders App component", async () => {
  render(<App />);

  await waitFor(() => {
    const appTitle = screen.getByTestId("app-title");
    expect(appTitle.textContent).toBe("The Blog");
  });
});

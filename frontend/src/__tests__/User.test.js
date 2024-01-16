/**
 * @jest-environment jsdom
 */

import React from "react";
import { render, screen } from "@testing-library/react";
import { MemoryRouter, Route, Routes } from "react-router-dom";
import User from "../Components/User.tsx";

jest.mock("react-router-dom", () => ({
  ...jest.requireActual("react-router-dom"),
  useLocation: jest.fn(),
}));

describe("User component", () => {
  test("renders User component with user data", () => {
    const mockUserData = {
      id: 1,
      name: "John Doe",
      username: "john_doe",
      email: "john.doe@example.com",
      phone: "123-456-7890",
      website: "www.example.com",
    };

    // Mock useLocation hook to provide user data
    const mockUseLocation = {
      state: {
        userData: mockUserData,
      },
    };
    require("react-router-dom").useLocation.mockImplementation(
      () => mockUseLocation
    );

    render(
      <MemoryRouter initialEntries={["/users/1"]}>
        <Routes>
          <Route path="/users/:id" element={<User />} />
        </Routes>
      </MemoryRouter>
    );

    const commentName = screen.getByTestId("user-name");
    expect(commentName.textContent).toBe("John Doe");
  });
});

import { render, screen, fireEvent } from "@testing-library/react";
import { MemoryRouter } from "react-router-dom";
import LoginPage from "./LoginPage";

jest.mock("react-router-dom", () => ({
  ...jest.requireActual("react-router-dom"),
  useNavigate: jest.fn(),
}));

describe("LoginPage Navigation", () => {
  test("Clicking Sign Up navigates to /signup", () => {
    const mockNavigate = require("react-router-dom").useNavigate();
    
    render(
      <MemoryRouter>
        <LoginPage />
      </MemoryRouter>
    );

    // Find Sign Up button
    fireEvent.click(screen.getByText("Sign Up"));

    // See if /signup was called
    expect(mockNavigate).toHaveBeenCalledWith("/signup");
  });
});

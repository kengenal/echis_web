import React from "react";
import { render } from "@testing-library/react";
import App from "./App";

describe("AppView", () => {
  const { container } = render(<App />);

  it("can render html", () => {
    const navbar = container.getElementsByClassName("navbar");
    expect(navbar[0].className).toBe("navbar");
  });
});

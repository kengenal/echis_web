import React from "react";
import { render, RenderResult } from "@testing-library/react";
import Navigation from "./Navigation";

describe("NavigationComponent", () => {
  let wrapper: RenderResult;

  beforeEach(() => {
    wrapper = render(<Navigation />);
  });

  it("can render html", () => {
    const navbar = wrapper.container.getElementsByClassName("navbar");
    expect(navbar[0].className).toBe("navbar");
  });

  it("have logo", () => {
    const brand = wrapper.container.getElementsByClassName("navbar__brand");
    expect(brand.length).toBeGreaterThan(0);
  });

  it("can render dropdown", () => {
    const dropdown = wrapper.container.getElementsByClassName("dropdown");
    expect(dropdown.length).toBeGreaterThan(0);
  });
});

import React from "react";
import { render, RenderResult } from "@testing-library/react";
import { MemoryRouter } from 'react-router-dom'
import Dropdown from "./Dropdown";

describe("DropdownComponent", () => {
  let wrapper: RenderResult;

  const dropdownData = {
    header: {
      label: "Share",
      icon: "share",
    },
    items: [
      { link: "/share/playlist", label: "Playlist", icon: "queue_music" },
      { link: "/share/songs", label: "Songs", icon: "music_note" },
    ],
  };

  beforeEach(() => {
    wrapper = render(
      <MemoryRouter>
        <Dropdown dropdown={dropdownData} />
      </MemoryRouter>
    );
  });

  it("can render html", () => {
    const dropdown = wrapper.container.getElementsByClassName("dropdown");
    expect(dropdown[0].className).toBe("dropdown");
  });
});

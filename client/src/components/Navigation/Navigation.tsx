import { BrowserRouter as Router, Link } from "react-router-dom";
import React from "react";

import "./Navigation.scss";

import Dropdown from "../Dropdown/Dropdown";

export default function Navigation() {
  const dropdownShare = {
    header: {
      label: "Share",
      icon: "share",
    },
    items: [
      { link: "/share/playlist", label: "Playlist", icon: "queue_music" },
      { link: "/share/songs", label: "Songs", icon: "music_note" },
    ],
  };

  const dropdownAccound = {
    header: {
      image:
        "https://cdn.discordapp.com/avatars/301796703277940737/c88c68adcb5b04db54ee1a8eb6081fc0.webp?size=1024",
    },
    items: [{ link: "/account/logout", label: "Logout", icon: "exit_to_app" }],
  };

  return (
    <Router>
      <nav className="navbar">
        <Link className="navbar__brand" to="/">
          <img
            className="navbar__image"
            alt="back to home page"
            src="https://cdn.discordapp.com/widget-avatars/EK8101DeRW0t0Jeze4L3YapbumoaRLCDWs5bV9Ntqf0/O7VJsYBxprw5iDc2BUlaItDtc-whuW9HwNy8Jm9qH-eal5gw3LhlSfTeOOqcpH0_JJSCgLWwyP9v-Nei_8kvTW-bohSs7JnQyfoUI_-q7osntUmM2H4LsFUPHOma1TCW2VNZqoG0x8xhmA"
          />
        </Link>

        <ul className="navbar__list mr-auto">
          <li className="navbar__list-item">
            <Dropdown dropdown={dropdownShare} />
          </li>
        </ul>
        <ul className="navbar__list">
          <li className="navbar__list-item">
            <Dropdown dropdown={dropdownAccound} />
          </li>
        </ul>
      </nav>
    </Router>
  );
}

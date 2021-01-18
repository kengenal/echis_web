import { BrowserRouter as Router, Link } from "react-router-dom";
import React from "react";

import "./Navigation.scss";

import Dropdown from "../Dropdown/Dropdown";

export default function Navigation() {
  const dropdown = {
    header: {
      label: "Share",
      icon: "share",
    },
    items: [
      { link: "/share/playlist", label: "Playlist", icon: "queue_music" },
      { link: "/share/songs", label: "Songs", icon: "music_note" },
    ],
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

        <ul className="navbar__list">
          <li className="navbar__list-item">
            <Dropdown dropdown={dropdown} />
          </li>
          {/* <ul className="navbar-nav ">
            <li className="nav-item">
              <a className="nav-link" href="sda">
                <i className="fa fa-bell">
                  <span className="badge badge-info">11</span>
                </i>
                Test
              </a>
            </li>
            <li className="nav-item">
              <a className="nav-link" href="dasd">
                <i className="fa fa-globe">
                  <span className="badge badge-success">11</span>
                </i>
                Test
              </a>
            </li>
          </ul> */}
          {/* <form className="form-inline my-2 my-lg-0">
            <input
              className="form-control mr-sm-2"
              type="text"
              placeholder="Search"
              aria-label="Search"
            />
            <button
              className="btn btn-outline-success my-2 my-sm-0"
              type="submit"
            >
              Search
            </button>
          </form> */}
        </ul>
      </nav>
    </Router>
  );
}

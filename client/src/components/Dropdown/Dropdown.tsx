/* eslint-disable @typescript-eslint/no-explicit-any */
import "./Dropdown.scss";
import MaterialIcon from "@material/react-material-icon";
import React, { useState } from "react";
import { Link } from "react-router-dom";
import { DropdownList } from "./Dropdown.model";

export default function Dropdown({ dropdown }: { dropdown: DropdownList }) {
  const [toggle, setToggle] = useState(false);
  const container = React.createRef<HTMLDivElement>();

  document.addEventListener("mousedown", handleClickOutside);

  function handleClickOutside(event: any) {
    if (container.current && !container.current.contains(event.target)) {
      setToggle(() => false);
    }
  }

  return (
    <div className="dropdown" ref={container}>
      <button
        type="button"
        className="dropdown__toggle"
        onClick={() => setToggle((_toggle) => !_toggle)}
        data-toggler="toggler"
      >
        {dropdown.header.icon ? (
          <MaterialIcon
            className="dropdown__icon"
            icon={dropdown.header.icon}
            title="Share"
          />
        ) : (
          <img
            data-toggler="toggler"
            className="navbar__image"
            src={dropdown.header.image}
            alt="discord profile avatar"
          />
        )}

        {dropdown.header.label ? dropdown.header.label : ""}
      </button>
      <ul className={`dropdown__menu ${toggle && "dropdown__menu--active"}`}>
        {dropdown.items.map(({ link, label, icon }) => (
          <li className="dropdown__menu-item" key={label}>
            {icon && <MaterialIcon icon={icon} title={label} />}
            <Link className="dropdown__link" to={link}>
              {label}
            </Link>
          </li>
        ))}
      </ul>
    </div>
  );
}

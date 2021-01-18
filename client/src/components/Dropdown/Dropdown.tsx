import "./Dropdown.scss";
import MaterialIcon from "@material/react-material-icon";
import React, { useState } from "react";
import { Link } from "react-router-dom";
import { DropdownList } from "./Dropdown.model";

export default function Dropdown({ dropdown }: { dropdown: DropdownList }) {
  const [toggle, setToggle] = useState(false);

  return (
    <div className="dropdown">
      <button
        type="button"
        className="dropdown__toggle"
        onClick={() => setToggle((_toggle) => !_toggle)}
      >
        <MaterialIcon
          className="dropdown__icon"
          icon={dropdown.header.icon}
          title="Share"
        />
        {dropdown.header.label}
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

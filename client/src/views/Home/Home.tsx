import React from "react";
import "./Home.scss";
import MaterialIcon from "@material/react-material-icon";

export default function Home() {
  return (
    <>
      <div className="container">
        <h1 className="container__header">Welcome Undero</h1>
        <hr />
        <div className="card">
          <h2 className="card__header">Your data</h2>
          <ul className="card__list">
            <li className="card__list-item">
              <MaterialIcon icon="fingerprint" title="discord_id" />
              <strong className="card__list-label">discord_id:</strong>
              <span className="card__list-txt">301796703277940737</span>
            </li>

            <li className="card__list-item">
              <MaterialIcon icon="account_box" title="discord_id" />
              <strong className="card__list-label"> username:</strong>
              <span className="card__list-txt">Undero</span>
            </li>

            <li className="card__list-item">
              <MaterialIcon icon="perm_identity" title="discord_id" />
              <strong className="card__list-label">permissions:</strong>
              <span className="card__list-txt">
                Groovy|BOT|share|Echis|music|DEVS|Support|registered|Admin
              </span>
            </li>

            <li className="card__list-item">
              <MaterialIcon icon="image" title="discord_id" />
              <strong className="card__list-label">avatar:</strong>
              <span className="card__list-txt">
                https://cdn.discordapp.com/avatars/301796703277940737/c88c68adcb5b04db54ee1a8eb6081fc0.webp?size=1024
              </span>
            </li>

            <li className="card__list-item">
              <MaterialIcon icon="schedule" title="discord_id" />
              <strong className="card__list-label">exp:</strong>{" "}
              <span className="card__list-txt">1611064031</span>
            </li>
          </ul>
        </div>
      </div>
    </>
  );
}

import React from "react";
import "./Home.scss";

export default function Home() {
  return (
    <>
      <div className="container">
        <h1 className="container__header">Welcome Undero</h1>
        <hr />
        <div className="card">
          <h2 className="card__header">Your data</h2>
          <ul className="card__list">
            <li className="card__list-item">discord_id: 301796703277940737</li>

            <li className="card__list-item">username: Undero</li>

            <li className="card__list">
              permissions:
              Groovy|BOT|share|Echis|music|DEVS|Support|registered|Admin
            </li>

            <li className="card__list">
              avatar:
              https://cdn.discordapp.com/avatars/301796703277940737/c88c68adcb5b04db54ee1a8eb6081fc0.webp?size=1024
            </li>

            <li className="card__list">exp: 1611064031</li>
          </ul>
        </div>
      </div>
    </>
  );
}

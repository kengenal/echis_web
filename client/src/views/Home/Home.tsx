/* eslint-disable @typescript-eslint/no-explicit-any */
import React from "react";
import { useParams } from "react-router-dom";
import "./Home.scss";
import MaterialIcon from "@material/react-material-icon";
import { useFetch } from "react-async";
import enviromant from "../../enviroment";

function splitPermission(permissions: string[]) {
  let string = "";

  for (const permission of permissions ?? []) {
    string += `${permission}|`;
  }

  return string;
}

export default function Home() {
  const { token }: { token: string } = useParams();
  const { data, error } = useFetch<any>(`${enviromant.API_URL}/auth`, {
    headers: { Authorization: `Bearer ${token}`, accept: "application/json" },
  });

  if (error) throw error;

  return (
    <>
      <div className="container">
        <h1 className="container__header">Welcome {data?.user?.username}</h1>
        <hr />
        <div className="card">
          <h2 className="card__header">Your data</h2>
          <ul className="card__list">
            <li className="card__list-item">
              <MaterialIcon icon="fingerprint" title="discord_id" />
              <strong className="card__list-label">discord_id:</strong>
              <span className="card__list-txt">{data?.user?.discord_id}</span>
            </li>

            <li className="card__list-item">
              <MaterialIcon icon="account_box" title="discord_id" />
              <strong className="card__list-label">username:</strong>
              <span className="card__list-txt">{data?.user?.username}</span>
            </li>

            <li className="card__list-item">
              <MaterialIcon icon="perm_identity" title="discord_id" />
              <strong className="card__list-label">permissions:</strong>
              <span className="card__list-txt">
                {splitPermission(data?.user?.permissions)}
              </span>
            </li>

            <li className="card__list-item">
              <MaterialIcon icon="image" title="discord_id" />
              <strong className="card__list-label">avatar:</strong>
              <span className="card__list-txt">{data?.user?.avatar}</span>
            </li>

            <li className="card__list-item">
              <MaterialIcon icon="schedule" title="discord_id" />
              <strong className="card__list-label">exp:</strong>
              <span className="card__list-txt">1611064031</span>
            </li>
          </ul>
        </div>
      </div>
    </>
  );
}

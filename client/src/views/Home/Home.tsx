/* eslint-disable @typescript-eslint/no-explicit-any */
import React from "react";
import { useParams } from "react-router-dom";
import "./Home.scss";
import MaterialIcon from "@material/react-material-icon";
import { useFetch } from "react-async";
import enviromant from "../../enviroment";
import UserData from "./Home.model";

export default function Home() {
  const { token }: { token: string } = useParams();
  const { data, error } = useFetch<UserData>(`${enviromant.API_URL}/auth`, {
    headers: { Authorization: `Bearer ${token}`, accept: "application/json" },
  });

  if (error) throw error;

  localStorage.setItem("user_token", data?.token ?? "");
  localStorage.setItem("user_img", data?.user?.avatar ?? "");

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
                {data?.user?.permissions_str ?? ""}
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
              <span className="card__list-txt">{data?.user?.exp}</span>
            </li>
          </ul>
        </div>
      </div>
    </>
  );
}

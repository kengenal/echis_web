import React from "react";
import Table from "../../../components/Table/Table";

import "./Playlist.scss";

export default function Playlist() {
  const items = [
    [1, "123", "User1", "Some-service", "NOW", true],
    [1, "123", "User1", "Some-service", "NOW", true],
    [1, "123", "User1", "Some-service", "NOW", true],
  ];
  const headers = ["", "Playlist ID", "User", "Service", "Added", "Active"];

  return (
    <>
      <div className="container">
        <h1 className="container__header">Playlist</h1>
        <Table headers={headers} items={items} />
      </div>
    </>
  );
}

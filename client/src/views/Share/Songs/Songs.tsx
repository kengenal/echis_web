import React from "react";
import Table from "../../../components/Table/Table";

export default function Songs() {
  const items = [
    [
      1,
      "123",
      "150322",
      "Everyday",
      "All For What",
      6492294924,
      "2020-09-10 19:57:25",
      "Kengenal",
      "sssss",
      true,
    ],
  ];
  const headers = [
    "",
    "Cover",
    "Rank",
    "Title",
    "Album",
    "Playlist ID",
    "Added",
    "Added by",
    "Source",
    "Send",
  ];

  return (
    <>
      <div className="container">
        <h1 className="container__header">Songs</h1>
        <Table headers={headers} items={items} />
      </div>
    </>
  );
}

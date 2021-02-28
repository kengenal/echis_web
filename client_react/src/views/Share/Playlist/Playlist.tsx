/* eslint-disable @typescript-eslint/ban-types */
import React, { useState } from "react";
import { useFetch } from "react-async";
import ReactPaginate from "react-paginate";
import Table from "../../../components/Table/Table";
import enviromant from "../../../enviroment";
import PlaylistData from "./Playlist.model";

import "./Playlist.scss";

export default function Playlist() {
  const token = localStorage.getItem("user_token");
  const [page, setPage] = useState(1);

  const { data, error } = useFetch<PlaylistData>(
    `${enviromant.API_URL}/share/playlist/${page}`,
    {
      headers: { Authorization: `Bearer ${token}`, accept: "application/json" },
    }
  );

  if (error) throw error;

  const headers = [
    "",
    "ID",
    "Service",
    "Added",
    "Active",
    "Playlist ID",
    "Record ID",
    "User",
  ];

  function pageChange({ selected }: { selected: number }) {
    setPage(selected);
  }

  return (
    <>
      <div className="container">
        <h1 className="container__header">Playlist</h1>
        <Table headers={headers} items={data?.playlists ?? []} />
        {(data?.results as Number) > 10 ? (
          <ReactPaginate
            pageCount={data?.results ?? 1 / 10}
            pageRangeDisplayed={5}
            marginPagesDisplayed={1}
            onPageChange={pageChange}
            containerClassName="pagination"
          />
        ) : (
          ""
        )}
      </div>
    </>
  );
}

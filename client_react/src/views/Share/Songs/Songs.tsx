/* eslint-disable @typescript-eslint/ban-types, no-underscore-dangle, no-param-reassign, lines-around-directive, @typescript-eslint/no-unused-expressions */
import React, { useState } from "react";
import { useFetch } from "react-async";

import ReactPaginate from "react-paginate";

import Table from "../../../components/Table/Table";
import enviromant from "../../../enviroment";
import SongsData from "./Songs.model";

import "./Songs.scss";

export default function Songs() {
  const token = localStorage.getItem("user_token");
  const [page, setPage] = useState(1);

  const { data, error } = useFetch<SongsData>(
    `${enviromant.API_URL}/share/songs/${page}`,
    {
      headers: { Authorization: `Bearer ${token}`, accept: "application/json" },
    }
  );

  if (error) throw error;

  const headers = [
    "",
    "Added by",
    "Added",
    "Album",
    "Api",
    "Artist",
    "Cover",
    "Created",
    "Shared",
    "Rank",
    "Title",
  ];

  function pageChange({ selected }: { selected: number }) {
    setPage(selected);
  }

  function getItems(items: SongsData["songs"]) {
    3;
    return items.map((item) => {
      delete item?._id;
      delete item?.song_id;
      delete item?.record_id;
      delete item?.playlist_id;

      return item;
    });
  }

  return (
    <>
      <div className="container">
        <h1 className="container__header">Songs</h1>
        <Table headers={headers} items={getItems(data?.songs ?? [])} />
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

/* eslint-disable react/no-array-index-key */
/* eslint-disable @typescript-eslint/no-explicit-any */
import React from "react";
import "./Table.scss";

export default function Table({
  items,
  headers,
}: {
  items: any[][];
  headers: string[];
}) {
  return (
    <table className="table">
      <thead className="table__head">
        <tr className="table__row">
          {headers.map((header, i: number) => (
            <th key={`${i}th`} className="table__header">
              {header}
            </th>
          ))}
        </tr>
      </thead>
      <tbody className="table__body">
        {items.map((item: string[], i: number) => (
          <tr className="table__row" key={`${i}tr`}>
            {item.map((row: string, j: number) => (
              <td key={`${j}td`} className="table__cell">
                {row}
              </td>
            ))}
          </tr>
        ))}
      </tbody>
    </table>
  );
}

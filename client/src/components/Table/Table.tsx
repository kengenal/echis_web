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
          {headers.map((header) => (
            <th className="table__header">{header}</th>
          ))}
        </tr>
      </thead>
      <tbody className="table__body">
        {items.map((item: string[]) => (
          <tr className="table__row">
            {item.map((row: string) => (
              <td className="table__cell">{row}</td>
            ))}
          </tr>
        ))}
      </tbody>
    </table>
  );
}

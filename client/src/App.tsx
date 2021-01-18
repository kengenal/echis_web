import React from "react";
import Navigation from "./components/Navigation/Navigation";
import Router from "./router";

import "./index.scss";

export default function App() {
  return (
    <>
      <Router />
      <Navigation />
    </>
  );
}

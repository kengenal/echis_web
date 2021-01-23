import React from "react";
import { BrowserRouter, Route, Switch } from "react-router-dom";
import Navigation from "./components/Navigation/Navigation";

import "./index.scss";
import Home from "./views/Home/Home";
import Playlist from "./views/Share/Playlist/Playlist";
import Songs from "./views/Share/Songs/Songs";

export default function App() {
  return (
    <>
      <BrowserRouter>
        <Navigation />
        <Switch>
          <Route exact path="/" component={Home} />
          <Route path="/share/playlist" component={Playlist} />
          <Route path="/share/songs" component={Songs} />
        </Switch>
      </BrowserRouter>
    </>
  );
}

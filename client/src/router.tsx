import { BrowserRouter, Switch, Route } from "react-router-dom";
import React from "react";

export default function Router() {
  return (
    <BrowserRouter>
      <Switch>
        <Route path="/">{/* <Home /> */}</Route>
        <Route path="/share">
          <Route path="/playlists">{}</Route>
          <Route path="/songs">{}</Route>
        </Route>
      </Switch>
    </BrowserRouter>
  );
}

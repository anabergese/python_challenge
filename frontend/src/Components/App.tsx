import "../index.css";
import "bulma/css/bulma.min.css";
import { BrowserRouter, Routes, Route } from "react-router-dom";
import React, { lazy, Suspense } from "react";
import Hero from "./Hero";

const Posts = lazy(() => import("./Posts"));
const Post = lazy(() => import("./Post"));
const User = lazy(() => import("./User"));

const App = () => {
  return (
    <BrowserRouter>
      <Suspense
        fallback={
          <div className="loader-container">
            <div className="loader" />
          </div>
        }
      >
        <div className="App">
          <Hero />
          <Routes>
            <Route path="/" element={<Posts />} />
            <Route path="/posts/:id" element={<Post />} />
            <Route path="/users/:id" element={<User />} />
          </Routes>
        </div>
      </Suspense>
    </BrowserRouter>
  );
};

export default App;

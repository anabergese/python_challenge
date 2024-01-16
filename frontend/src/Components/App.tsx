import "../index.css";
import "bulma/css/bulma.min.css";
import { BrowserRouter, Routes, Route } from "react-router-dom";
import React, { lazy, Suspense } from "react";

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
          <section className="hero is-warning mb-4">
            <div className="hero-body">
              <p className="title" data-testid="app-title">
                The Blog
              </p>
              <p className="subtitle">Code Challenge</p>
            </div>
          </section>
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
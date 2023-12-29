import "./App.css";
import "bulma/css/bulma.min.css";
import Posts from "./Components/Posts";
import Post from "./Components/Post";
import User from "./Components/User";
import { BrowserRouter, Routes, Route } from "react-router-dom";

const App = () => {
  return (
    <BrowserRouter>
      <div className="App">
        <section className="hero is-warning mb-4">
          <div className="hero-body">
            <p className="title">The Blog</p>
            <p className="subtitle">Code Challenge</p>
          </div>
        </section>
        <Routes>
          <Route path="/" element={<Posts />} />
          <Route path="/posts/:id" element={<Post />} />
          <Route path="/users/:id" element={<User />} />
        </Routes>
      </div>
    </BrowserRouter>
  );
};

export default App;

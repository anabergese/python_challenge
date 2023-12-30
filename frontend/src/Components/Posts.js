import React from "react";
import { Link } from "react-router-dom";
import axios from "axios";
import { useState, useEffect } from "react";

const Posts = () => {
  const [posts, setPosts] = useState([]);

  useEffect(() => {
    const fetchData = async () => {
      try {
        const response = await axios.get("http://localhost:8000/posts/");
        setPosts(response.data);
      } catch (error) {
        console.error("Error fetching data:", error);
      }
    };

    fetchData();
  }, []);

  return (
    <div className="columns is-multiline">
      {!posts.length ? (
        <h1>Loading Posts</h1>
      ) : (
        posts.map((post) => (
          <div key={post.id} className="column is-half">
            <Link
              to={`/posts/${post.id}`}
              className="is-capitalized	is-size-5 has-text-dark"
            >
              {post.title}
            </Link>
          </div>
        ))
      )}
    </div>
  );
};

export default Posts;

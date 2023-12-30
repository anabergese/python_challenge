import React, { useState, useEffect } from "react";
import axios from "axios";
import { useParams } from "react-router-dom";
import { useNavigate } from "react-router-dom";
import Comments from "./Comments";

const Post = () => {
  const { id } = useParams();
  const [post, setPost] = useState(null);
  const [user, setUser] = useState(null);
  const navigate = useNavigate();

  useEffect(() => {
    const fetchData = async () => {
      try {
        const postResponse = await axios.get(
          `http://localhost:8000/post-with-comments/${id}`
        );
        setPost(postResponse.data);

        const userResponse = await axios.get(
          `http://localhost:8000/users/${postResponse.data.userId}`
        );
        setUser(userResponse.data);
      } catch (error) {
        console.error("Error fetching data:", error);
      }
    };

    fetchData();
  }, [id]);

  const handleClick = () => {
    navigate(`/users/${user.id}`, { state: { userData: user } });
  };

  return (
    <div>
      {post && user ? (
        <div>
          <div className="card">
            <div className="card-content has-background-light">
              <p className="title is-capitalized">{post.title}</p>
              <button className="subtitle btn-no-style" onClick={handleClick}>
                Created by: {user.name}
              </button>
              <div className="content is-capitalized">{post.body}</div>
            </div>
          </div>
          <Comments comments={post.comments} />
        </div>
      ) : (
        <p>Loading post details...</p>
      )}
    </div>
  );
};

export default Post;

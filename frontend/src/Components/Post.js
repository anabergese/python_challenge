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
    axios
      .get(`http://localhost:8000/post-with-comments/${id}`)
      .then((res) => {
        setPost(res.data);
        console.log(res.data);
        return axios.get(`http://localhost:8000/users/${res.data.userId}`);
      })
      .then((res) => {
        setUser(res.data);
      })
      .catch((err) => {
        console.log(err);
      });
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

import React, { useState, useEffect } from "react";
import { useParams } from "react-router-dom";
import { useNavigate } from "react-router-dom";
import Comments from "./Comments";
import { getUserDataById, getPostWithComments } from "../api";
import { IUser, IPost } from "../Types/TypesIndex";
import Card from "./Card";

const Post = () => {
  const { id: postId } = useParams();
  const [post, setPost] = useState(null as IPost | null);
  const [user, setUser] = useState(null as IUser | null);
  const [error, setError] = useState(null as string | null);
  const navigate = useNavigate();

  useEffect(() => {
    const fetchData = async () => {
      try {
        const postResponse = await getPostWithComments(postId);
        setPost(postResponse);

        const userData = await getUserDataById(postResponse.userId as number);
        setUser(userData);
      } catch (error) {
        console.error("Error fetching data:", error);
        setError("Inexistent post. Please try again.");
      }
    };

    fetchData();
  }, [postId]);

  const handleClick = () => {
    if (user) {
      navigate(`/users/${user.id}`, { state: { userData: user } });
    }
  };

  return (
    <div>
      {error ? (
        <p>Error: {error}</p>
      ) : post && user ? (
        <div>
          <Card
            title={post.title}
            headerClassName="title card-content has-background-light"
            cardClassName="card-content has-background-light"
          >
            <>
              <button
                className="subtitle btn-no-style"
                onClick={handleClick}
                disabled={!user}
              >
                Created by: {user?.name}
              </button>
              <div className="content is-capitalized">{post.body}</div>
            </>
          </Card>
          <Comments comments={post.comments || []} />
        </div>
      ) : (
        <p>Loading post details...</p>
      )}
    </div>
  );
};

export default Post;

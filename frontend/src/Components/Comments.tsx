import React from "react";
import { IComment } from "../Types/TypesIndex";

const Comments = ({ comments }: { comments: IComment[] }) => {
  if (!comments || !comments.length) {
    return (
      <>
        <h1 className="title is-2 mt-6 mb-5">Comments</h1>
        <p>No comments found</p>
      </>
    );
  }

  return (
    <>
      <h1 className="title is-2 mt-6 mb-5">Comments</h1>
      <div className="columns is-multiline">
        {comments.map((comment) => (
          <div className="column is-half" key={comment.id}>
            <div className="card">
              <p
                className="card-header-title has-background-warning has-text-black-ter is-capitalized"
                data-testid="comment-name"
              >
                {comment.name}
              </p>
              <div className="card-content">
                <div className="content is-capitalized">{comment.body}</div>
                <div className="content">Author: {comment.email}</div>
              </div>
            </div>
          </div>
        ))}
      </div>
    </>
  );
};

export default Comments;

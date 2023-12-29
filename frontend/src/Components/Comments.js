import React from "react";

const Comments = ({ comments }) => {
  return (
    <>
      <h1 className="title is-2 mt-6 mb-5">Comments</h1>
      <div className="columns is-multiline">
        {comments.map((comment) => (
          <div className="column is-half">
            <div className="card" key={comment.id}>
              <p className="card-header-title has-background-warning has-text-black-ter is-capitalized">
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

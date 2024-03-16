import React from "react";
import { IComment } from "../Types/TypesIndex";
import Card from "./Card";

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
          <Card
            title={comment.name}
            key={comment.id}
            headerClassName="card-header-title has-background-warning"
            columnClassName="is-half"
          >
            <>
              <div className="content is-capitalized">{comment.body}</div>
              <div className="content">Author: {comment.email}</div>
            </>
          </Card>
        ))}
      </div>
    </>
  );
};

export default Comments;

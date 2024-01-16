/**
 * @jest-environment jsdom
 */

import React from "react";
import { render, screen } from "@testing-library/react";
import { BrowserRouter as Router } from "react-router-dom";
import Comments from "../Components/Comments.tsx";

test("renders Comments component with comments", async () => {
  const mockComments = [
    {
      id: 1,
      postId: 1,
      name: "id labore ex et quam laborum",
      email: "Eliseo@gardner.biz",
      body: "laudantium enim quasi est quidem magnam voluptate ipsam eos\ntempora quo necessitatibus\ndolor quam autem quasi\nreiciendis et nam sapiente accusantium",
    },
    {
      id: 2,
      postId: 1,
      name: "quo vero reiciendis velit similique earum",
      email: "Jayne_Kuhic@sydney.com",
      body: "est natus enim nihil est dolore omnis voluptatem numquam\net omnis occaecati quod ullam at\nvoluptatem error expedita pariatur\nnihil sint nostrum voluptatem reiciendis et",
    },
  ];

  render(
    <Router>
      <Comments comments={mockComments} />
    </Router>
  );

  const commentName = screen.getAllByTestId("comment-name")[1];
  expect(commentName.textContent).toBe(
    "quo vero reiciendis velit similique earum"
  );
});

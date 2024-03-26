/**
 * @jest-environment jsdom
 */

import React from "react";
import { render, waitFor, screen } from "@testing-library/react";
import axios from "axios";
import { MemoryRouter, Route, Routes } from "react-router-dom";
import Post from "../Components/Post.tsx";

jest.mock("axios");

test("renders Posts component with posts", async () => {
  const mockPost = {
    id: 1,
    userId: 1,
    title: "sunt aut facere repellat",
    body: "quia et suscipit\nsuscipit recusandae consequuntur expedita et cum\nreprehenderit molestiae ut ut quas totam\nnostrum rerum est autem sunt rem eveniet architecto",
    comments: [
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
    ],
  };

  const mockUser = {
    id: 1,
    name: "John Doe",
    username: "john_doe",
    email: "john.doe@example.com",
    phone: "123-456-7890",
    website: "www.example.com",
  };

  axios.get.mockResolvedValueOnce({ data: mockPost });
  axios.get.mockResolvedValueOnce({ data: mockUser });

  render(
    <MemoryRouter initialEntries={["/posts/1"]}>
      <Routes>
        <Route path="/posts/:id" element={<Post />} />
      </Routes>
    </MemoryRouter>
  );

  await waitFor(() => {
    const postTitle = screen.getAllByTestId("card-title")[0];
    expect(postTitle.textContent).toBe(mockPost.title);
  });

  expect(axios.get).toHaveBeenCalledWith(
    `http://localhost:8000/post-with-comments/1`
  );
  expect(axios.get).toHaveBeenCalledWith(
    `http://localhost:8000/users/${mockPost.userId}`
  );
  expect(axios.get).toHaveBeenCalledTimes(2);
});

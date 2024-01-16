/**
 * @jest-environment jsdom
 */

import React from "react";
import { render, waitFor, screen } from "@testing-library/react";
import axios from "axios";
import { BrowserRouter as Router } from "react-router-dom";
import Posts from "../Components/Posts.tsx";

jest.mock("axios");

test("renders Posts component with posts", async () => {
  const mockPosts = [
    {
      id: 1,
      userId: 1,
      title:
        "sunt aut facere repellat provident occaecati excepturi optio reprehenderit",
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
    },
    {
      id: 2,
      userId: 1,
      title: "qui est esse",
      body: "est rerum tempore vitae\nsequi sint nihil reprehenderit dolor beatae ea dolores neque\nfugiat blanditiis voluptate porro vel nihil molestiae ut reiciendis\nqui aperiam non debitis possimus qui neque nisi nulla",
      comments: [
        {
          id: 6,
          postId: 2,
          name: "et fugit eligendi deleniti quidem qui sint nihil autem",
          email: "Presley.Mueller@myrl.com",
          body: "doloribus at sed quis culpa deserunt consectetur qui praesentium\naccusamus fugiat dicta\nvoluptatem rerum ut voluptate autem\nvoluptatem repellendus aspernatur dolorem in",
        },
        {
          id: 7,
          postId: 2,
          name: "repellat consequatur praesentium vel minus molestias voluptatum",
          email: "Dallas@ole.me",
          body: "maiores sed dolores similique labore et inventore et\nquasi temporibus esse sunt id et\neos voluptatem aliquam\naliquid ratione corporis molestiae mollitia quia et magnam dolor",
        },
      ],
    },
  ];

  axios.get.mockResolvedValueOnce({ data: mockPosts });

  render(
    <Router>
      <Posts />
    </Router>
  );

  await waitFor(() => {
    const postTitle = screen.getAllByTestId("posts-titles")[1];
    expect(postTitle.textContent).toBe("qui est esse");
  });

  expect(axios.get).toHaveBeenCalledWith("http://localhost:8000/posts/");
  expect(axios.get).toHaveBeenCalledTimes(1);
});

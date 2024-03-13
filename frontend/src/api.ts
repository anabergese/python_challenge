import axios from "axios";

export const getPostWithComments = async (postId: any) => {
  try {
    const postResponse = await axios.get(
      `http://localhost:8000/post-with-comments/${postId}`
    );
    return postResponse.data;
  } catch (error) {
    console.error("Error fetching post data:", error);
    throw new Error("Failed to fetch post data");
  }
};

export const getUserDataById = async (userId: any) => {
  try {
    const userResponse = await axios.get(
      `http://localhost:8000/users/${userId}`
    );
    return userResponse.data;
  } catch (error) {
    console.error("Error fetching user data:", error);
    throw new Error("Failed to fetch user data");
  }
};

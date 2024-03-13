import axios from "axios";

export const getUserDataById = async (userId: number) => {
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

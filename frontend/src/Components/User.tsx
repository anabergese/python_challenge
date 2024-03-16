import React from "react";
import { useLocation } from "react-router-dom";
import Card from "./Card";

const User = () => {
  const location = useLocation();
  const { userData } = location.state || {};

  if (!userData) {
    throw new Error("No user data found");
  }

  return (
    <div className="columns is-multiline">
      <Card
        title={userData.name}
        headerClassName="card-header-title has-background-warning has-text-black-ter is-capitalized"
        columnClassName="is-half"
      >
        <>
          <div className="content is-capitalized">
            Username: {userData.username}
          </div>
          <div className="content is-capitalized">Name: {userData.name}</div>
          <div className="content is-capitalized">Email: {userData.email}</div>
          <div className="content is-capitalized">Phone: {userData.phone}</div>
          <div className="content is-capitalized">
            Website: {userData.website}
          </div>
        </>
      </Card>
    </div>
  );
};

export default User;

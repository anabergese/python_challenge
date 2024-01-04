import React from "react";
import { useLocation } from "react-router-dom";

const User = () => {
  const location = useLocation();
  const { userData } = location.state || {};

  if (!userData) {
    throw new Error("No user data found");
  }

  return (
    <div className="columns is-multiline">
      <div className="column is-half">
        {userData ? (
          <div>
            <div className="card" key={userData.id}>
              <p className="card-header-title has-background-warning has-text-black-ter is-capitalized">
                {userData.name}
              </p>
              <div className="card-content">
                <div className="content is-capitalized">
                  Username: {userData.username}
                </div>
                <div className="content is-capitalized">
                  Name: {userData.name}
                </div>
                <div className="content is-capitalized">
                  Email: {userData.email}
                </div>
                <div className="content is-capitalized">
                  Phone: {userData.phone}
                </div>
                <div className="content is-capitalized">
                  Website: {userData.website}
                </div>
              </div>
            </div>
          </div>
        ) : (
          <p>Loading user...</p>
        )}
      </div>
    </div>
  );
};

export default User;

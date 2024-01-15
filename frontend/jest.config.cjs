module.exports = {
  testEnvironment: "jsdom",
  transform: {
    "^.+\\.jsx?$": "babel-jest",
    "^.+\\.tsx?$": "ts-jest",
  },
  moduleNameMapper: {
    "\\.(css|less|scss|sass)$": "identity-obj-proxy",
  },
  testRegex: "(/__tests__/.*|(\\.|/)(test|spec))\\.jsx?$",
  moduleFileExtensions: ["js", "jsx", "json", "node", "ts", "tsx"],
};

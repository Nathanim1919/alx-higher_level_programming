const request = require("request");

const url = process.argv[2];

request.get(url, (error, response) => {
   console.log("code: ", response.statusCode);
});

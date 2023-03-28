const express = require("express");
var cors = require("cors");
const app = express();

app.use(cors());
app.use(express.json());
app.use(express.urlencoded({ extended: true }));

var mysql = require("mysql");

var connection = mysql.createConnection({
  host: "35.238.175.158",
  user: "root",
  password: "2412",
  database: "artist",
});

connection.connect(function (err) {
  if (err) throw err;
  console.log("Connected!");
});

app.get("/", (req, res) => {
  res.send("Server on port 3000");
});

app.post("/add", (req, res) => {
  console.log(`INSERT INTO songs (artist, song) VALUES ('${req.body.artist}', '${req.body.song}')`)
  var sql = connection.query(
  `INSERT INTO songs (artist, song) VALUES ('${req.body.artist}', '${req.body.song}')`,

  function (error, result) {
    if (error) throw error;
    res.send(JSON.stringify(result));
  }
  );
});

var server = app.listen(3000, function () {
  var port = server.address().port;
  console.log("Server on port %s", port);
});
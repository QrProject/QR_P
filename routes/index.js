var express = require('express');
const mysql   = require('mysql');
const dbconfig = require('../bin/database.js');

const conn = mysql.createConnection(dbconfig);

var app = express();
//var router = express.Router();

//app.use(bodyParser.urlencoded({ extended: false }));
app.use(express.json())

/* GET home page. */
app.get('/', function(req, res, next) {
  res.render('index', { title: 'Express' });
});


module.exports = app;

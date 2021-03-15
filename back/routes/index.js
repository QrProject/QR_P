const express = require('express');
const mysql   = require('mysql');
const dbconfig = require('../bin/database.js');

const conn = mysql.createConnection(dbconfig);

const app = express();

app.use(express.json())


app.get('/', function(req, res, next) {
  res.render('index', { title: 'Express' });
});


module.exports = app;

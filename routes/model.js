const express = require('express');
const mysql   = require('mysql');
const dbconfig = require('../bin/database.js');

const connection = mysql.createConnection(dbconfig);

const router = express.Router();

router.get('/', (req, res) => {
    res.json({
        success: true,
        fail:false
    });
});

router.get('/list', (req, res) => {
  connection.query('SELECT * from pmp_model', (error, rows) => {
    if (error)
      throw error;
    else
    {
      res.json(rows);
    }});
  });


module.exports = router;

const express = require('express');
const mysql   = require('mysql');
const dbconfig = require('../bin/database.js');

const conn = mysql.createConnection(dbconfig);

var app = express();

app.use(express.json())

app.get('/', (req, res) => {
    res.json({
        success: true,
        fail:false
    });
});


//제조 번호 요청에 따른 응답 (메인화면 페이지)
app.get('/:pmp_num', (req, res) => {
var sql =
           `SELECT A.PMP_MANU_NUM, A.PMP_MODEL_NM, A.PMP_TYPE, A.BORE, A.HEAD, A.CAPACITY
                  ,B.VISIT_DATE, B.VISIT_ENGINEER_NM, B.VISIT_ENGINEER_PHONE, B.REPAIR_CONTENTS
                  ,C.SITE_NUM, C.SITE_NM, C.SITE_ADDR
                  ,D.MANU_COMP_NM, D.MANU_COMP_PHONE, D.DELI_COMP_NM, D.DELI_COMP_PHONE, D.MANU_DT, D.FREE_SRV_ST_DT, D.FREE_SRV_END_DT, D.PAID_SRV_COMP_NM, D.PAID_SRV_COMP_PHONE
            FROM  PMP_MODEL A
            LEFT OUTER JOIN PMP_REPAIR_HISTORY B ON A.PMP_MANU_NUM = B.PMP_MANU_NUM
            LEFT OUTER JOIN SITE_INFO C ON A.PMP_MANU_NUM = C.PMP_MANU_NUM
            LEFT OUTER JOIN SITE_DETAIL_INFO D ON A.PMP_MANU_NUM = D.PMP_MANU_NUM
            WHERE A.PMP_MANU_NUM = ?`;

  var params = mysql.format(sql,[req.params.pmp_num]);

  conn.query(params,(err, data) => {
      if(err) { console.error(err);  res.status(500).send('Internal Server Error'); return;}

          if(data == 0)
          {
            res.json('{result:count 0}');
            return;
          }

           res.json(data);
      });

  });

app.post('/add', (req, res) => {

    var pmp_manu_num = req.body.pmp_manu_num;
    var pmp_model_nm = req.body.pmp_model_nm;
    var pmp_type = req.body.pmp_type;
    var bore = req.body.bore;
    var head = req.body.head;
    var capacity = req.body.capacity;

    console.log(req.body);

    var sql = `INSERT INTO PMP_MODEL (PMP_MANU_NUM,PMP_MODEL_NM,PMP_TYPE,BORE,HEAD,CAPACITY,CREATE_DT) VALUES (?,?,?,?,?,?,now())`;

    var params = [pmp_manu_num, pmp_model_nm, pmp_type, bore, head, capacity];

    conn.query(sql, params, function(err, result, fields){
        if(err) {
          res.status(500).send('Internal Server Error');
          return;
        }
        res.json('{result:ok}');
        //res.redirect('/topic/'+result.insertId);//새로운 데이터가 insert될때, 자동으로 생기는 id가 있는데, query 함수의 두번째 인자인 result 객체에서 insertId라는 키로 그 값인 id를 찾을 수 있다. 그것을 통하여 새로 생긴 데이터의 화면을 바로 띄워줄 수 있다.
    });
});

module.exports = app;

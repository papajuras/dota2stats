/// <reference path="../../typings/main/ambient/mongodb/mongodb.d.ts" />

'use strict';
import {GenerateCombination} from "./model/generate";
import {MongoClient} from "mongodb";
import {DbHandler} from "./model/DbHandler";


// declare var require, console : Console;
//
// var express = require('express');
// var app_port = 8080;
//
// var app = express();
// app.use(express.static('www'));
// app.listen(app_port);
//
// console.log("Listening at http://localhost:" + app_port + "/");

var mongoClient = new MongoClient();

mongoClient.connect('mongodb://localhost:27017/dotastatsdb', (error, db) => {
    if (error) {
        console.log(error);
    }
    
    // let dbUpdater = new DbHandler(db);
    // dbUpdater.initDb();

    var generateCombination = new GenerateCombination();
    var any = generateCombination.generate5v5TestData();
    console.log(any);


    // for (var i = 0; i < 25; i++) {
    //     dbUpdater.saveRecord({wacek: 123});
    // }

});



// GenerateCombination.generate2v2();

// Server app goes here




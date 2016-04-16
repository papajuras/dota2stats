import {Db} from "mongodb";
import {Collection} from "mongodb";
import {HERO_COUNT} from "../dota2Consts";
export class DbHandler {
    private collection2v2: Collection;

    constructor(private db: Db) {
    }

    initDb() {
        this.collection2v2 = this.db.collection('2v2');
        this.collection2v2.createIndex({'rad0': 'number', 'rad1': 'number', 'dire0': 'number', 'dire1': 'number'});
    }

    saveRecord(record: {}): Promise  {
        return this.collection2v2.insertOne(record);

        // console.log(insertOne);
        // insertOne.then(res => {
        //     console.log('resolved');
        //     return '';
        // });

        // Promise.all([insertOne]).then();
    }

    createJson(rad0, rad1, dire0, dire1): Object {
        let res = {
            rad0: rad0,
            rad1: rad1,
            dire0: dire0,
            dire1: dire1
        };
        for (let i = 0; i < HERO_COUNT; i++) {
            res[i] = {win: 0, lose: 0};
        }
        return res;
    }
    
    async storeData(i, j, k, l): Promise {
        let object = this.createJson(i, j, k, l);
        return this.saveRecord(object);
    }

    listAll(): void {
    }
}
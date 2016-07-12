import {Db} from "mongodb";
import {Collection} from "mongodb";
import {HERO_COUNT} from "../dota2Consts";
export class DbHandler {
    private collection5v5: Collection;

    constructor(private db: Db) {
    }

    initDb() {
        this.collection5v5 = this.db.collection('5v5');
        this.collection5v5.createIndex({'r': 1, 'd': 1});
    }

    saveRecord(record: {}): Promise  {
        return this.collection5v5.insertOne(record);
    }
    
    async storeData(i, j, k, l): Promise {
        let object = this.createJson(i, j, k, l);
        return this.saveRecord(object);
    }

    listAll(): void {
    }
}
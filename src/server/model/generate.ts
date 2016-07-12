import {HERO_COUNT} from "../dota2Consts";
import {DbHandler} from "./DbHandler";
export class GenerateCombination {

    async generate2v2(dbHandler: DbHandler): void {
        let i: number, j: number;
        for (i = 0; i < HERO_COUNT - 1; i = i + 1) {
            for (j = i + 1; j < HERO_COUNT; j = j + 1) {
                this.generateOpposingTeam2v2(i, j, dbHandler);
            }
        }
    }

    async generateOpposingTeam2v2(i, j, dbHandler: DbHandler): void {
        let ii, jj: number;
        for (ii = 0; ii < HERO_COUNT - 1; ii = ii + 1) {
            if ([i, j].indexOf(ii) == -1) {
                for (jj = ii + 1; jj < HERO_COUNT; jj = jj + 1) {
                    if ([i, j].indexOf(jj) == -1) {
                        await dbHandler.storeData(i, j, ii, jj);
                    }
                }
            }
        }
    }
    
    generate5v5TestData() {
        let numberList = [];
        for (var i = 0; i < 82; i += 1) {
            numberList.push(i);
        }

        this.getCombinations(numberList);

        console.log('done')
    }

    private count: number = 0;
    private result = [];

    getCombinations(chars) {
        this.doGenerate([], chars);
    }

    async doGenerate(prefix: Array, chars) {
        if (prefix.length == 10) {
            this.count += 1;
            this.result.push(prefix);
            console.log(this.result);
            return;
        }

        if (this.count > 10) {
            return;
        }
        for (var i = 0; i < chars.length; i++) {
            await this.doGenerate(prefix.concat(chars[i]), chars.slice(i + 1));
        }
    }
}
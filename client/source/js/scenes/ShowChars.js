import Phaser from 'phaser';
import config from '../config';

export default class ShowChars extends Phaser.Scene {

    constructor() {
        super({key:"ShowChars"});
    }

    preload() {
        this.load.image('char_female_ranger', './assets/WomenRanger.png')
        this.load.image('char_men_ranger', './assets/MenRanger.png')
        this.load.image('char_female_strolth', './assets/WomanStrolth.png');
        this.load.image('char_men_strolth', './assets/MenStrolth.png');
        this.load.image('char_female_kuirk', './assets/FemaleWuick.png');
        this.load.image('char_men_kuirk', './assets/MenWuick.png');

        this.load.image('symbol_ranger', './assets/SymbolRanger.png');
        this.load.image('symbol_strolth', './assets/SymbolStrolth.png');
        this.load.image('symbol_kuirk', './assets/SymbolWuick.png');

        this.load.image('pirate', './assets/Pirat.png');
        // naves


    }

    async create() {
        let res = await this.getCharsInfo(this.sys.game._GENDER, this.sys.game._CLAN);

        if(res) {
            let clan = res.clan.name
            let playername = res.player.name;
            let ship1 = res.ship1.name;
            let ship2 = res.ship2.name;
            let ship3 = res.ship3.name;

            this.add.image(100, 100, `char_${gender}_${clan}`);
            this.add.text(100, 300, playername);
            this.add.image(400, 100, `symbol_${clan}`);
        }

        for(int i = 0; i < 4; i++) {
            this.load.image(100, (i+1)*100, 'pirate')
        }
    }

    async getCharsInfo(gender, clan) {
        await fetch(`${config.serverUrl}/get_group_of/${gender}/${clan}`)
            .then(res => res.json())
            .then(res => res);
    }
 
}
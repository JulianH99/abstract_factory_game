import Phaser from 'phaser';
import config from '../config';

export default class ShowChars extends Phaser.Scene {

    constructor() {
        super({key:"ShowChars"});
    }

    preload() {
        this.load.image('char_women_ranger', './assets/WomenRanger.png')
        this.load.image('char_men_ranger', './assets/MenRanger.png')
        this.load.image('char_women_strolth', './assets/WomenStrolth.png');
        this.load.image('char_men_strolth', './assets/MenStrolth.png');
        this.load.image('char_women_kuirk', './assets/WomenWuick.png');
        this.load.image('char_men_kuirk', './assets/MenWuick.png');

        this.load.image('symbol_ranger', './assets/SymbolRanger.png');
        this.load.image('symbol_strolth', './assets/SymbolStrolth.png');
        this.load.image('symbol_kuirk', './assets/SymbolWuick.png');

        this.load.image('pirate', './assets/Pirat.png');
        
        // naves
        this.load.image('agile', './assets/FirstModelQuick.png');
        this.load.image('heavy', './assets/FirstModelMiddle.png');
        this.load.image('smart', './assets/SecondModelBase.png');

    }

    async create() {
        let gender = this.sys.game._GENDER;
        let clan = this.sys.game._CLAN;
        let res = await fetch(`${config.serverUrl}/get_group_of/${gender}/${clan}`);
        res = await res.json();

        console.log(res);
        if(res) {
            let clan = res.clan.name
            let playername = res.player.name;
            let ship1 = res.ship1;
            let ship2 = res.ship2;
            let ship3 = res.ship3;

            this.renderShips(ship1, ship2, ship3);

            console.log(`char_${this.getGender(gender)}_${clan}`);
            this.add.image(100, 100, `char_${this.getGender(gender)}_${clan}`);
            this.add.text(50, 150, playername);
            this.add.image(400, 100, `symbol_${clan}`);
        }

        for(var i = 0; i < 4; i++) {
            this.add.image(600, (i+1)*100, 'pirate')
        }
    }

    async getCharsInfo(gender, clan) {
        await fetch(`${config.serverUrl}/get_group_of/${gender}/${clan}`)
            .then(res => res.json());
    }
    

    /**
     * 
     * @param {string} gender 
     * @returns {string}
     */
    getGender(gender) {
        return gender.toLowerCase() === 'male'? 'men':'women';
    }

    /**
     * 
     * @param  {...Object} ships 
     */
    renderShips(...ships) {
        ships.forEach((ship, index) => {
            let xPosition = (index + 1)*100 + 50*index
            this.add.image(xPosition, 300, ship.name);

            let keys = Object.keys(ship);

            let keyIndex = 0;
            keys.forEach((key) => {
                if(key !== 'name' && key !== 'id' && key !== 'accesories') {
                    this.add.text(xPosition - 50, 350 + (keyIndex*20) , `${key.toUpperCase()}:${ship[key]}`);
                    keyIndex += 1;
                }
            })
        })
    }
 
}
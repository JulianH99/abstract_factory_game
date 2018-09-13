import Phaser from 'phaser';
import config from '../config';

export default class ShowChars extends Phaser.Scene {

    constructor() {
        super({key:"ShowChars"});
    }

    preload() {
        // rangers
        this.load.image('WomenRanger', './assets/WomenRanger.png');
        this.load.image('MenRanger', './assets/MenRanger.png');

        // strolth
        this.load.image('WomanStrolth', './assets/WomenStrolth.png');
        this.load.image('MenStrolth', './assets/MenStrolth.png');

        // kuirk
        this.load.image('WomenKuirk', './assets/WomenKuirk.png');
        this.load.image('MenKuirk', './assets/MenKuirk.png');

        this.load.image('SymbolRanger', './assets/SymbolRanger.png');
        this.load.image('SymbolStrolth', './assets/SymbolStrolth.png');
        this.load.image('SymbolWuick', './assets/SymbolWuick.png');

        this.load.image('Pirate', './assets/Pirate.png');
        
        // naves
        this.load.image('Agile', './assets/FirstModelQuick.png');
        this.load.image('Heavy', './assets/FirstModelMiddle.png');
        this.load.image('Smart', './assets/SecondModelBase.png');

        // fondo
        this.load.image('fondo', './assets/fondo.png')

    }

    async create() {
        let gender = this.sys.game._GENDER;
        let clan = this.sys.game._CLAN;
        let res = await fetch(`${config.serverUrl}/get_group_of/${gender}/${clan}`);
        res = await res.json();

        let fondo = this.add.tileSprite(880, 550, 600, 600 ,'fondo');
        fondo.scaleY = 2.5;
        fondo.scaleX = 2.5;

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

        await this.getPirates();
    }

    async getCharsInfo(gender, clan) {
        await fetch(`${config.serverUrl}/get_group_of/${gender}/${clan}`)
            .then(res => res.json());
    }
    async getPirates() {
        let res = await fetch(`${config.serverUrl}/get_pirates/6`);
        res = await res.json();
        console.log(res);
        res.forEach((pirate, index) => {
            this.add.image(600, (index + 1)*100, 'pirate');
            this.add.image(700, (index + 1)*100, pirate.ship.name);
        })
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
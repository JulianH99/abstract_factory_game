import Phaser from 'phaser';
import config from '../config';

export default class ShowChars extends Phaser.Scene {

    constructor() {
        super({key:"ShowChars"});
    }

    preload() {
        // rangers
        this.load.image('WomanRanger', './assets/WomanRanger.png');
        this.load.image('ManRanger', './assets/ManRanger.png');

        // strolth
        this.load.image('WomanStrolth', './assets/WomanStrolth.png');
        this.load.image('ManStrolth', './assets/ManStrolth.png');

        // kuirk
        this.load.image('WomanKuirk', './assets/WomanKuirk.png');
        this.load.image('ManKuirk', './assets/ManKuirk.png');

        this.load.image('SymbolRanger', './assets/SymbolRanger.png');
        this.load.image('SymbolStrolth', './assets/SymbolStrolth.png');
        this.load.image('SymbolWuick', './assets/SymbolWuick.png');

        this.load.image('Pirate', './assets/Pirate.png');
        
        // naves
        this.load.image('Agile', './assets/FirstModelQuick.png');
        this.load.image('Heavy', './assets/FirstModelMiddle.png');
        this.load.image('Smart', './assets/SecondModelBase.png');

        // ropas
        this.load.image('ClothesMenRanger',  './assets/ClothesMenRanger.png');
        this.load.image('ClothesMenStrolth', './assets/ClothesMenStrolth.png');
        this.load.image('ClothesWomenRanger', './assets/ClothesWomenRanger.png');
        this.load.image('ClothesWomenStrolth', './assets/ClothesWomenStrolth.png');
        this.load.image('ClothesMenKuirk', './assets/ClothesWuickMen.png');
        this.load.image('ClothesWomenKuirk', './assets/ClothesWuickWomen.png');

        // bases
        this.load.image('ManModel', './assets/ManModel.png');
        this.load.image('WomanModel', './assets/WomanModel.png');

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
            let clan = res.clan.sprite;
            let playername = res.player.name;
            let ship1 = res.ship1;
            let ship2 = res.ship2;
            let ship3 = res.ship3;

            this.renderShips(ship1, ship2, ship3);

            console.log(`${clan}`);
            this.add.image(100, 100, res.player.base_sprite);
            this.add.text(50, 150, playername);
            this.add.image(400, 100, clan);
        }

        await this.getPirates();
        await this.useBuilder(gender, clan)
    }


    async useBuilder(gender, clan) {
        return fetch(`${config.serverUrl}/get_player_builder/${gender}/${clan}`)
            .then(res => res.json())
            .then(res => {

                this.add.image(900, 100, res[0].sprite);
                this.add.image(900, 98, res[1].clothes);
            })
    }

    async getPirates() {
        let res = await fetch(`${config.serverUrl}/get_pirates/6`);
        res = await res.json();
        console.log(res);
        res.forEach((pirate, index) => {
            this.add.image(600, (index + 1)*100, pirate.sprite);
            this.add.image(700, (index + 1)*100, pirate.ship.sprite);
        })
    }

    /**
     * 
     * @param  {...Object} ships 
     */
    renderShips(...ships) {
        ships.forEach((ship, index) => {
            let xPosition = (index + 1)*100 + 50*index
            this.add.image(xPosition, 300, ship.sprite);

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
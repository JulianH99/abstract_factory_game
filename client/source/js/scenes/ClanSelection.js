import Phaser from 'phaser';
import config from "../config";

export default class ClanSelection extends Phaser.Scene {

    constructor() {
        super({key:"ClanSelection"});

        this.textConfig = {
            fontFamily: 'Arial',
            align: 'center',
            fontSize: 24,
            fill: 'white'
        }
    }

    preload() {
        this.load.image('SymbolKuirk', './assets/SymbolKuirk.png');
        this.load.image('SymbolRanger', './assets/SymbolRanger.png');
        this.load.image('SymbolStrolth', './assets/SymbolStrolth.png');
        this.load.image('fondo', './assets/fondo.png')
    }

    async create(){

        let center = window.innerWidth;

        let fondo = this.add.tileSprite(880, 550, 600, 600 ,'fondo');
        fondo.scaleY = 2.5;
        fondo.scaleX = 2.5;

        this.text = this.add.text(100, 100, 'Choose your clan', this.textConfig);
        this.text.x = window.innerWidth / 2 - this.text.width + 50;


        await this.getClans();

        this.input.on('gameobjectdown', this.onGameObjectDown, this);
    }

    onGameObjectDown(pointer, object) {
        let clan = object.texture.key;

        this.sys.game._CLAN = this.sys.game._CLANS[clan];

        this.scene.start("Scene1");
    }

    /**
     *
     * Gets the clans from the server
     *
     * @returns {Promise<Response | never>}
     */
    async getClans() {
        this.sys.game._CLANS= [];
        return fetch(`${config.serverUrl}/clans`)
            .then(res => res.json())
            .then(res => {
                res.map((clan, index) => {

                    this.sys.game._CLANS[clan.sprite] = clan.name;
                    let img = this.add.image(window.innerWidth/2 + index*150, 300, clan.sprite);
                    img.x = img.x - 2.1*img.width;
                    img.setInteractive();
                    let text = this.add.text(img.x, img.y + img.height, clan.name.toUpperCase(),
                        this.textConfig);
                    text.x = text.x - text.width/2;
                })
            })
    }

}
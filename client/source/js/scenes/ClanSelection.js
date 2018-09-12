import Phaser from 'phaser';

export default class ClanSelection extends Phaser.Scene {

    constructor() {
        super({key:"ClanSelection"});
    }

    preload() {
        this.load.image('kuirk', './assets/SymbolWuick.png');
        this.load.image('ranger', './assets/SymbolRanger.png');
        this.load.image('strolth', './assets/SymbolStrolth.png');
        this.load.image('fondo', './assets/fondo.png')
    }

    create(){

        let center = window.innerWidth;

        let textConfig = {
            fontFamily: 'Arial',
            align: 'center',
            fontSize: 24,
            fill: 'white'
        }

        let fondo = this.add.tileSprite(880, 550, 600, 600 ,'fondo');
        fondo.scaleY = 2.5;
        fondo.scaleX = 2.5;

        this.text = this.add.text(100, 100, 'Choose your clan', textConfig);
        this.text.x = window.innerWidth / 2 - this.text.width + 50;

        let clans = ['kuirk', 'ranger', 'strolth'];

        clans.map((clan, index) => {
            let img = this.add.image(center/2 + index*150, 300, clan);
            img.x = img.x - 2.1*img.width;
            img.setInteractive();
            let text = this.add.text(img.x, img.y + img.height, clan, textConfig);
            text.x = text.x - text.width/2;
        }); 
        

        this.input.on('gameobjectdown', this.onGameObjectDown, this);
    }

    onGameObjectDown(pointer, object) {
        let clan = object.texture.key;

        this.sys.game._CLAN = clan;

        this.scene.start("Scene1");
    }

}
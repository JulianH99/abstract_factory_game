
import Phaser from 'phaser';

export default class Scene1 extends Phaser.Scene{

    constructor() {
        super({key: "Scene1"});
    }

    preload() {
        this.load.image('male', './assets/male.png');
        this.load.image('female', './assets/female.png');
        this.load.image('mario', './assets/mario.png');
    }

    create() {
        let centerX = window.innerWidth/2;
        console.log(centerX);
        let imageWidth = 200;

        this.chooseGenderText = this.add.text(centerX - 100, 50, 'Escoge tu genero', {
            fontFamily: 'Arial',
            fontSize: '30px'
        });

        this.maleImg = this.add.image(centerX - 100, 300, 'male');
        this.maleImg.displayWidth = imageWidth;
        this.maleImg.scaleY = this.maleImg.scaleX;


        this.femaleImg = this.add.image(centerX + 100, 300, 'female');
        this.femaleImg.displayWidth = imageWidth + 50;
        this.femaleImg.scaleY = this.femaleImg.scaleX;
        
        this.maleImg.setInteractive();
        this.femaleImg.setInteractive();

        this.input.on('gameobjectdown', this.onObjectDown, this);
    }

    onObjectDown(pointer, gameObject) {
        let gender = gameObject.texture.key;

        this.scene.start("ShowChars", {
            gender: gender
        });
    }

    update() {
    }

}
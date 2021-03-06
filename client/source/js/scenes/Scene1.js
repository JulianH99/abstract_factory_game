
import Phaser from 'phaser';

export default class Scene1 extends Phaser.Scene{

    constructor() {
        super({key: "Scene1"});
    }

    preload() {
        this.load.image('male', './assets/male.png');
        this.load.image('female', './assets/female.png');
        this.load.image('fondo', './assets/fondo.png')
    }

    create() {
        let centerX = window.innerWidth/2;
        let imageWidth = 200;
        let height = window.innerHeight;
        let width = window.innerWidth;

        console.log(height);
        console.log(width);

        let fondo = this.add.tileSprite(650, 550, 600, 600 ,'fondo');
        fondo.scaleY = 2.5;
        fondo.scaleX = 2.5;

        this.chooseGenderText = this.add.text(centerX - 120, 50, 'Choose your gender', {
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

        this.sys.game._GENDER = gender;
        console.log(this.sys.game._GENDER);
        this.scene.start("ShowChars");

    }

}

import Phaser from 'phaser';
import socket from '../handlers/Socket';

export default class Scene1 extends Phaser.Scene{

    constructor() {
        super({key: "Scene1"});
    }

    preload() {
        this.load.image('mario', './assets/mario.gif');
    }

    create() {


        this.text = this.add.text(0, 0, "Welcome to my games");

        this.D = this.input.keyboard.addKey(Phaser.Input.Keyboard.KeyCodes.D);

        socket.on('response', () => {
            console.log('response from server');
            this.add.image(Phaser.Math.RND.integerInRange(100, 500), 100, 'mario');
        })
    }

    update() {



    }

}
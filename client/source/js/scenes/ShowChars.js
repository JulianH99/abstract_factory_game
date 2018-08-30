import Phaser from 'phaser';
import config from '../config';

export default class ShowChars extends Phaser.Scene {

    constructor() {
        super({key:"ShowChars"});
    }

    preload() {
        this.getCharsInfo(this.sys.game._GENDER);

        let gender = this.sys.game._GENDER;
        let clan = this.sys.game._CLAN;
        let prefix = '';

        if(gender === 'male')
            prefix = 'Men';
        else
            prefix = 'Women';

        this.load.image('char_ranger', `./assets/${prefix}Ranger.jpg`);
        this.load.image('char_strolth', `./assets/${prefix}Strolth.jpg`);
        this.load.image('char_kuirk', `./assets/${prefix}Wuick.jpg`);
        this.load.image('SecondModelBase', './assets/SecondModelBase.jpg');

    }

    create() {
        this.add.image(200,200, `char_${this.sys.game._CLAN}`);
        this.add.image(300, 100, 'SecondModelBase');
    }

    async getCharsInfo(gender) {
        await fetch(`${config.serverUrl}/get_group_of/${gender}`)
            .then(res => res.json())
            .then(res => {
                console.log(res);
            });
    }
 
}
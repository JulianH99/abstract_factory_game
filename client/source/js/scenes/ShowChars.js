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

        this.load.image('char_ranger', `./assets/${prefix}Ranger.png`);
        this.load.image('char_strolth', `./assets/${prefix}Strolth.png`);
        this.load.image('char_kuirk', `./assets/${prefix}Wuick.png`);
        this.load.image('SecondModelBase', './assets/SecondModelBase.png');

    }

    async create() {
        this.add.image(200, 200, `char_${this.sys.game._CLAN}`);
        this.add.image(300, 100, 'SecondModelBase');
    }

    async getCharsInfo(gender, clan) {
        await fetch(`${config.serverUrl}/get_group_of/${gender}/${clan}`)
            .then(res => res.json())
            .then(res => {
                console.log(res);
            });
    }
 
}
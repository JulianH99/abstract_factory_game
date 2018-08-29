import Phaser from 'phaser';
import config from '../config';

export default class ShowChars extends Phaser.Scene {

    constructor() {
        super({key:"ShowChars"});
    }

    init(data) {
        console.log(data);
        this.sys.game._GENDER = data.gender;
        
    }

    async preload() {
        await this.getCharsInfo(this.sys._GENDER);

        let gender = this.sys.game._GENDER;
        let prefix = '';
        console.log(gender);
        if(gender == 'male') 
            prefix = 'Men';
        else
            prefix = 'Women';

        console.log(prefix);
        
        this.load.image('rander', `./assets/${prefix}Ranger.jpg`);
        this.load.image('strolth', `./assets/${prefix}Strolth.jpg`);
        this.load.image('wuick', `./assets/${prefix}Wuick.jpg`);
        this.load.image('SecondModeloBase', './assets/SecondModelBase.jpg');

    }

    create() {
        this.add.image(200,200, 'ranger');
        this.add.image(300, 100, 'SecondModelBase')
    }

    async getCharsInfo(gender) {
        await fetch(`${config.serverUrl}/get_group_of/${gender}`)
            .then(res => res.json())
            .then(res => {
                console.log(res);
            });
    }
 
}
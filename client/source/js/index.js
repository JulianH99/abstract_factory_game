
import Phaser from 'phaser';
import Scene1 from './scenes/Scene1';
import ShowChars from './scenes/ShowChars';
//import Socket from './handlers/Socket';
import '../scss/main.scss';

/*let socket = SocketIO.connect('http://127.0.0.1:3001')

socket.on('connect', function() {
    document.querySelector('#connected')
        .innerHTML = "Connected with socket io"
    socket.emit('connected')
})*/


// initialize config
const config = {
    type: Phaser.AUTO,
    width: window.innerWidth,
    height: window.innerHeight,
    scene: [Scene1, ShowChars],
    physics: {
        default: 'ARCADE'
    }

};

const game = new Phaser.Game(config);



// initialize game





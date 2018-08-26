
import Phaser from 'phaser';
import Scene1 from './scenes/Scene1';
import Socket from './handlers/Socket';
import '../scss/main.scss';

// import SocketIO from 'socket.io-client'

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
    scene: [Scene1],
    physics: {
        default: 'ARCADE'
    }

};

const game = new Phaser.Game(config);



// initialize game





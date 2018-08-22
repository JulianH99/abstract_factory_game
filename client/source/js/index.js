
import { Game } from 'phaser';
import SocketIO from 'socket.io-client'

let socket = SocketIO.connect('http://127.0.0.1:3001')

socket.on('connect', function() {
    document.querySelector('#connected')
        .innerHTML = "Connected with socket io"
    socket.emit('connected')
})




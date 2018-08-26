import io from 'socket.io-client';
import config from '../config';


let socket = io(config.serverUrl);

socket.on('connect', () => {
    console.log('io connected');
    socket.emit('message');

});

export default socket;


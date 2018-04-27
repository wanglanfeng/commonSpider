PROJECT.socket = function () {
    var domain = window.location.host;
    var namespace = '/test';
    var url = 'ws://' + domain + namespace;

    var socket = io.connect(url);
    setInterval(function () {
        console.info('发送消息');
        socket.emit('request_for_response', {'param': 'value'});
        socket.emit('test', {'param': 'value'})
    }, 5000)
    socket.on('connect', function (data) {
        socket.emit('request_for_response', {'param': 'value'})
        console.info('连接服务器');
    })
    socket.on('response', function (data) {
        console.info('response');
    });
    socket.on('test', function (data) {
        console.info('test');
    })
    return socket;
}();
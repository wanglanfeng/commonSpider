PROJECT.socket = function () {
    let ip = 'localhost';
    let port = '9000';
    let path = '';
    let url = 'ws://'+ip+':'+port+path;

    function init() {
        var socket = io.connect(url);
        socket.emit('request_for_response', {'param': 'value'});
        socket.on('response', function (data) {
            if(data.code == '200'){
                console.info('成功');
            }else{
                console.info('失败');
            }
        });
    }
    return {
        init: function () {
            
        }
    }
}
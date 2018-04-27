/**
 * Created by 王凯 on 2018/3/21.
 */

PROJECT = window.PROJECT || {}


// 浏览器storage操作模型
PROJECT.storage = function (storage) {
    this.storage = storage;
    this.storageSupport = !!this.storage
    this.set = function (key, value, expire_time) {
        var result = false;
        if(!this.storageSupport || !key || !value){
            return result;
        }
        var data = {
            value: value
        }
        if(expire_time){
            // 存在
            if(Object.prototype.toString.call((expire_time)) == '[object Number]'){
                // 秒数
                var now = new Date();
                // 毫秒数
                var timestamp = now.getTime();
                data['expire_time'] = timestamp + expire_time*1000;
            }else if(Object.prototype.toString.call((expire_time)) == '[object Date]'){
                // 定点时间
                var timestamp = expire_time.getTime();
                data['expire_time'] = timestamp;
            }
        }
        data = JSON.stringify(data);
        try{
            this.storage.setItem(key, data);
            result = true;
        }catch (e){
            console.log('存储出错，异常信息：' + e);
        }
        return result;
    }
    this.get = function (key) {
        if(!this.storageSupport || !key){
            return undefined;
        }
        var data = this.storage.getItem(key);
        if(!!key && !!data){
            // 存在
            data = JSON.parse(data);
            var now_timestamp = new Date().getTime();
            var expire_time = data['expire_time'];
            if(!expire_time){
                // 不存在
                data = data['value'];
            }else if(now_timestamp <= expire_time){
                // 没过期
                data = data['value'];
            }else{
                // 过期了
                this.remove(key);
                data = undefined;
            }
        }else{
            data = undefined;
        }
        return data;
    }
    this.remove = function (key) {
        if(!this.storageSupport || !key){
            return false;
        }
        this.storage.removeItem(key);
        return true;
    }
    this.clear = function () {
        if(!this.storageSupport){
            return false;
        }
        this.storage.clear();
        return true;
    }
    return this;
}

// 浏览器sessionStorage操作
PROJECT.sessionStorage = (function () {
    var instance = new PROJECT.storage(window.sessionStorage);
    return instance;
})();

// 浏览器localStorage操作
PROJECT.localStorage = (function (){
    var instance = new PROJECT.storage(window.localStorage);
    return instance;
})();


// 配置tostr请提示配置
toastr.options=
 {
    "closeButton":false,//显示关闭按钮
    "debug":false,//启用debug
    "positionClass":"toast-bottom-right",//弹出的位置
    "showDuration":"300",//显示的时间
    "hideDuration":"100",//消失的时间
    "timeOut":"3000",//停留的时间
    "extendedTimeOut":"1000",//控制时间
    "showEasing":"swing",//显示时的动画缓冲方式
    "hideEasing":"linear",//消失时的动画缓冲方式
    "showMethod":"fadeIn",//显示时的动画方式
    "hideMethod":"fadeOut"//消失时的动画方式
};

// 配置jquery-confirm配置
jconfirm.defaults = {
    title: '提示',
    titleClass: 'tc f14',
    type: 'default',
    typeAnimated: true,
    draggable: true,
    dragWindowGap: 15,
    dragWindowBorder: true,
    animateFromElement: false,
    smoothContent: true,
    content: '',
    buttons: {},
    defaultButtons: {},
    contentLoaded: function(data, status, xhr){
    },
    icon: '',
    lazyOpen: false,
    bgOpacity: null,
    theme: 'light',
    animation: 'scale',
    closeAnimation: 'scale',
    animationSpeed: 400,
    animationBounce: 1,
    rtl: false,
    container: 'body',
    containerFluid: false,
    backgroundDismiss: false,
    backgroundDismissAnimation: 'shake',
    autoClose: false,
    closeIcon: null,
    closeIconClass: false,
    watchInterval: 100,
    columnClass: 'col-md-4 col-md-offset-4 col-sm-6 col-sm-offset-3 col-xs-10 col-xs-offset-1',
    boxWidth: '50%',
    scrollToPreviousElement: true,
    scrollToPreviousElementAnimate: true,
    useBootstrap: true,
    offsetTop: 40,
    offsetBottom: 40,
    bootstrapClasses: {
        container: 'container',
        containerFluid: 'container-fluid',
        row: 'row',
    },
    onContentReady: function () {},
    onOpenBefore: function () {},
    onOpen: function () {},
    onClose: function () {},
    onDestroy: function () {},
    onAction: function () {}
};

// 封装ajax
PROJECT.ajax = function (url, data, success, error, type) {
    $.ajax({
        url: url,
        headers: {
            Accept: "application/json, text/html/, application/xhtml+xml; charset=utf-8"
        },
        type: type || 'post',
        dataType: 'json',
        data: data,
        success: success || function (res) {
            if(res.status){
                res.msg != '' && toastr.error(res.msg);
            }else{
                res.msg != '' && toastr.success(res.msg);
            }
        },
        error: error || function (jqXHR, textStatus, errorThrown) {
            toastr.error(errorThrown);
        }
    });
}


// 提示工具
PROJECT.tool = {
    alert: function (msg, type, buttons) {
        var config = {
            type: type || 'orange',
            content: '<div class="tc f14 pt10">'+msg+'</div>',
            buttons: buttons || {
                '关闭': function () {

                }
            }
        }
        $.alert(config);
    },
    dangerAlert: function (msg, buttons) {
        this.alert(msg, 'red', buttons);
    },
    warnAlert: function (msg, buttons) {
        this.alert(msg, 'orange', buttons);
    },
    successAlert: function (msg, buttons) {
        this.alert(msg, 'green', buttons);
    },
    infoAlert: function (msg, buttons) {
        this.alert(msg, 'blue', buttons);
    },
    darkAlert: function (msg, buttons) {
        this.alert(msg, 'dark', buttons);
    },
    confirm: function (msg, success, cancel, type, title) {
        var config = {
            content: '<div class="tc f14 pt10">'+msg+'</div>',
            type: type || 'red',
            buttons: {
                '确认': {
                    btnClass: 'btn-blue',
                    action: success || function () {

                    }
                },
                '取消': {
                    action: cancel || function () {

                    }
                }
            }
        }
        if(title){
            config['title'] = title;
        }
        $.confirm(config);
    },
    dangerConfirm: function (msg, success, cancel, title) {
        this.confirm(msg, success, cancel, 'red', title);
    },
    warnConfirm: function (msg, success, cancel, title) {
        this.confirm(msg, success, cancel, 'orange', title);
    },
    successConfirm: function (msg, success, cancel, title) {
        this.confirm(msg, success, cancel, 'green', title);
    },
    infoConfirm: function (msg, success, cancel, title) {
        this.confirm(msg, success, cancel, 'blue', title);
    },
    darkConfirm: function (msg, success, cancel, title) {
        this.confirm(msg, success, cancel, 'dark', title);
    }
}

// 获取表单键值对，建为name，值为value
PROJECT.form_data = function (form, name_array) {
    var result = {};
    var value = ''
    $.each(name_array, function (index, name) {
        var choose = form.find('[name=' + name + ']');
        var selector = choose.prop('tagName');
        switch (selector) {
            case 'INPUT':
                var type = choose.attr('type');
                switch (type) {
                    case 'radio':
                        value = choose.find(':checked').val();
                        break;
                    case 'checkbox':
                        var checkboxs = choose.find(':checked');
                        var temp = [];
                        for (var i = 0, len = checkboxs.length; i < len; i++) {
                            temp.push(checkboxs.eq(i).val());
                        }
                        value = temp;
                        break;
                    default:
                        value = choose.val();
                        break;
                }
                break;
            case 'SELECT':
                value = choose.find(':checked').val();
                break;
            case 'TEXTAREA':
                value = choose.val();
                break;
            default:
                break;
        }
        result[name] = value;
    });
    return result;
}

// 通过name更新表单信息
PROJECT.form_update = function (form, data) {
    $.each(data, function (name, value) {
        var choose = form.find('[name=' + name + ']');
        var selector = choose.prop('nodeName');
        if (typeof value == 'str') {
            value = value.trim();
        }
        if (value) {
            switch (selector) {
                case 'INPUT':
                    var type = choose.attr('type');
                    switch (type) {
                        case 'radio':
                            choose.find('value=' + value).trigger('click');
                            break;
                        case 'checkbox':
                            // value为一个数组
                            $.each(value, function (index, temp) {
                                choose.find('value=' + temp).trigger('click');
                            });

                            break;
                        default:
                            choose.val(value);
                            break;
                    }
                    break;
                case 'SELECT':
                    choose.find("option[value='" + value + "']").attr("selected", true);
                    break;
                case 'TEXTAREA':
                    choose.text(value);
                    break;
                default:
                    break;
            }
        }
    });
}

// 实现全屏
PROJECT.fullScreen = function(el) {
    var rfs = el.requestFullScreen || el.webkitRequestFullScreen || el.mozRequestFullScreen || el.msRequestFullScreen,
        wscript;

    if(typeof rfs != "undefined" && rfs) {
        rfs.call(el);
        return;
    }

    if(typeof window.ActiveXObject != "undefined") {
        wscript = new ActiveXObject("WScript.Shell");
        if(wscript) {
            wscript.SendKeys("{F11}");
        }
    }
};

// 退出全屏
PROJECT.exitFullScreen = function(el) {
    var el= document,
        cfs = el.cancelFullScreen || el.webkitCancelFullScreen || el.mozCancelFullScreen || el.exitFullScreen,
        wscript;

    if (typeof cfs != "undefined" && cfs) {
      cfs.call(el);
      return;
    }

    if (typeof window.ActiveXObject != "undefined") {
        wscript = new ActiveXObject("WScript.Shell");
        if (wscript != null) {
            wscript.SendKeys("{F11}");
        }
  }
};

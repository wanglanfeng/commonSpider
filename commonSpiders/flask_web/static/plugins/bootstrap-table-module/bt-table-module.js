/**
 * Created by Administrator on 2017/11/9 0009.
 */
!function ($) {
    // 用户表配置
    var TableInit = function () {
        var oTableInit = new Object();
        oTableInit.context = {};
        oTableInit.cache = {};
        oTableInit.extensions = {};
        //初始化Table
        oTableInit.init = function () {
            $(oTableInit.context.table).bootstrapTable({
                url: oTableInit.context.config.url,         //请求后台的URL（*）
                method: oTableInit.context.config.method,                      //请求方式（*）
                contentType: oTableInit.context.config.contentType,
                ajaxOptions: oTableInit.context.config.ajaxOptions,
                toolbar: oTableInit.context.config.toolbar,                //工具按钮用哪个容器
                cache: oTableInit.context.config.cache,                       //是否使用缓存，默认为true，所以一般情况下需要设置一下这个属性（*）
                pagination: oTableInit.context.config.pagination,                   //是否显示分页（*）
                sortable: oTableInit.context.config.sortable,                     //是否启用排序
                sortOrder: oTableInit.context.config.sortOrder,                   //排序方式
                queryParams: oTableInit.context.config.queryParams,//传递参数（*）
                sidePagination: oTableInit.context.config.sidePagination,           //分页方式：client客户端分页，server服务端分页（*）
                pageNumber:oTableInit.context.config.pageNumber,                       //初始化加载第一页，默认第一页
                pageSize: oTableInit.context.config.pageSize,                       //每页的记录行数（*）
                pageList: oTableInit.context.config.pageList,        //可供选择的每页的行数（*）
                strictSearch: oTableInit.context.config.strictSearch,
                paginationLoop: oTableInit.context.config.paginationLoop,
                responseHandler: oTableInit.context.config.responseHandler,
                search: oTableInit.context.config.search,
                uniqueId: oTableInit.context.config.uniqueId,
                columns: oTableInit.context.config.columns
            });
        };
        
        oTableInit.initConfig = function (table, opts) {

            oTableInit.context.table = table;
            var config = opts.config || {};
            oTableInit.context.config = {
                url: config.url || '',         //请求后台的URL（*）
                method: config.method || 'post',                      //请求方式（*）
                ajaxOptions: config.ajaxOptions || {},
                responseHandler: config.responseHandler || function (res) {
                    return res;
                },
                contentType: config.contentType || "application/x-www-form-urlencoded",
                toolbar: config.toolbar || false,                //工具按钮用哪个容器
                cache: config.cache || true,                       //是否使用缓存，默认为true，所以一般情况下需要设置一下这个属性（*）
                pagination: config.pagination || true,                   //是否显示分页（*）
                sortable: config.sortable || true,                     //是否启用排序
                sortOrder: config.sortOrder || "asc",                   //排序方式
                queryParams: oTableInit.getQueryParams,//传递参数（*）
                sidePagination: config.sidePagination || "client",           //分页方式：client客户端分页，server服务端分页（*）
                pageNumber:config.pageNumber || 1,                       //初始化加载第一页，默认第一页
                pageSize: config.pageSize || 25,                       //每页的记录行数（*）
                pageList: config.pageList || [10, 25, 50, 100, 'All'],        //可供选择的每页的行数（*）
                strictSearch: config.strictSearch || true,
                paginationLoop: config.paginationLoop || true,
                search: config.search || false,
                uniqueId: config.uniqueId || 'index',
                columns: config.columns || []
            };
            oTableInit.context.getQueryParam = opts.getQueryParam || function () {
                return {};
            };
        }

        // 刷新函数
        oTableInit.refresh = function(params){
            if(!!params){
                oTableInit.func('refresh', params);
            }else{
                oTableInit.func('refresh');
            }

        };
        
        // 调用默认的方法
        oTableInit.func = function (func_name, options) {
            var result = oTableInit.context.table.bootstrapTable(func_name, options);
            return result;
        }

        //得到查询的参数
        oTableInit.getQueryParams = function (params) {
            var param = oTableInit.context.getQueryParam() || {};
            if(oTableInit.context.config.sidePagination == 'server'){
                params = {
                    page: params.offset/params.limit,
                    size: params.limit
                }
                $.extend(param, params);
            }
            return param;
        };
        return oTableInit;
    };

    // 配置到jquery的方法域中
    $.fn.extend({
        "BTableModule": function (opts) {
            opts = opts || {};
            var table = this;
            var oTable = TableInit();
            oTable.initConfig(table, opts);
            oTable.init();
            return oTable;
        }
    });
}(jQuery);
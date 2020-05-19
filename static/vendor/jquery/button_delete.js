$(function(){
    $("input[type='button_delete']").click(function() {
        $("input[name='checkItem']:checked").each(function() { // 遍历选中的checkbox
            n = $(this).parents("li").index();  // 获取checkbox所在行的顺序
            $("table#table1").find("li:eq("+n+")").remove();
        });
    });
});

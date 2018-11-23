$(function () {



    $('.glyphicon-heart').click(function () {
        var $like_num = $(this).next().html()
        // 判断颜色是否相等，rgb后面的三个rgb，最后两个必须加一个空格才能比较
        if ($(this).css('color') =='rgb(255, 0, 0)'){
            $(this).css('color','#333333')
            $(this).next().html(parseInt($like_num)-1)
        }else{
             $(this).css('color','red')

        $(this).next().html(parseInt($like_num)+1)
        }

    })




})
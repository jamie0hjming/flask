$(function () {

    var no_telemail = true
    var account_status = false

    $('#account input').blur(function () {

        // 数字、字母
        // var reg = /^[A-Za-z0-9]+$/
        var reg = /^[a-zA-Z0-9_.-]+@[a-zA-Z0-9-]+(\.[a-zA-Z0-9-]+)*\.[a-zA-Z0-9]{2,6}$/
        // var reg = /^[\w.\-]+@(?:[a-z0-9]+(?:-[a-z0-9]+)*\.)+[a-z]{2,3}$/
        istelemail = reg.test($(this).val())
        if (istelemail) {  // 符合
            // ajax,获取账号是否可用
            no_telemail = false

            $.get('/check/', {'account': $(this).val()}, function (response) {

                if (response.status == 1) {  // 可用
                    account_status = false
                    $('#account i').html('')
                    $('#account').removeClass('has-error').addClass('has-success')
                } else {    // 不可用
                    account_status = true
                    $('#account i').html(response.msg)
                    $('#account').removeClass('has-success').addClass('has-error')
                }
            })

        } else {    // 不符合
            no_telemail = true

            $('#account i').html('请用邮箱注册')
            $('#account').removeClass('has-success').addClass('has-error')
        }
    })

    ////////////////////////////////////////////////////////////////////////////////////////////////////

    ////////////////////////////////////////////////////////////////////////////////////////////////////

    $('#password input').blur(function () {
        if ($(this).val() == '') return

        // 数字，字母
        var reg = /^[A-Za-z0-9]{6,12}$/
        if (reg.test($(this).val())) {  // 符合
            $('#password i').html('')
            $('#password').removeClass('has-error').addClass('has-success')
        } else {    // 不符合
            $('#password i').html('6~12位数字或者字母组成')

            $('#password').removeClass('has-success').addClass('has-error')
        }
    })

    // 确认密码
    var submit_status_pwd = true
    $('#passwd input').blur(function () {
        if ($(this).val() == '') return

        // 数字

        if ($(this).val() == $('#password input').val()) {  // 符合
            submit_status_pwd = true
            $('#passwd i').html('')
            $('#passwd').removeClass('has-error').addClass('has-success')
        } else {    // 不符合
            $('#passwd i').html('两次密码不一致')
            submit_status_pwd = ~submit_status_pwd
            $('#passwd').removeClass('has-success').addClass('has-error')
        }
    })

    ////////////////////////////////////////////////////////////////////////////////////////////////////

    //给表单添加提交事件*
    $(".blue-button").click(function () {

        var $account_val = $.trim($("input[name=account]").val())
        var $password_val = $.trim($("input[name=password]").val())
        var $passwd_val = $.trim($("input[name=check_pwd]").val())
        var $nickname_val = $.trim($("input[name=nick_name]").val())
        var reg = /(^[\w.\-]+@(?:[a-z0-9]+(?:-[a-z0-9]+)*\.)+[a-z]{2,3}$)|(^1[3|4|5|8]\d{9}$)/
        var reg1 = /^[A-Za-z0-9]{6,12}$/

        //当表单提交的时候，对字段验证，并根据需要放出提示 trim去除字符串两端的空格

        if ($account_val == "") {
            alert("用户名不能为空");
            return false;//终止表单提交
        }
        else if (!reg.test($account_val)) {
            alert("请用邮箱注册");
            return false;//终止表单提交
        }
        else if (account_status) {
            alert("账号已被注册");
            return false;//终止表单提交
        }
        else if (!reg1.test($password_val)) {

            alert("密码不满足条件");
            return false;//终止表单提交
        }

        else if ($nickname_val == "") {
            alert("昵称不能为空");
            return false;//终止表单提交
        }
        else if ($password_val != $passwd_val) {
            alert("两次密码不一致");
            return false;//终止表单提交
        }


        $("#formid").submit()

    })

    $('.login').click(function () {
        var $account_val = $.trim($("input[name=account_login]").val())
        var $password_val = $.trim($("input[name=password_login]").val())
        alert($password_val)
        data = {
            'account':$account_val,
            'password':$password_val,
        }
        $.get('/login/',data,function (response) {
            alert(response.status)
            if(response.status){
                $("#login").submit()
            }else {
                alert(response.msg)
            }
        })
    })
})

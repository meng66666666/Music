$(function(){
    var typediv = document.getElementById("label_a")
    var sortdiv = document.getElementById("label_a")
    alert('进入了ajax')
    typediv.style.display = "none"
    sortdiv.style.display = "none"


    alltypebtn.addEventListener("click", function(){
        typediv.style.display = "block"
        sortdiv.style.display = "none"
    },false)
    showsortbtn.addEventListener("click", function(){
        typediv.style.display = "none"
        sortdiv.style.display = "block"
    },false)
    typediv.addEventListener("click", function(){
        typediv.style.display = "none"
    },false)
    sortdiv.addEventListener("click", function(){
        sortdiv.style.display = "none"
    },false)

    //选中所有的类名为addShopping的对象（即+）
    var $addShopping = $(".addShopping");
    $addShopping.bind("click",function(){
        //this为当前触发事件的DOM对象，即为点那个+就为哪个对象
        var goods_id = $(this).attr("ga");   // 获取点击按钮所在行的商品id
        $.getJSON("/addshop/",{"goods_id":goods_id},function(data){
            //第一个参数为请求的路径URL，发送给服务端的对象
            if(data["status"]=="900"){
                window.open("/login/",target="_self");
            }else if(data["status"]=="200"){
                document.getElementById(goods_id).innerHTML=data["cart_num"];
            }
        });
    });


    var $subShopping = $(".subShopping");
    $subShopping.bind("click",function(){
        var goods_id = $(this).attr("ga");
        $.getJSON("/subcart/",{"goods_id":goods_id},function(data){
            if(data["status"]=="900"){
                window.open("/login/",target="_self");
            }else if(data["status"]=="200"){
                document.getElementById(goods_id).innerHTML=data["cart_num"];
            }else if(data["status"]=="901"){
                alert(data["msg"]);
            }
        });
    });
})
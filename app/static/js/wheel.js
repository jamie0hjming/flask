$(function () {

var swiper = new Swiper('.swiper-container', {
        pagination: '.swiper-pagination',
        nextButton: '.swiper-button-next',
        prevButton: '.swiper-button-prev',
        paginationClickable: true,
        spaceBetween: 30,
        centeredSlides: true,
        autoplay: 2500,
        autoplayDisableOnInteraction: false
    });
   // $.getJSON('/wheel/',function (response) {
   //     var wheel = response.data
   //     for (var i=0;i<wheel.length;i++){
   //
   //         var $img = $('<img>').attr('src','/static/img1/'+wheel[i].img_root)
   //         $('<div class="swiper-slide"></div>').append($img).appendTo('.wheel')
   //
   //     }
   //
   // })

})



// Удалите этот кусок кода
// $(function(){
//     $('a[href*=#]').click(function() {
//     if (location.pathname.replace(/^\//,'') == this.pathname.replace(/^\//,'')
//         && location.hostname == this.hostname) {
//             var $target = $(this.hash);
//             $target = $target.length && $target || $('[name=' + this.hash.slice(1) +']');
//             if ($target.length) {
//                 var targetOffset = $target.offset().top;
//                 $('html,body').animate({scrollTop: targetOffset}, 500);//скорость прокрутки
//                 return false;
//             }
//         }
//     });
// });
$(function(){
    // Открываем и закрываем подвал
    $("footer").click(function() {     
        $("footer").toggleClass("action");
    })
    $(".reg_btn").click(function() {     
        $(".reg_input").toggleClass('hidden');
        
    })
});
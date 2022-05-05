$(document).ready(function() {
    // Transition effect for navbar 
    $(window).scroll(function() {
        // checks if window is scrolled more than 500px, adds/removes solid class
        if ($(this).scrollTop() > 500) {
            $('.navbar').addClass('solid');
        } else {
            $('.navbar').removeClass('solid');
        }
    });
});

$(function() {
    //WOW plugin init
    new WOW().init();

    //parallax effect for banner
    (function() {
        var posY;
        var image = document.getElementById('parallax');;

        function paralax() {
            posY = window.pageYOffset;
            image.style.top = posY * 0.9 + 'px';
        }
        window.addEventListener('scroll', paralax);
    })();
});
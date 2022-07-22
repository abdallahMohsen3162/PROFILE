var closer = document.querySelector(".close"),
    show = document.getElementById('show'),
    theNav = document.querySelector('.link-container');

show.onclick = function() {
    theNav.classList.add('show');


}
closer.onclick = function() {
    theNav.classList.remove('show');

}


document.onkeyup = function(e) {
    if (e.key === 'Escape') {
        theNav.classList.remove('show');
    }
}






var taps = new Vue({
    el: '#tap',
    data: {
        currentActive: 1
    }
})


var collapse = new Vue({
    el: '#collapse',
    data: {
        currentActive: 1
    }
})
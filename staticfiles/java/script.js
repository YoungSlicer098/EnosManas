function scrollReply() {
    document.getElementById('reply_form').scrollIntoView({
        behavior: 'smooth'
    });
};

document.addEventListener("DOMContentLoaded", function (event) {
    var scrollpos = localStorage.getItem('scrollpos');
    if (scrollpos) window.scrollTo(0, scrollpos);
    document.getElementById('reply_form').scrollIntoView({
    });
});

window.onbeforeunload = function (e) {
    localStorage.setItem('scrollpos', window.scrollY);
};


let frameline = document.getElementById("frameline");
let title = document.getElementById("title");
let subtitle = document.getElementById("sub-title");
let road = document.getElementById("road");
let text = document.getElementById("text");

window.addEventListener('scroll', function () {
    var value = window.scrollY;

    frameline.style.top = -value * 0.05 + "px";
    title.style.transform = "translateY(" + ((-value * 0.05) + 30) + 'vh)';
    subtitle.style.transform = "translateY(" + ((-value * 0.05) + 30) + 'vh)';
    road.style.top = value * 0.15 + 'px';
    text.style.top = value * 1 + 'px';
});


const tabs = document.querySelectorAll('.tab-btn');
const gallerybtn = document.querySelectorAll('.gallery-btn')
const all_content = document.querySelectorAll('.content');
const gallery = document.querySelectorAll('.gallery')

tabs.forEach((tab, index) => {
    tab.addEventListener('click', (e) => {
        tabs.forEach(tab => { tab.classList.remove('active') });
        tab.classList.add('active');

        var line = document.querySelector('.tab-line');
        line.style.width = e.target.offsetWidth + "px";
        line.style.left = e.target.offsetLeft + "px";

        all_content.forEach(content => { content.classList.remove('active') });
        all_content[index].classList.add('active');
    })
})

gallerybtn.forEach((tab, index) => {
    tab.addEventListener('click', (e) => {
        gallerybtn.forEach(tab => { tab.classList.remove('active') });
        tab.classList.add('active');

        var line = document.querySelector('.gallery-line');
        line.style.width = e.target.offsetWidth + "px";
        line.style.left = e.target.offsetLeft + "px";


        gallery.forEach(content => { content.classList.remove('active') });
        gallery[index].classList.add('active');
    })
})

window.addEventListener('load', () => {
    const loader = document.querySelector(".loader");

    loader.classList.add("loader-hidden");

    loader.addEventListener("transitionend", () => {
        document.body.removeChild("loader");
    })

})


document.addEventListener("DOMContentLoaded", function() {
    const nbtn = document.querySelectorAll('.nbtn');
    const navLine = document.querySelector('.nav-line');

    nbtn.forEach((tab) => {
        tab.addEventListener('click', function(e) {
            e.preventDefault();

            nbtn.forEach(tab => { tab.classList.remove('active'); });
            this.classList.add('active');

            const href = this.getAttribute('href');
            const target = document.querySelector(href);

            // Run a scroll animation to the position of the element which has the same id like the href value.
            $('html, body').animate({
                scrollTop: target.offsetTop
            }, 600);

            // Update the nav-line position and size
            navLine.style.width = this.offsetWidth + "px";
            navLine.style.left = this.offsetLeft + "px";
        });
    });

    $(window).on("scroll", function() {
        const currentPos = $(window).scrollTop();

        nbtn.forEach((tab) => {
            const href = tab.getAttribute('href');
            const section = document.querySelector(href);

            const sectionTop = section.offsetTop;
            const sectionBottom = sectionTop + section.offsetHeight;

            if (currentPos >= sectionTop && currentPos < sectionBottom) {
                nbtn.forEach(tab => { tab.classList.remove('active'); });
                tab.classList.add('active');

                // Update the nav-line position and size
                navLine.style.width = tab.offsetWidth + "px";
                navLine.style.left = tab.offsetLeft + "px";
            }
        });
    });
});

document.addEventListener("DOMContentLoaded", function() {
    const sbtns = document.querySelectorAll('.sbtn');
    const sideLine = document.querySelector('.side-line');

    sbtns.forEach((btn) => {
        btn.addEventListener('click', function(e) {
            e.preventDefault();

            sbtns.forEach(btn => { btn.classList.remove('active'); });
            this.classList.add('active');

            const href = this.getAttribute('href');
            const target = document.querySelector(href);

            // Run a scroll animation to the position of the element which has the same id like the href value.
            $('html, body').animate({
                scrollTop: target.offsetTop
            }, 600);

            // Update the side-line position and size
            sideLine.style.height = this.offsetHeight + "px";
            sideLine.style.top = this.offsetTop + "px";
        });
    });

    $(window).on("scroll", function() {
        const currentPos = $(window).scrollTop();

        sbtns.forEach((btn) => {
            const href = btn.getAttribute('href');
            const section = document.querySelector(href);

            const sectionTop = section.offsetTop;
            const sectionBottom = sectionTop + section.offsetHeight;

            if (currentPos >= sectionTop && currentPos < sectionBottom) {
                sbtns.forEach(btn => { btn.classList.remove('active'); });
                btn.classList.add('active');

                // Update the side-line position and size
                sideLine.style.height = btn.offsetHeight + "px";
                sideLine.style.top = btn.offsetTop + "px";
            }
        });
    });
});

document.addEventListener("DOMContentLoaded", function() {
    const hamburgerContainer = document.getElementById('hamburger-container');
    const sidenav = document.querySelector('.sidenav');

    hamburgerContainer.addEventListener('click', function() {
        sidenav.classList.toggle('active');
    });
});

// Google Sheets

const scriptURL = 'https://script.google.com/macros/s/AKfycbyqxGzqvcPAgS-G_9kkQbAov_0f2Sq_J1TlmT7nDwFLtkKr6rNO_0ICJbE5tBhPz7W0vA/exec'

const form = document.forms['Contact-Form']

form.addEventListener('submit', e => {
    e.preventDefault()
    fetch(scriptURL, {method: 'POST', body: new FormData(form)}).then(response => alert("Thank you! Your form is submitted successfully.")).then(() => {window.location.reload(); }).catch(error => console.error('Error!', error.message))
})




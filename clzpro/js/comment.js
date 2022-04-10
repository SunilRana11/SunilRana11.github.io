

const reviews = document.querySelector('.reviews');
const reviewSec = document.querySelectorAll('.review-section');

// Buttons
const prevCmtBtn = document.querySelector('.prev-cmt-btn');
const nextCmtBtn = document.querySelector('.next-cmt-btn');

// Counter
let counter = 1;
let size = reviewSec[0].clientWidth;

// styling reiviews

reviews.style.transform = 'translateX(' + (- size * counter) +'px)'

nextCmtBtn.addEventListener('click',function(){
    if(counter >= reviewSec.length - 1) return;
    counter++;
    moveReviews();
    
});
prevCmtBtn.addEventListener('click',function(){
    if(counter <= 0) return;
    counter--;
    moveReviews();
});

reviews.addEventListener('transitionend',function(){
    if(reviewSec[counter].id === 'lastclone'){
        reviews.style.transition = 'none';
        counter = reviewSec.length - 2;
        reviews.style.transform = 'translateX(' + (- size * counter) +'px)';

    }
})

reviews.addEventListener('transitionend',function(){
    if(reviewSec[counter].id === 'firstclone'){
    reviews.style.transition = 'none';
    counter = reviewSec.length - counter;
    reviews.style.transform = 'translateX(' + (- size * counter) +'px)';
        
    }
})

function moveReviews(){
    reviews.style.transform = 'translateX(' + (- size * counter) +'px)';
    reviews.style.transition = 'transform .5s ease-in-out';

}
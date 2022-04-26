// NAVBAR
const header = document.querySelector('.header');
const main = document.querySelector('.main');

// Popular services
const coverContainer = document.querySelector('.services');
const coverCard = document.querySelector('.popular-services');

// Other more services

const moreServices = document.querySelector('.more-services');
const ourServices = document.querySelector('.our-services');


const navOptions = {
    rootMargin: "-220px 0px 0px 0px"
};

const navObserver = new IntersectionObserver(function(entries,navObserver){
    entries.forEach(entry =>{
        if(!entry.isIntersecting){
            header.classList.add('primary-back');
        }else{
            header.classList.remove('primary-back');
        }
    })
},navOptions);

navObserver.observe(main);

// Popular Service Card
const cardOptions = {
    threshold: 0.5
};

const coverOberserver = new IntersectionObserver(function(entries,coverOberserver){
    entries.forEach(entry =>{
        if(!entry.isIntersecting){
            return
                       
        }else{
            coverCard.classList.add('ani-up');
        }
    })
},cardOptions);

coverOberserver.observe(coverContainer);

// Other more services

const otherOptions = {
    threshold: 0.5
}
const moreServicesObserver = new IntersectionObserver(function(entries,moreServicesObserver){
    entries.forEach(entry =>{
       if(!entry.isIntersecting){
           return
       }else{
            ourServices.classList.add('left');
            console.log('run')
       }
    })
},otherOptions);

moreServicesObserver.observe(moreServices);

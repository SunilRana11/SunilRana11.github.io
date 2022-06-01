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
    rootMargin: "-350px 0px 0px 0px"
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
            // coverCard.classList.remove('ani-up');
            return
                       
        }else{
            coverCard.classList.add('ani-up');
        }
    })
},cardOptions);

coverOberserver.observe(coverContainer);

// Other more services

const otherOptions = {
    threshold: 0.25
}
const moreServicesObserver = new IntersectionObserver(function(entries,moreServicesObserver){
    entries.forEach(entry =>{
       if(!entry.isIntersecting){
        //    ourServices.classList.remove('left');
        return
       }else{
            ourServices.classList.add('left');
       }
    })
},otherOptions);

moreServicesObserver.observe(moreServices);


// About our team oberver

const aboutUs = document.querySelector('.about-us');
const teamImg = document.querySelector('.team-img');
const teamDes = document.querySelector('.team-descri');

const team = {
    threshold : 0.5
}

const aboutOberserver = new IntersectionObserver(function(entries,aboutOberserver){
    entries.forEach(entry =>{
        if(!entry.isIntersecting){
            return
        } else {
            teamImg.classList.add('team-img-int');
            teamDes.classList.add('team-descri-int');
        }
    })
},team)

aboutOberserver.observe(aboutUs)


// Main section 

const tagHead = document.querySelector('.headTag');
const tagHead2 = document.querySelector('.headTag2');
const searchService = document.querySelector('.search-service')
const popTxt = document.querySelector('.pop-text');
const tagImg = document.querySelector('.main-img');

window.addEventListener('DOMContentLoaded',mainAni()
)

function mainAni(){
    //Header
    header.style.marginTop = '0%';
    header.style.opacity = '1'
    // head Tag
    tagHead.style.marginLeft = '0%';
    tagHead.style.opacity = '1';

    // head tag2
    tagHead2.style.marginLeft = '0%';
    tagHead2.style.opacity = '1';

    // Search service
    searchService.style.marginLeft = '0%';
    searchService.style.opacity = '1';

    // mainImage
    tagImg.style.opacity = '1';

    // popText
    popTxt.style.marginLeft = '0%';
    popTxt.style.opacity = '0.7';

}
  // LOGIN SIGNUP FORM
  var x = document.getElementById("login")
  var y = document.getElementById("register")
  var z = document.getElementById("btn")

  function register(){
      x.style.left = "-400px"
      y.style.left = "50px"
      z.style.left = "110px"
  }
  function login(){
      x.style.left = "50px"
      y.style.left = "450px"
      z.style.left = "0px"
  }
  // OPEN CLOSE FORM
  const join = document.querySelector('.join');
  const formContainer = document.querySelector('.form-container');
  const formBox = document.querySelector('.form-box');


  join.addEventListener('click',function(){
      formContainer.style.transform = 'scaleY(1)';
      formBox.style.transform = 'scaleY(1)';
      showForm();
  })

  function showForm(){
    formBox.style.transform = 'scaleY(1)';
      formContainer.addEventListener('click',function(e){
          let fCC1 = e.target.classList.contains('close-form');
          let fCC2 = e.target.parentElement.classList.contains('close-form');
          if(!fCC1 & !fCC2) {
              formContainer.style.transform = 'scaleY(0)';
          }else{
              formContainer.style.transform = 'scaleY(1)';
          }
      });
  };

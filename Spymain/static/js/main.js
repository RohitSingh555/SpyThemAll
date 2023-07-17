

const showSidebar = () => {
    sidebar.style.display="block";
  sidebar.style.transform =  `translate(0%)`;
  sidebar.style.filter = 'drop-shadow(0 0.5em 0.5em black)';
  overlay.style.display = 'block';
  var body= document.querySelector('light')
  document.body.style.overflowY = 'hidden';
  document.querySelector('#overlay').style.filter ='blur(7px)';
  document.querySelector('nav').style.filter ='blur(7px)';
  
  
}

const hideSidebar = () => {
  sidebar.style.transform = `translate(${translateX}%)`;
  document.querySelector('#overlay').style.filter ='none';
  document.querySelector('nav').style.filter ='none';
  document.body.style.overflowY = 'auto';
}


function ScrollRight(){
  document.querySelector('.card-main').scrollLeft += 226;
}
function ScrollLeft(){
  document.querySelector('.card-main').scrollLeft -= 226;
}

function ScrollRight1(){
  document.querySelector('.card-main1').scrollLeft += 226;
}
function ScrollLeft1(){
  document.querySelector('.card-main1').scrollLeft -= 226;
}

function ScrollRight2(){
  document.querySelector('.card-main2').scrollLeft += 226;
}
function ScrollLeft2(){
  document.querySelector('.card-main2').scrollLeft -= 226;
}

function ScrollRight3(){
  document.querySelector('.card-main3').scrollLeft += 226;
}
function ScrollLeft3(){
  document.querySelector('.card-main3').scrollLeft -= 226;
}

function ScrollRight4(){
  document.querySelector('.card-main4').scrollLeft += 226;
}
function ScrollLeft4(){
  document.querySelector('.card-main4').scrollLeft -= 226;
}



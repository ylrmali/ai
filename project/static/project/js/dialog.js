const modal = document.getElementById('modal');
const popupBtn = document.getElementById('popupBtn');
const backdrop = document.getElementById('backdrop');

popupBtn.addEventListener('click', ()=>{
    console.log('clicked');
    backdrop.classList.add('active');
    modal.style.display = 'flex';
});
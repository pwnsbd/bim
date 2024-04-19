const image = document.getElementById('image');
const slider = document.getElementById('exposure');

slider.oninput = function() {
    const exposureValue = this.value;
    image.style.filter = `brightness(${exposureValue}%)`;
};

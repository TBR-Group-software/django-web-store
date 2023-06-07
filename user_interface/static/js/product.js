function selectSize(obj){
    activateAddToCartButton();
}

function activateAddToCartButton(){
    const addToCartButton = document.querySelector('#addToCartButton');
    addToCartButton.classList.remove('disabled')
    addToCartButton.disabled = false;
}

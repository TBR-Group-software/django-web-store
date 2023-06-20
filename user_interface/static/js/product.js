function selectSize(obj) {
    activateAddToCartButton();
}

function activateAddToCartButton() {
    const addToCartButton = document.getElementById('addToCartButton');
    addToCartButton.classList.remove('disabled')
    addToCartButton.disabled = false;
}


function addToCart() {
    const addToCartButton = document.getElementById('addToCartButton')
    if (addToCartButton.disabled == false) {
        let xhttp = new XMLHttpRequest();
        xhttp.onerror = function () {
            createAlert('danger', this.responseText);
            return false
        }

        xhttp.onload = function () {
            console.log(this);
            if (this.status != 200) {
                createAlert('danger', this.responseText);
                return false
            }
            createAlert('primary', "Product added to cart !");
            return true
        }

        const slug = new URL(document.URL).pathname.split('/').pop();

        const postJSON = JSON.stringify({ "product_parameter_value": getSelectedSize(), 'product_slug': slug});

        xhttp.open("POST", `/add_to_cart/`, true);
        xhttp.setRequestHeader('Content-type', 'application/json; charset=UTF-8');
        xhttp.setRequestHeader('X-CSRFToken', getCookie('csrftoken'));
        xhttp.send(postJSON);

        return true;
    }
}

function getSelectedSize() {
    const sizeContainer = document.querySelector('.product-size-container');
    const selectedSize = sizeContainer.querySelector('input[name="size"]:checked').value;
    return selectedSize;
}

document.addEventListener('DOMContentLoaded', function () {
    const addToCartButton = document.getElementById('addToCartButton')
    addToCartButton.addEventListener('click', addToCart)

})

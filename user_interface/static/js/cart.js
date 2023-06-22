

function calculateSubtotal() {
    const productPrices = document.querySelectorAll('.product-price');
    let newSubtotal = 0;
    productPrices.forEach(price => {
        newSubtotal += parseInt(price.innerHTML);
    })
    return newSubtotal
}

document.addEventListener('DOMContentLoaded', function () {
    const plusButtons = document.querySelectorAll('.plus-item');
    console.log(plusButtons)
    plusButtons.forEach(function (plusButton) {
        plusButton.addEventListener('click', function () {
            const productContainter = plusButton.parentElement.parentElement.parentElement.parentElement.parentElement;
            const cartAmmountId = parseInt(productContainter.querySelector('input[name="cart-ammount-id"]').value);
            const productAmmountElement = productContainter.querySelector('.product-ammount');
            const productAmmount = parseInt(productAmmountElement.innerHTML);
            const productPriceElement = productContainter.querySelector('.product-price');
            const defaultProductPrice = parseInt(productContainter.querySelector('input[name="default-product-price"]').value)
            const subtotalElement = document.querySelector('.subtotal');

            productAmmountElement.innerHTML = productAmmount + 1;
            productPriceElement.innerHTML = defaultProductPrice * (productAmmount + 1);

            subtotalElement.innerHTML = calculateSubtotal();
        });

    });
})

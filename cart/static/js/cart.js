function calculateSubtotal() {
    const productPrices = document.getElementsByClassName('product-price');
    let newSubtotal = 0;
    Array.from(productPrices).forEach(price => {
      newSubtotal += +price.innerHTML;
    });
    return newSubtotal;
  }

  function updateProductDetails(productContainer, amountChange) {
    const productAmountElement = productContainer.getElementsByClassName('product-amount')[0];
    const productPriceElement = productContainer.getElementsByClassName('product-price')[0];
    const defaultProductPrice = +productContainer.querySelector('input[name="default-product-price"]').value;

    let productAmount = +productAmountElement.innerHTML + amountChange;

    if (productAmount > 0) {
      productAmountElement.innerHTML = productAmount;
      productPriceElement.innerHTML = defaultProductPrice * productAmount;
    } else {
      createAlert('danger', 'You cannot have a negative product amount');
    }
  }

  async function sendUpdatedProductDetails(cartAmountId, operationType) {
    try {
      const response = await fetch('/cart/edit/', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json; charset=UTF-8',
          'X-CSRFToken': getCookie('csrftoken')
        },
        body: JSON.stringify({ "cart_amount_id": cartAmountId, 'operation_type': operationType })
      });

      if (!response.ok) {
        const errorMessage = await response.text();
        createAlert('danger', errorMessage);
        return false;
      }

      return true;
    } catch (error) {
      createAlert('danger', error.message);
      return false;
    }
  }

  document.addEventListener('DOMContentLoaded', function () {
    const plusButtons = document.getElementsByClassName('plus-item');
    const minusButtons = document.getElementsByClassName('minus-item');
    const removeButtons = document.getElementsByClassName('remove-item');
    const subtotalElement = document.querySelector('.subtotal');

    Array.from(plusButtons).forEach(plusButton => {
      plusButton.addEventListener('click', async () => {
        const productContainer = plusButton.closest('.product-container');
        const cartAmountId = +productContainer.querySelector('input[name="cart-amount-id"]').value;

        if (await sendUpdatedProductDetails(cartAmountId, "cart_plus")) {
          updateProductDetails(productContainer, 1);
          subtotalElement.innerHTML = calculateSubtotal();
        }
      });
    });

    Array.from(minusButtons).forEach(minusButton => {
      minusButton.addEventListener('click', async () => {
        const productContainer = minusButton.closest('.product-container');
        const cartAmountId = +productContainer.querySelector('input[name="cart-amount-id"]').value;

        if (await sendUpdatedProductDetails(cartAmountId, "cart_minus")) {
          updateProductDetails(productContainer, -1);
          subtotalElement.innerHTML = calculateSubtotal();
        }
      });
    });

    Array.from(removeButtons).forEach(removeButton => {
      removeButton.addEventListener('click', async () => {
        const productContainer = removeButton.closest('.product-container');
        const cartAmountId = +productContainer.querySelector('input[name="cart-amount-id"]').value;

        if (await sendUpdatedProductDetails(cartAmountId, "cart_remove")) {
          productContainer.remove();
          subtotalElement.innerHTML = calculateSubtotal();
          minusCartItemCount()
        }
      });
    });
  });

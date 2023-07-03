function closeAlert() {
    const alertElement = document.querySelector('.alert');
    if (alertElement !== null) {
        const bsAlert = new bootstrap.Alert(alertElement);
        setTimeout(() => {
            bsAlert.close();
        }, 5000);
    }
}

function createAlert(type, message) {
    const alert = document.createElement('div');
    alert.classList.add('alert', `alert-${type}`, 'alert-dismissible', 'fade', 'show', 'position-absolute', 'message-alert');

    alert.innerHTML = message;

    const closeButton = createCloseButton();
    alert.appendChild(closeButton);

    const container = document.querySelector('.content');
    container.prepend(alert);

    closeAlert();

    return alert;
}

function capitalizeFirstLetter(string) {
    return string.charAt(0).toUpperCase() + string.slice(1);
}

function createCloseButton() {
    const closeButton = document.createElement('button');
    closeButton.classList.add('btn-close');
    closeButton.setAttribute('type', 'button');
    closeButton.setAttribute('data-bs-dismiss', 'alert');
    return closeButton;
}

const getCookie = function (cName) {
    const name = cName + "=";
    const cDecoded = decodeURIComponent(document.cookie);
    const cArr = cDecoded.split('; ');
    let res;
    cArr.forEach(val => {
        if (val.indexOf(name) === 0) res = val.substring(name.length);
    });
    return res;
}


function changeCartItemCount(ItemCount) {
    const cartItemLinkElement = document.querySelector('.cart-link');

    let cartItemCountElement = cartItemLinkElement.querySelector('.item-cart-count');

    if (ItemCount <= 0) {
        if (cartItemCountElement) {
            cartItemCountElement.remove()
        }
        return ItemCount
    }

    if (cartItemCountElement) {
        cartItemCountElement.innerHTML = ItemCount;
        return cartItemCountElement
    }
    else {
        const newCartItemCountElement = document.createElement('i');

        newCartItemCountElement.classList.add('item-cart-count', 'position-absolute');
        newCartItemCountElement.innerHTML = ItemCount;
        cartItemLinkElement.appendChild(newCartItemCountElement);
        return newCartItemCountElement;
    }
}

function getCartItemCount() {
    let cartItemCountElement = document.querySelector('.item-cart-count');
    if (cartItemCountElement) {
        return parseInt(cartItemCountElement.innerHTML)
    }
    return 0
}

function addCartItemCount() {
    return changeCartItemCount(getCartItemCount() + 1);
}

function minusCartItemCount() {
    return changeCartItemCount(getCartItemCount() - 1);
}

function updateURLFilter(key, value, addFilter, url) {
    const newUrl = new URL(url || window.location.href);
    const searchParams = newUrl.searchParams;

    if (addFilter) {
        searchParams.append(key, value);
    } else {
        const values = searchParams.getAll(key);
        searchParams.delete(key);
        const updatedValues = values.filter(val => val !== value);
        updatedValues.forEach(updatedValue => searchParams.append(key, updatedValue));
    }

    return newUrl;
}

function navigateToUrl(url) {
    window.location.href = url;
}

function updateFilter(key, oldValue, newValue, url, navigate) {
    const updatedUrl = updateURLFilter(key, oldValue, false, url?.href);
    const newUrl = updateURLFilter(key, newValue, true, updatedUrl.href);

    if (navigate) {
        navigateToUrl(newUrl.href);
    } else {
        return newUrl;
    }
}

function addFilter(key, value, url, navigate) {
    const newUrl = updateURLFilter(key, value, true, url);
    if (navigate) {
        navigateToUrl(newUrl.href);
    } else {
        return newUrl;
    }
}

function deleteFilter(key, value, url, navigate) {
    const newUrl = updateURLFilter(key, value, false, url);
    if (navigate) {
        navigateToUrl(newUrl.href);
    } else {
        return newUrl;
    }
}

function hardDeleteFilter(key, url, navigate) {
    const newUrl = new URL(url || window.location.href);
    const searchParams = newUrl.searchParams;

    searchParams.delete(key);

    if (navigate) {
        navigateToUrl(newUrl.href);
    } else {
        return newUrl;
    }
}

function updateFilters(keyValues, newUrl) {
    for (const [key, oldValue, newValue] of keyValues) {
        newUrl = updateFilter(key, oldValue, newValue, newUrl, false);
    }

    navigateToUrl(newUrl.href);
}

function setPriceFilters() {
    const minPrice = parseInt(document.querySelector('#min-price').value);
    const maxPrice = parseInt(document.querySelector('#max-price').value);

    if ((isNaN(minPrice) || isNaN(maxPrice)) && (minPrice > maxPrice) || (minPrice === '' && maxPrice === '')) {
        createAlert('danger', 'invalid price filter');
        return;
    }

    let newUrl = hardDeleteFilter('minPrice', null, false);
    newUrl = hardDeleteFilter('maxPrice', newUrl, false);

    if (!isNaN(minPrice)) {
        newUrl = addFilter('minPrice', minPrice, newUrl, false);
    }
    if (!isNaN(maxPrice)) {
        newUrl = addFilter('maxPrice', maxPrice, newUrl, false);
    }
    navigateToUrl(newUrl.href);
}

document.addEventListener('DOMContentLoaded', function () {
    const filterButton = document.getElementById('filter-button');
    filterButton.addEventListener('click', setPriceFilters);

    const checkboxes = document.querySelectorAll('input[type="checkbox"]');
    checkboxes.forEach(function (checkbox) {
        checkbox.addEventListener('change', function () {
            const key = checkbox.name;
            const value = checkbox.value;
            const checked = checkbox.checked;

            if (checked) {
                addFilter(key, value, null, true);
            } else {
                deleteFilter(key, value, null, true);
            }
        });

    });
});

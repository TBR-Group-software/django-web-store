function modifyFilter(key, value, addFilter) {
    const { href } = window.location;
    const url = new URL(href);
    const searchParams = url.searchParams;

    if (addFilter) {
        searchParams.append(key, value);
    } else {
        const values = searchParams.getAll(key);
        searchParams.delete(key);

        const updatedValues = values.filter(val => val !== value);
        updatedValues.forEach(updatedValue => searchParams.append(key, updatedValue));
    }

    window.location.href = url.href;
}

function addFilter(key, value) {
    modifyFilter(key, value, true);
}

function deleteFilter(key, value) {
    modifyFilter(key, value, false);
}

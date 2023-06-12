function setFilter(key, value) {
    let url = new URL(window.location.href)
    url.searchParams.append(key, value);
    window.location.href = url.href;
}

function removeFilter(key, value) {
    let url = new URL(window.location.href)
    url.searchParams.delete(key, value);
    window.location.href = url.href;
}

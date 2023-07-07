document.addEventListener('DOMContentLoaded', function () {
    const ratingMeters = document.getElementsByClassName('rating-meter');
    for (let ratingMeter of ratingMeters) {
        ratingMeter.style.setProperty('--rating-value', ratingMeter.getAttribute('value'));
    };
});

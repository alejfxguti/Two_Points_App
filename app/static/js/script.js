document.addEventListener('DOMContentLoaded', function () {
    const form = document.querySelector('#distance-form');
    const resultParagraph = document.querySelector('#result');

    form.addEventListener('submit', function (e) {
        e.preventDefault();
        const startLocation = document.querySelector('#start-location').value;
        const endLocation = document.querySelector('#end-location').value;

        fetch('/calculate_distance', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({
                start_location: startLocation,
                end_location: endLocation,
            }),
        })
            .then((response) => response.json())
            .then((data) => {
                if (data.error) {
                    resultParagraph.textContent = `Error: ${data.error}`;
                } else {
                    resultParagraph.textContent = `Distance: ${data.distance} miles`;
                }
            })
            .catch((error) => {
                console.error('Error:', error);
                resultParagraph.textContent = 'An error occurred while calculating the distance.';
            });
    });
});

document.addEventListener('DOMContentLoaded', function () {
    const rockets = document.querySelectorAll('.rocket');
    const launchButton = document.getElementById('launchButton');

    let selectedRockets = [];

    rockets.forEach((rocket) => {
        rocket.addEventListener('click', () => {
            toggleRocketSelection(rocket);
        });
    });

    launchButton.addEventListener('mousedown', () => {
        launchSelectedRockets();
    });
    launchButton.addEventListener('touchstart', () => {
        launchSelectedRockets();
    });
    launchButton.addEventListener('mouseup', () => {
        launchButton.style.backgroundImage = "url('../static/war_bakuha_switch_off.png')";
    });
    launchButton.addEventListener('touchend', () => {
        launchButton.style.backgroundImage = "url('../static/war_bakuha_switch_off.png')";
    });

    function toggleRocketSelection(rocket) {
        if (selectedRockets.includes(rocket)) {
            selectedRockets = selectedRockets.filter(selectedRocket => selectedRocket !== rocket);
        } else {
            selectedRockets.push(rocket);
        }
        rocket.classList.toggle('selected');
    }

    function launchSelectedRockets() {
        if (selectedRockets.length > 0) {
            launchButton.style.backgroundImage = "url('../static/war_bakuha_switch_on.png')";
            // alert(`Launching ${selectedRockets.length} rocket(s)!`);
            // fetch('/api/launch', {
            //     method: 'POST',
            //     headers: {
            //         'Content-Type': 'application/json',
            //     },
            //     body: JSON.stringify(joystick.value),
            // })
            //     .then(response => response.json())
            //     .then(data => {
            //         console.log('Response from server:', data);
            //     })
            //     .catch(error => {
            //         console.error('Error:', error);
            //     });
        } else {
            // alert('Please select at least one rocket to launch.');
        }
    }
});
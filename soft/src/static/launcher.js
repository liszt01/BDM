document.addEventListener('DOMContentLoaded', function () {
    const launchButton = document.getElementById('launchButton');

    let totalAmmo = 8;
    let remainingAmmo = 8;

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

    function launchSelectedRockets() {
        if (remainingAmmo > 0) {
            launchButton.style.backgroundImage = "url('../static/war_bakuha_switch_on.png')";
            // alert(`Launching ${selectedRockets.length} rocket(s)!`);
            // 選択されたロケットのIDだけを抽出してJSON形式のリストに変換
            fetch('/api/launch', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
            })
                .then(response => response.json())
                .then(data => {
                    console.log('Response from server:', data);
                    totalAmmo = data['totalAmmo']
                    remainingAmmo = data['remainingAmmo']
                })
                .catch(error => {
                    console.error('Error:', error);
                });
            document.getElementById("ammo").innerText = JSON.stringify(remainingAmmo) + "/" + JSON.stringify(totalAmmo);
        } else {
            // alert('Please select at least one rocket to launch.');
        }
    }
});
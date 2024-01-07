const launchButton = document.getElementById('launchButton');

let totalAmmo;
let remainingAmmo;

window.addEventListener('load', function () {
    fetch('/api/reload', {
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
            document.getElementById("ammo").innerText = `${remainingAmmo}/${totalAmmo}`;
        })
        .catch(error => {
            console.error('Error:', error);
        });
});

launchButton.addEventListener('mousedown', () => {
    launchSelectedRockets();
});
launchButton.addEventListener('touchstart', () => {
    launchSelectedRockets();
});
launchButton.addEventListener('mouseup', () => {
    launchButton.src = '../static/war_bakuha_switch_off.png';
});
launchButton.addEventListener('touchend', () => {
    launchButton.src = '../static/war_bakuha_switch_off.png';
});

function launchSelectedRockets() {
    if (remainingAmmo > 0) {
        launchButton.src = '../static/war_bakuha_switch_on.png';
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
                document.getElementById("ammo").innerText = `${remainingAmmo}/${totalAmmo}`;
            })
            .catch(error => {
                console.error('Error:', error);
            });
    } else {
        // alert('Please select at least one rocket to launch.');
    }
}

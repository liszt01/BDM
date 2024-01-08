class LaunchButtonController {
    constructor(buttonID) {
        this.id = buttonID;
        let launchButton = document.getElementById(buttonID);

        this.value = { totalAmmo: 0, remainingAmmo: 0 };
        this.disabled = false;

        let self = this;

        function handleFetch(action) {
            fetch(`/api/${action}`, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
            })
                .then(response => response.json())
                .then(data => {
                    console.log('Response from server:', data);
                    self.value.totalAmmo = data['totalAmmo'];
                    self.value.remainingAmmo = data['remainingAmmo'];
                    document.getElementById("ammo").innerText = `${self.value.remainingAmmo}/${self.value.totalAmmo}`;
                })
                .catch(error => {
                    console.error('Error:', error);
                });
        }

        function handlePush() {
            if (self.value.remainingAmmo <= 0 || self.disabled) return;

            self.disabled = true;
            launchButton.src = '../static/war_bakuha_switch_on.png';
            handleFetch('launch');
            setTimeout(function () {
                self.disabled = false;
            }, 5000);
        }
        function handleRelease() {
            launchButton.src = '../static/war_bakuha_switch_off.png';
        }

        launchButton.addEventListener('mousedown', handlePush);
        launchButton.addEventListener('touchstart', handlePush);
        launchButton.addEventListener('mouseup', handleRelease);
        launchButton.addEventListener('touchend', handleRelease);
        window.addEventListener('load', handleFetch('reload'));
    }
}

let launchButton = new LaunchButtonController('launchButton');

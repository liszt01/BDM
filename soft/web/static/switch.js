class ModeSwitchController {
    constructor(buttonID) {
        this.id = buttonID;
        let modeSwitch = document.getElementById(buttonID);

        let self = this;

        function handleFetch() {
            fetch(`/api/advanced`, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
            })
                .then(response => response.json())
                .then(data => {
                    console.log('Response from server:', data);
                })
                .catch(error => {
                    console.error('Error:', error);
                });
        }

        function handlePush() {
            handleFetch();
        }

        modeSwitch.addEventListener('mousedown', handlePush);
        modeSwitch.addEventListener('touchstart', handlePush);
    }
}

let modeSwitch = new ModeSwitchController('modeSwitch');
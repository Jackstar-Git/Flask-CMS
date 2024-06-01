const passwordInput = document.getElementById('password');
const progressBar = document.querySelector('.progress-bar');
const showPasswordCheckbox = document.getElementById('show-password');



function calculatePasswordStrength(password) {
    const hasNumber = /[0-9]/.test(password);
    const hasSymbol = /[!@#$%^&*()_+\-=\[\]{};':"\\|,.<>\/?]+/.test(password);
    const length = password.length;

    if (length >= 11 && hasNumber && hasSymbol) {
        return 4;
    } else if (length >= 10 && (hasNumber || hasSymbol)) {
        return 3;
    } else if (length >= 10) {
        return 2;
    } else if (length >= 8) {
        return 1;
    } else {
        return 0;
    }
}

function getProgressBarColor(strength) {
    switch (strength) {
        case 0:
            return '#ccc';
        case 1:
            return '#ff4d4d';
        case 2:
            return '#ffad33';
        case 3:
            return '#faef16';
        case 4:
            return '#66ff66';
        default:
            return '#ccc';
    }
}

passwordInput.addEventListener('input', function() {
    const password = this.value;
    const strength = calculatePasswordStrength(password);
    progressBar.style.width = `${strength * 25}%`;
    progressBar.style.backgroundColor = getProgressBarColor(strength);
});

showPasswordCheckbox.addEventListener('change', function() {
    const isChecked = this.checked;
    if (isChecked) {
        passwordInput.type = 'text';
    } else {
        passwordInput.type = 'password';
    }
});

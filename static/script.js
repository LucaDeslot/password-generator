document.getElementById('passwordInput').addEventListener('input', function() {
    const password = this.value;
    checkPasswordStrength(password);
});

let isWeakPassword = false;

function checkPasswordStrength(password) {
    fetch('/verify_password_strength', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({password: password}),
    })
    .then(response => response.json())
    .then(data => {
        let resultText = `Strength: ${data.result}`;
        isWeakPassword = data.result.toLowerCase() === 'weak';

        // Affiche les critères manquants
        if (data.missing && data.missing.length > 0) {
            resultText += `\nMissing: ${data.missing.join(', ')}`;
        }

        // Utilisez innerHTML pour les sauts de ligne avec <br> si vous voulez garder le formatage
        document.getElementById('strengthResult').innerHTML = resultText.replace(/\n/g, '<br>');
    });
}

const copyButton = document.getElementById('copyButton');
copyButton.addEventListener('mouseenter', function() {
    if (!isWeakPassword) return;

    const viewportWidth = window.innerWidth;
    const viewportHeight = window.innerHeight;

    // Calcule une position aléatoire à l'intérieur de la fenêtre
    let randomX = Math.random() * (viewportWidth - copyButton.offsetWidth);
    let randomY = Math.random() * (viewportHeight - copyButton.offsetHeight);

    // Déplacer le bouton à la position aléatoire
    copyButton.style.position = 'absolute';
    copyButton.style.left = `${randomX}px`;
    copyButton.style.top = `${randomY}px`;
});

function copyPassword() {
    const passwordInput = document.getElementById('passwordInput');
    passwordInput.select();
    document.execCommand('copy');
}

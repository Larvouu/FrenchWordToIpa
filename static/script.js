function getPhonemes() {
    for (let i = 0; i < 10; i++) {
        const input = document.getElementById(`wordInput${i}`);
        const result = document.getElementById(`result${i}`);
        const word = input.value.trim();

        if (word) { // Vérifie que le champ n'est pas vide
            const apiUrl = `http://localhost:5000/getIPA?word=${encodeURIComponent(word)}`;
            fetch(apiUrl)
                .then(response => {
                    if (response.ok) {
                        return response.json();
                    }
                    throw new Error('Réponse du serveur non réussie');
                })
                .then(data => {
                    result.textContent = data.ipa;
                })
                .catch(error => {
                    console.error('Erreur lors de la récupération des phonèmes:', error);
                    result.textContent = 'Erreur: ' + error.message;
                });
        } else {
            result.textContent = ''; // Nettoyer si le champ est vide
        }
    }
}

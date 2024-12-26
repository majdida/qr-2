// Function to switch the language
function changeLanguage(lang) {
    // Fetch the translations from languages.json
    fetch('languages.json')
        .then(response => response.json())
        .then(translations => {
            // Loop through all elements with a data-key attribute
            document.querySelectorAll('[data-key]').forEach(element => {
                // Get the key from the element's data-key attribute
                const key = element.getAttribute('data-key');
                // Replace the text content with the translation for the selected language
                if (translations[lang] && translations[lang][key]) {
                    element.textContent = translations[lang][key];
                }
            });
        })
        .catch(err => {
            console.error('Error loading translations:', err);
        });
}

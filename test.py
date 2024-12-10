# Mauvais exemple - Ne pas inclure de clés API en clair dans le code source
AWS_API_KEY = "AKIAEXAMPLE1234567890"

def use_api():
    print(f"Using API key: {AWS_API_KEY}")
    # Simulate API call

use_api()

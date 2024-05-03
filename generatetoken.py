import secrets

token = secrets.token_urlsafe(256)
print(token)


# Note: The code above generates a random token using the secrets module. The token is then printed to the console.
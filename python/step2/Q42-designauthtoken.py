# Design Authentication Manager **Unique**
#     - The Authentication Manager problem involves designing a system that manages authentication tokens
# with expiration times. The system should support operations to add new tokens, renew existing tokens, and 
# count valid tokens at any point in time.

# Problem Description
# You are tasked to implement an AuthenticationManager class:

# Constructor:

# AuthenticationManager(timeToLive: int): Initializes the manager with a fixed timeToLive (in seconds). This is the duration for which a token remains valid after being generated or renewed.
# Methods:

# generate(tokenId: str, currentTime: int): Generates a new token with the given tokenId at currentTime. The token will expire after currentTime + timeToLive.
# renew(tokenId: str, currentTime: int): Renews the token with the given tokenId if it is still valid at currentTime. If valid, its expiration time is extended to currentTime + timeToLive. If it has expired or does not exist, nothing happens.
# countUnexpiredTokens(currentTime: int): Returns the count of all unexpired tokens at currentTime.

# Key Idea
# To efficiently manage tokens:

# Use a dictionary to store tokens with their expiration times.

# Key: tokenId
# Value: expirationTime
# When renewing or counting tokens:

# Check if the current time is less than the token's expiration time. Expired tokens can be ignored.
# Operations must be efficient, so all operations should ideally work in O(1) time.

class AuthenticationManager:
    def __init__(self, timeToLive: int):
        self.timeToLive = timeToLive
        self.tokens = {}  # Dictionary to store tokenId -> expirationTime

    def generate(self, tokenId: str, currentTime: int) -> None:
        self.tokens[tokenId] = currentTime + self.timeToLive

    def renew(self, tokenId: str, currentTime: int) -> None:
        # Renew only if the token exists and is not expired
        if tokenId in self.tokens and self.tokens[tokenId] > currentTime:
            self.tokens[tokenId] = currentTime + self.timeToLive

    def countUnexpiredTokens(self, currentTime: int) -> int:
        # Count tokens whose expiration time is greater than currentTime
        return sum(expirationTime > currentTime for expirationTime in self.tokens.values())

# Example Test Case
manager = AuthenticationManager(5)  # Tokens have a time-to-live of 5 seconds

manager.generate("token1", 1)  # token1 expires at time 6
manager.generate("token2", 2)  # token2 expires at time 7

print(manager.countUnexpiredTokens(6))  # Output: 1 (only token2 is valid)
manager.renew("token2", 6)  # token2 is renewed, now expires at time 11
print(manager.countUnexpiredTokens(7))  # Output: 1 (only token2 is valid)

manager.generate("token3", 8)  # token3 expires at time 13
print(manager.countUnexpiredTokens(9))  # Output: 2 (token2 and token3 are valid)

# Complexity

# Time Complexity:
# generate: O(1)
# renew: O(1)
# countUnexpiredTokens: O(n), where n is the number of tokens (iterate over all tokens).

# # Space Complexity: O(n), where n is the number of tokens stored in the dictionary.

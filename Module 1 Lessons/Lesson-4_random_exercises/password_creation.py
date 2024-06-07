# Import the random and string modules
# Combine uppercase letters, lowercase letters, digits, and punctuation to create a pool of characters
# Use a loop to randomly select 8 characters from the pool to form a password. 
# Print out the generated password

import random
import string

characters = string.ascii_letters + string.digits + string.punctuation

password = ''.join(random.choice(characters) for _ in range(8))

print(f"Generated password: {password}")
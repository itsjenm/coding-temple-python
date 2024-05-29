emails = ["user1@example.com", None, "user2@example.com", "user3@example.com", None]

valid_emails = []

for email in emails:
    if email is None: 
        continue
    valid_emails.append(email)

print("valid emails: ", valid_emails)

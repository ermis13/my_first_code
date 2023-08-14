import random

def generate_password(length):
  characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()_+-="
  password = ""
  for i in range(length):
    password += random.choice(characters)
  return password

def main():
  password_length = int(input("Enter the length of the password you want to generate: "))
  password = generate_password(password_length)
  print("Your password is:", password)

if __name__ == "__main__":
  main()

# def character_frequency(filename):
#   """Counts the frequency of each character in the given file."""
#   # First try to open the file
#   try:
#     f = open(filename)
#   except OSError:
#     print("File not found")
#     return None

#   # Now process the file
#   characters = {}
#   for line in f:
#     for char in line:
#       characters[char] = characters.get(char, 0) + 1
#   f.close() 
#   return characters

# character_frequency("text.txt")

def validate_user(username, minlen):
  assert type(username) == str, "username must be a string"
  if minlen < 1:
    raise ValueError("minlen must be at least 1")

  if len(username) < minlen:
    return False
  if not username.isalnum():
    return False
  return True

# validate_user("", 1)
# validate_user("myuser", 1)
# validate_user(88, 1)
# validate_user([3], 1)
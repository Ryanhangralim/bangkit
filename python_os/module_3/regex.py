import re

# log = "July 31 07:51:48 mycomputer bad_process[12345]: ERROR Performing package upgrade"
# regex = r"\[(\d+)\]"
# result = re.search(regex, log)
# print(result[1])

# Simple matching
# print(re.search(r"aza", "plaza"))
# print(re.search(r"aza", "bazaar"))
# print(re.search(r"aza", "maze"))
# print(re.search(r"p.ng", "clapping"))
# print(re.search(r"p.ng", "sponge"))
# print(re.search(r"p.ng", "Pangaea", re.IGNORECASE))

# Character classes
# print(re.search(r"[Pp]ython", "python"))
# print(re.search("cloud[a-zA-Z0-9]", "cloudy"))
# print(re.search("cloud[a-zA-Z0-9]", "cloud9"))
# print(re.search(r"[^a-zA-Z]", "This is a sentence with spaces."))
# print(re.search(r"[^a-zA-Z ]", "This is a sentence with spaces."))

# print(re.search(r"cat|dog", "I like cats."))
# print(re.search(r"cat|dog", "I love dogs!"))
# print(re.search(r"cat|dog", "I like both dogs and cats."))

# print(re.search(r"cat|dog", "I like cats."))
# print(re.search(r"cat|dog", "I love dogs!"))
# print(re.search(r"cat|dog", "I like both dogs and cats."))
# print(re.findall(r"cat|dog", "I like both dogs and cats."))

# Repetition qualifiers
# print(re.search(r"Py.*n", "Pygmalion"))
# print(re.search(r"Py.*n", "Python Programming"))
# print(re.search(r"Py[a-z]*n", "Python Programming"))
# print(re.search(r"Py[a-z]*n", "Pyn"))

# print(re.search(r"o+l+", "goldfish"))
# print(re.search(r"o+.+l+", "wodlly"))
# print(re.search(r"o+l+", "boil"))

# print(re.search(r"p?each", "To each their own"))
# print(re.search(r"p?each", "I like peaches"))

# Escaping characers
# print(re.search(r".com", "welcome"))
# print(re.search(r"\.com", "welcome"))
# print(re.search(r"\.com", "mydomain.com"))

# print(re.search(r"\w*", "This is an example"))
# print(re.search(r"\w*", "And_this_is_another"))

# Regular expressions in action
# print(re.search(r"A.*a", "Argentina"))
# print(re.search(r"A.*a", "Azerbaijan"))
# print(re.search(r"^A.*a$", "Australia"))

# pattern = r"^[a-zA-Z_][a-zA-Z0-9_]*$"
# print(re.search(pattern, "_this_is_a_valid_variable_name"))
# print(re.search(pattern, "this isn't a valid variable"))
# print(re.search(pattern, "my_variable1"))
# print(re.search(pattern, "2my_variable1"))

# Advanced REGEX
# Capturing groups
# result = re.search(r"^(\w*), (\w*)$", "Lovelace, Ada")
# print(result)
# print(result.groups())
# print(result[0])
# print(result[1])
# print(result[2])
# "{} {}".format(result[2], result[1])

# def rearrange_name(name):
#     result = re.search(r"^(\w*), (\w*)$", name)
#     if result is None:
#         return name
#     return "{} {}".format(result[2], result[1])
# print(rearrange_name("Lovelace, Ada"))
# print(rearrange_name("Ritchie, Dennis"))

# def rearrange_name2(name):
#     result = re.search(r"^([\w \.-]*), ([\w \.-]*)$", name)
#     if result == None:
#         return name
#     return "{} {}".format(result[2], result[1])
# print(rearrange_name2("Hopper, Grace M."))

# Repetitive qualifiers
# print(re.search(r"[a-zA-Z]{5}", "a ghost"))
# print(re.search(r"[a-zA-Z]{5}", "a scary ghost appeared"))
# print(re.findall(r"[a-zA-Z]{5}", "a scary ghost appeared"))
# print(re.findall(r"\b[a-zA-Z]{5}\b", "A scary ghost appeared"))
# print(re.findall(r"\w{5,10}", "I really like strawberries"))
# print(re.findall(r"\w{5,}", "I really like strawberries"))
# print(re.search(r"s\w{,20}", "I really like strawberries"))

# Extracting PID using regexes in python
# log = "July 31 07:51:48 mycomputer bad_process[12345]: ERROR Performing package upgrade"
# regex = r"\[(\d+)\]"
# result = re.search(regex, log)
# print(result[1])

# log = "July 31 07:51:48 mycomputer bad_process[12345]: ERROR Performing package upgrade"
# regex = r"\[(\d+)\]"
# result = re.search(regex, log)
# result = re.search(regex, "A completely different string that also has numbers [34567]")
# print(result[1])

# log = "July 31 07:51:48 mycomputer bad_process[12345]: ERROR Performing package upgrade"
# regex = r"\[(\d+)\]"
# result = re.search(regex, log)
# result = re.search(regex, "A completely different string that also has numbers [34567]")
# result = re.search(regex, "99 elephants in a [cage]")
# def extract_pid(log_line):
#     regex = r"\[(\d+)\]"
#     result = re.search(regex, log_line)
#     if result is None:
#         return ""
#     return result[1]
# print(extract_pid(log))

# log = "July 31 07:51:48 mycomputer bad_process[12345]: ERROR Performing package upgrade"
# regex = r"\[(\d+)\]"
# result = re.search(regex, log)
# result = re.search(regex, "A completely different string that also has numbers [34567]")
# result = re.search(regex, "99 elephants in a [cage]")
# def extract_pid(log_line):
#     regex = r"\[(\d+)\]"
#     result = re.search(regex, log_line)
#     if result is None:
#         return ""
#     return result[1]
# print(extract_pid(log))
# print(extract_pid("99 elephants in a [cage]"))

# Splitting and replacing
print(re.split(r"[.?!]", "One sentence. Another one? And the last one!"))
# Includes the characters used to split
print(re.split(r"([.?!])", "One sentence. Another one? And the last one!"))
print(re.sub(r"[\w.%+-]+@[\w.-]+", "[REDACTED]", "Received an email for go_nuts95@my.example.com"))
# \2 and \1 to reference the captured group
print(re.sub(r"^([\w .-]*), ([\w .-]*)$", r"\2 \1", "Lovelace, Ada"))
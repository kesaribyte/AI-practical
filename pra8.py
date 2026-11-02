import random
import re

# Pronoun swaps so replies can echo the user's words ("my" -> "your")
REFLECTIONS = {
"i": "you", "me": "you", "my": "your", "mine": "yours", "am": "are",
"you": "I", "your": "my", "yours": "mine", "are": "am",
}

# Each rule: (regex pattern, list of possible responses).
# {0}, {1}... are filled with the regex's captured groups.
# Rules are checked top to bottom; the first match wins.
RULES = [
(r"\b(hello|hi|hey|good (morning|afternoon|evening))\b",
["Hello! How can I help you today?",
"Hi there! What can I do for you?"]),

(r"\bmy name is (\w+)",
["Nice to meet you, {0}!",
"Hello {0}, how are you today?"]),

(r"\bhow are you\b",
["I'm just a program, but I'm running fine. How about you?",
"Doing well, thanks for asking! How are you?"]),

(r"\bi (?:am|feel|'m) (sad|unhappy|depressed|upset|angry|stressed)\b",
["I'm sorry you're feeling {0}. Do you want to talk about it?",

"Why do you think you feel {0}?"]),

(r"\bi (?:am|feel|'m) (happy|great|good|excited|fine)\b",
["That's wonderful to hear! What made you feel {0}?",
"Glad you're feeling {0}!"]),

(r"\bi need (.*)",
["Why do you need {0}?",
"Would getting {0} really help you?"]),

(r"\bi want (.*)",
["What would it mean to you to get {0}?",
"Why do you want {0}?"]),

(r"\bwhat(?:'s| is) your name\b",
["I'm RuleBot, a simple pattern-matching chatbot."]),

(r"\b(?:what can you do|help)\b",
["I can chat using simple rules. Try greeting me, telling me your name, "
"or saying how you feel."]),

(r"\b(?:time|date)\b",
["I don't have a clock, but your device does!"]),

(r"\b(bye|goodbye|exit|quit|see you)\b",
["Goodbye! Have a great day.",
"Bye! It was nice talking to you."]),
]

FALLBACKS = [
"I'm not sure I understand. Could you rephrase that?",
"Tell me more.",
"Interesting. Can you explain a bit more?",
]

def reflect(text):
"""Swap first/second person words in a captured fragment."""
words = text.lower().split()
return " ".join(REFLECTIONS.get(w, w) for w in words)

def respond(user_input):
"""Return a reply for user_input by finding the first matching rule."""
text = user_input.strip()
for pattern, responses in RULES:
match = re.search(pattern, text, re.IGNORECASE)
if match:
groups = [reflect(g) if g else "" for g in match.groups()]
# "my name is X": keep the name's original capitalisation
if pattern.startswith(r"\bmy name is"):
groups = [match.group(1).capitalize()]
return random.choice(responses).format(*groups)
return random.choice(FALLBACKS)

def is_exit(user_input):
return re.search(r"\b(bye|goodbye|exit|quit|see you)\b", user_input, re.I) is not None

def chat():
print("RuleBot: Hi! I'm RuleBot. Type 'bye' to exit.")
while True:
user = input("You: ")
print("RuleBot:", respond(user))
if is_exit(user):
break

if __name__ == "__main__":
import sys
if "--demo" in sys.argv:
random.seed(1)
for line in ["Hello", "My name is alex", "How are you?",
"I feel sad", "I need a vacation", "I want my own car",
"What is your name?", "blah blah", "bye"]:
print("You: ", line)
print("RuleBot:", respond(line), "\n")
else:
chat()

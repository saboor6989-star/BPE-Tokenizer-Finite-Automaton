from tokenizer import BPETokenizer
from automata import TokenAutomaton


# Train tokenizer

tokenizer = BPETokenizer("corpus.txt")

tokenizer.load_corpus()

tokenizer.build_character_vocabulary()

tokenizer.train(10)

learned_tokens = tokenizer.get_learned_tokens()


# Build automaton

automaton = TokenAutomaton()

for token in learned_tokens:

    automaton.add_token(token)


# Results

print("\n===== LEARNED TOKENS =====\n")

print(tokenizer.get_learned_tokens())

for token in learned_tokens:

    print(token)

automaton.show_automaton()
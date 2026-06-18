from collections import defaultdict


class BPETokenizer:

    def __init__(self, corpus_file):

        self.corpus_file = corpus_file

        self.corpus = ""

        self.character_words = []

        self.merge_rules = []

        self.vocabulary = set()

    def load_corpus(self):

        with open(self.corpus_file, "r", encoding="utf-8") as file:

            self.corpus = file.read()

    def build_character_vocabulary(self):

        words = self.corpus.split()

        self.character_words = []

        for word in words:

            self.character_words.append(list(word))

    def count_pair_frequencies(self):

        pair_counts = defaultdict(int)

        for word in self.character_words:

            for i in range(len(word) - 1):

                pair = (word[i], word[i + 1])

                pair_counts[pair] += 1

        return pair_counts
    
    def merge_pair(self, pair_to_merge):

        first, second = pair_to_merge

        merged_token = first + second

        updated_words = []

        for word in self.character_words:

            new_word = []

            i = 0

            while i < len(word):

                if (
                    i < len(word) - 1
                    and word[i] == first
                    and word[i + 1] == second
                ):

                    new_word.append(merged_token)

                    i += 2

                else:

                    new_word.append(word[i])

                    i += 1

            updated_words.append(new_word)

        self.character_words = updated_words

        self.merge_rules.append(pair_to_merge)

    def train(self, num_merges=10):

        for step in range(num_merges):

            pair_counts = self.count_pair_frequencies()

            if not pair_counts:
                break

            most_frequent_pair = max(
                pair_counts,
                key=pair_counts.get
            )

            print(
                f"Merge {step + 1}: "
                f"{most_frequent_pair} "
                f"Frequency = {pair_counts[most_frequent_pair]}"
            )

            self.merge_pair(most_frequent_pair)
        
        self.build_vocabulary()

    def build_vocabulary(self):

        self.vocabulary = set()

        for word in self.character_words:

            for token in word:

                self.vocabulary.add(token)

    def get_learned_tokens(self):

        return sorted(
            list(self.vocabulary),
            key=len,
            reverse=True
        )

    def show_merge_rules(self):

        print("\n===== LEARNED MERGE RULES =====\n")

        for index, rule in enumerate(self.merge_rules, start=1):

            print(f"{index}. {rule[0]} + {rule[1]}")

    def tokenize_word(self, word):

        tokens = list(word)

        for first, second in self.merge_rules:

            merged_token = first + second

            i = 0

            while i < len(tokens) - 1:

                if tokens[i] == first and tokens[i + 1] == second:

                    tokens[i] = merged_token

                    del tokens[i + 1]

                else:

                    i += 1

        return tokens

    def show_statistics(self):

        print("\n===== TOKENIZER STATISTICS =====")

        print("Total Words:", len(self.character_words))

        print("Merge Rules Learned:", len(self.merge_rules))

        print("Vocabulary Size:", len(self.vocabulary))




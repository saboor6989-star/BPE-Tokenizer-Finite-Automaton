class TokenAutomaton:

    def __init__(self):

        self.states = {}

        self.next_state = 1

    def add_token(self, token):

        current_state = 0

        for char in token:

            key = (current_state, char)

            if key not in self.states:

                self.states[key] = self.next_state

                self.next_state += 1

            current_state = self.states[key]

    def show_automaton(self):

        print("\n===== AUTOMATON TRANSITIONS =====\n")

        for (state, char), next_state in self.states.items():

            print(
                f"q{state} --{char}--> q{next_state}"
            )

    def get_transitions(self):

        return self.states
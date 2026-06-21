class TuringMachine:

    def __init__(self, tokens):

        self.tape = tokens + ["_"]

        self.head = 0

        self.state = "q0"

        self.state_history = ["q0"]

    def run(self):

        print("\n===== TURING MACHINE SIMULATION =====\n")

        print("Tape:")

        print(self.tape)

        print()

        while self.head < len(self.tape) - 1:

            current_symbol = self.tape[self.head]

            print(
                f"Head Position: {self.head}"
            )

            print(
                f"State {self.state} reads "
                f"'{current_symbol}'"
            )

            state_number = int(
                self.state[1:]
            )

            self.state = f"q{state_number + 1}"

            self.state_history.append(
                self.state
            )

            print(
                f"Transition -> {self.state}"
            )

            print("Move Right\n")

            self.head += 1

        print(
            f"Reached ACCEPT STATE: "
            f"{self.state}"
        )

        print()

        print(
            "State Path: "
            + " -> ".join(self.state_history)
        )
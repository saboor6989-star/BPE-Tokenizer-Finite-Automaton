from graphviz import Digraph
from automata import TokenAutomaton


automaton = TokenAutomaton()

sample_tokens = [
    "in",
    "ing",
    "learn",
    "token",
    "auto"
]

for token in sample_tokens:

    automaton.add_token(token)


dot = Digraph()

transitions = automaton.get_transitions()

all_states = set()

for (state, char), next_state in transitions.items():

    all_states.add(state)

    all_states.add(next_state)


for state in all_states:

    dot.node(f"q{state}")


for (state, char), next_state in transitions.items():

    dot.edge(
        f"q{state}",
        f"q{next_state}",
        label=char
    )


dot.render(
    "real_automaton",
    format="png",
    view=True
)

print("Automaton visualization generated!")
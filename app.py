import streamlit as st

from tokenizer import BPETokenizer
from automata import TokenAutomaton
from graphviz import Digraph
from turing_machine import TuringMachine


st.title("📚 BPE Tokenizer & Finite Automaton")

st.markdown(
    """
    ### Tokenization as Finite-State Transduction

    This project demonstrates:
    - Byte Pair Encoding (BPE) Tokenization
    - Vocabulary Learning
    - Merge Rule Generation
    - Finite Automaton Construction
    - Automaton Visualization
    """
)


st.write(
    "Implementation of the research paper: "
    "'Tokenization as Finite-State Transduction'"
)

# Load and train tokenizer

tokenizer = BPETokenizer("corpus.txt")

tokenizer.load_corpus()

tokenizer.build_character_vocabulary()

tokenizer.train(10)

# User Input

user_text = st.text_input(
    "Enter a word:",
    "learning"
)

if user_text:

    tokens = tokenizer.tokenize_word(user_text)

    st.success("Tokenization Completed Successfully")
    st.subheader("Tokenization Result")

    st.write(tokens)

    st.subheader("📖 Learned Tokens")

    st.write(tokenizer.get_learned_tokens())

    st.subheader("🔗 Merge Rules")

    for index, rule in enumerate(
        tokenizer.merge_rules,
        start=1
    ):

        st.write(
            f"{index}. {rule[0]} + {rule[1]}"
        )

    st.subheader("📊 Statistics")

    st.write(
        f"Total Words: {len(tokenizer.character_words)}"
    )

    st.write(
        f"Merge Rules Learned: {len(tokenizer.merge_rules)}"
    )

    st.write(
        f"Vocabulary Size: {len(tokenizer.vocabulary)}"
    )

    automaton = TokenAutomaton()

    for token in tokenizer.get_learned_tokens():

        automaton.add_token(token)

    st.subheader("🤖 Automaton Information")

    st.write(
        f"Number of States: {automaton.next_state}"
    )

    st.write(
        f"Number of Transitions: "
        f"{len(automaton.get_transitions())}"
    )

    st.subheader("Turing Machine")

    tm = TuringMachine(tokens)

    st.write("Tape:")

    st.write(tm.tape)

    st.write("Initial State: q0")

    st.write(
    f"Final Accept State: q{len(tokens)}"
    )

    st.write(
    f"Head Movements: {len(tokens)}"
    )

    st.subheader("🌐 Automaton Diagram")

    dot = Digraph()

    transitions = automaton.get_transitions()

    for (state, char), next_state in transitions.items():

        dot.edge(
            f"q{state}",
            f"q{next_state}",
            label=char
        )

    st.graphviz_chart(dot)
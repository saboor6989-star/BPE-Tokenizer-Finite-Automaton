# Modeling BPE Tokenization using Finite Automata and Turing Machines

## Project Overview

This project implements Byte Pair Encoding (BPE) tokenization and demonstrates how concepts from Theory of Automata can be applied to modern Natural Language Processing (NLP) systems.

The system learns tokens from a text corpus using BPE merge operations, constructs a Finite Automaton to represent learned tokens, and simulates token processing using a Turing Machine.

An interactive Streamlit web interface is also provided for experimentation and visualization.

---

## Features

- BPE Tokenizer Implementation
- Merge Rule Learning
- Vocabulary Construction
- Tokenization of Input Words
- Finite Automaton Construction
- Turing Machine Simulation
- Graph Visualization using Graphviz
- Interactive Streamlit Web Interface

---

## Project Structure

```text
tokenizer.py         -> BPE Tokenizer Implementation

automata.py          -> Finite Automaton Construction

turing_machine.py    -> Turing Machine Simulation

main.py              -> Main Console Program

app.py               -> Streamlit Web Interface

visualizer.py        -> Automaton Visualization

corpus.txt           -> Training Corpus

requirements.txt     -> Project Dependencies
```

---

## Working Methodology

1. Load the training corpus.
2. Build character-level vocabulary.
3. Learn frequent token pairs using BPE.
4. Generate merge rules.
5. Construct vocabulary from learned tokens.
6. Build a Finite Automaton using generated tokens.
7. Place tokens on a Turing Machine tape.
8. Simulate state transitions and head movements.
9. Display results through console and Streamlit interface.

---

## Example

Input Word:

```text
learning
```

Generated Tokens:

```text
['l', 'e', 'ar', 'n', 'ing']
```

Turing Machine State Path:

```text
q0 → q1 → q2 → q3 → q4 → q5
```

Accept State:

```text
q5
```

---

## Technologies Used

- Python
- Streamlit
- Graphviz

---

## Theory of Automata Concepts

This project demonstrates:

- Finite Automata
- State Transitions
- Token Recognition
- Turing Machine Simulation
- Tape Processing
- Accept States
- Computational Modeling

---

## Installation

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the Streamlit application:

```bash
streamlit run app.py
```

Run the console version:

```bash
python main.py
```

---

## Future Enhancements

- Multi-Tape Turing Machine Simulation
- Larger Training Corpora
- Advanced Token Learning Strategies
- Enhanced Automaton Visualization

---

## Author

Muhammad Saboor Ansar Gill

Theory of Automata – Complex Computing Problem (CCP)

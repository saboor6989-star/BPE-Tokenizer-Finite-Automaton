# BPE Tokenizer and Finite Automaton

## Project Overview

This project implements the ideas presented in the research paper:

**"Tokenization as Finite-State Transduction"**

The system learns subword tokens using Byte Pair Encoding (BPE) and then builds a Finite Automaton from the learned vocabulary.

---

## Features

- Character-level vocabulary construction
- Pair frequency counting
- Byte Pair Encoding (BPE) training
- Token merging
- Vocabulary generation
- Word tokenization
- Finite Automaton construction
- Automaton visualization using Graphviz
- Interactive Streamlit Web Interface

---

## Project Structure

```text
tokenizer.py      -> BPE Tokenizer implementation
automata.py       -> Finite Automaton implementation
visualizer.py     -> Graphviz visualization
app.py            -> Streamlit web application
main.py           -> Main execution file
corpus.txt        -> Training corpus
requirements.txt  -> Required libraries
```

## Technologies Used

- Python
- Streamlit
- Graphviz

---

## How to Run

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run Main Program

```bash
python main.py
```

### Run Streamlit Interface

```bash
streamlit run app.py
```

---

## Sample Output

The tokenizer learns merge rules and generates tokens such as:

```text
ing
ge
ch
an
ar
at
```

The automaton is then built from these learned tokens.

---

## Author

Muhammad Saboor Ansar Gill

Course Project - Theory of Automata

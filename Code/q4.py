from automata.fa.dfa import DFA

from visual_automata.fa.dfa import VisualDFA

dfa = VisualDFA(
    states={"A", "B", "C", "D", "E","F"},
    input_symbols={"0", "1"},
    transitions={
        "A": {"0": "B", "1": "D"},
        "B": {"0": "E", "1": "C"},
        "C": {"0": "C", "1": "C"},
        "D": {"0": "E", "1": "D"},
        "E": {"0": "E", "1": "F"},
        "F": {"0": "E", "1": "D"},
    },
    initial_state="A",
    final_states={"C","F"},
)
dfa.show_diagram(view=True,filename="a4.gv",input_str="")
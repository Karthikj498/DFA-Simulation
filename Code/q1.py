from automata.fa.dfa import DFA

from visual_automata.fa.dfa import VisualDFA

dfa = VisualDFA(
    states={"q0", "q1", "q2", "q3", "q4"},
    input_symbols={"a", "b"},
    transitions={
        "q0": {"a": "q1", "b": "q3"},
        "q1": {"a": "q2", "b": "q4"},
        "q2": {"a": "q1", "b": "q3"},
        "q3": {"a": "q4", "b": "q3"},
        "q4": {"a": "q4", "b": "q4"},
    },
    initial_state="q0",
    final_states={"q3"},
)
dfa.show_diagram(view=True,filename="a1.gv",input_str="abba")
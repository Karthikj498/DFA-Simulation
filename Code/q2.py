from automata.fa.dfa import DFA

from visual_automata.fa.dfa import VisualDFA

dfa = VisualDFA(
    states={"00", "01", "02", "10", "11","12","20","21","22"},
    input_symbols={"a", "b"},
    transitions={
        "00": {"a": "10", "b": "01"},
        "01": {"a": "11", "b": "02"},
        "02": {"a": "12", "b": "00"},
        "10": {"a": "20", "b": "11"},
        "11": {"a": "21", "b": "12"},
        "12": {"a": "22", "b": "10"},
        "20": {"a": "00", "b": "21"},
        "21": {"a": "01", "b": "22"},
        "22": {"a": "02", "b": "20"},
    },
    initial_state="00",
    final_states={"00","11","22"},
)
dfa.show_diagram(view=True,filename="a2.gv",input_str="")
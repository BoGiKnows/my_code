class Automaton(object):

    def __init__(self):
        self.states = {'q1': ['q1', 'q2'], 'q2': ['q3', 'q2'], 'q3': ['q2', 'q2']}

    def read_commands(self, commands):
        state = self.states['q1'][int(commands[0])]
        for i in commands[1:]:
            command = int(i)
            state = self.states[state][command]
        return state == 'q2'


my_automaton = Automaton()
print(my_automaton.read_commands(["1", "0", "0", "1", "0"]))

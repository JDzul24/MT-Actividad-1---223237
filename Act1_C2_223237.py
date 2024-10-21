import tkinter as tk

class TuringMachine:
    def __init__(self, input_string):
        self.tape = list(input_string) + ['□']  # Añadimos blanco al final
        self.head_position = 0
        self.state = 'q0'

    def step(self):
        symbol = self.tape[self.head_position]
        
        if self.state == 'q0':
            if symbol == 'a':
                self.tape[self.head_position] = 'a'
                self.head_position += 1
                self.state = 'q1'
            else:
                self.state = 'q_reject'
                
        elif self.state == 'q1':
            if symbol == 'b':
                self.tape[self.head_position] = 'b'
                self.head_position += 1
                self.state = 'q2'
            else:
                self.state = 'q_reject'
                
        elif self.state == 'q2':
            if symbol == 'b':
                self.tape[self.head_position] = 'b'
                self.head_position += 1
                self.state = 'q3'
            else:
                self.state = 'q_reject'
                
        elif self.state == 'q3':
            if symbol == 'a':
                self.head_position += 1
                self.state = 'q1'
            elif symbol == '□':
                self.state = 'q_accept'
            else:
                self.state = 'q_reject'
        
    def run(self):
        while self.state not in ['q_accept', 'q_reject']:
            self.step()
        return self.state

# GUI con Tkinter
def run_machine():
    input_string = entry.get()
    tm = TuringMachine(input_string)
    result = tm.run()
    result_label.config(text="Resultado: " + ("Aceptado" if result == 'q_accept' else "Rechazado"))

root = tk.Tk()
root.title("Máquina de Turing")

label = tk.Label(root, text="Ingrese la cadena:")
label.pack()

entry = tk.Entry(root)
entry.pack()

run_button = tk.Button(root, text="Ejecutar", command=run_machine)
run_button.pack()

result_label = tk.Label(root, text="Resultado: ")
result_label.pack()

root.mainloop()

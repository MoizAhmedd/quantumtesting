from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister, execute, Aer

#Defining Registers
q = QuantumRegister(1)
c = ClassicalRegister(1)

#Building Circuits
single_qubit = QuantumCircuit(q,c)
single_qubit.measure(q,c)

#Executing Circuit
job = execute(single_qubit,backend = Aer.get_backend('qasm_simulator'),shots=1024)
result = job.result()

#Print result
print(result.get_counts(single_qubit))

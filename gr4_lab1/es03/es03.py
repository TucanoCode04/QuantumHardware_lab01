from qiskit import QuantumCircuit
from qiskit.quantum_info import Statevector
from qiskit.providers.basic_provider import BasicProvider
from qiskit.qasm2 import dump
import matplotlib.pyplot as plt

qc = QuantumCircuit(2)

qc.h(0)
qc.h(1)
qc.cz(0, 1)
qc.h(0)
qc.h(1)
qc.x(0)
qc.x(1)
qc.cz(0, 1)
qc.x(0)
qc.x(1)
qc.h(0)
qc.h(1)

qc.draw(output="mpl")
plt.show()

# Statevector simulation
statevector = Statevector(qc)
print(statevector)

# Basic simulation
qc.measure_all()

backend = BasicProvider().get_backend("basic_simulator")
result = backend.run(qc).result()

print(result.get_counts())

# Save the circuit to a qasm file
with open("es03_qasm.qasm", "w") as f:
    dump(qc, f)

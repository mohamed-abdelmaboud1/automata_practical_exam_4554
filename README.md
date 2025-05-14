# Theory of Computation Practical
#### Name: Mohamed Mohamed Abdelmaboud Mohamed
#### Section: 5
#### id: 4554

### Task Being Solved

* **DFA for Substring '101'**: A Deterministic Finite Automaton (DFA) designed to check if a binary string contains the substring "101".
  
  ![daf](https://github.com/user-attachments/assets/5b2264b3-8a73-40bb-918c-72c5baec8acd)
---
* **Turing Machine for Divisibility by 3**: A Turing Machine that determines if a binary number is divisible by 3.
  
![Turing-Machine-divisible-by-3](https://github.com/user-attachments/assets/cfbb463c-b818-4275-9afa-57c85bc394e2)
---
### How to Run and Test the Code
Before running the code, ensure that you have Python 3.x installed. You can check the Python version by running the following command:

```bash
python --version
```
Additionally, make sure you have `git` installed to clone the repository.

#### 1.Open cmd and clone the Repository

```bash
git clone https://github.com/mohamed-abdelmaboud1/automata_practical_exam_4554.git
```

#### 2. Navigate to the Project Directory

```bash
cd automata_practical_exam_4554
```

#### 3. Install Required Dependencies

Ensure that all necessary dependencies are installed by running:

```bash
pip install -r requirements.txt
```

This will install the required libraries for both the DFA and the Turing Machine scripts.

---

### DFA for Substring '101'

This script uses a DFA to check whether a given binary string contains the substring '101'. It will continuously accept input until you choose to exit.

#### How to Run:

1. Open a terminal in the project directory.

2. Run the `dfa.py` script to start the DFA:

   ```bash
   python dfa.py
   ```

3. The program will check if the string contains the substring '101'. If the substring is found, the result will be "Accepted"; otherwise, it will return "Rejected".

#### Example:

```bash
Enter a binary string (or 'x' to exit): 1101011
Accepted

Enter a binary string (or 'x' to exit): 111000
Rejected
```
---

### Turing Machine for Divisibility by 3

This Turing Machine is designed to determine if a binary number is divisible by 3. It works by processing the binary string and using the machine’s states to check divisibility.

#### How to Run:

1. Run:
   ```bash
   python turing_machine_divisible_by_3.py
   ```

2. The code will determines whether the binary number is divisible by 3.

#### Example:

```bash
Enter a binary number (or 'x' to exit): 110
Accepted

Enter a binary number (or 'x' to exit): 101
Rejected
```

#### Notes:

* The program reject any input that contains characters other than '0' or '1'.
* You can exit the program at any time by typing 'x'.

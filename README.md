# **CyberEdu CTFs - Reverse Engineering**

In aceasta sectiune, vom prezenta solutiile pentru **4 provocari CTF** din categoria **Reverse Engineering**.

---

## **1. 'source' - Dificultate: Easy**

### **Descriere**
> "Stoc toti secretii mei in binare, nimeni nu poate sa ii citeasca daca nu are codul sursa!"

### **Fisiere furnizate**
- `main` - Un fisier binar (ELF, executabil).

### **Solutie**
Aceasta provocare ne invata sa incarcam un fisier binar intr-un instrument de analiza precum **IDA**, **Cutter**, **Ghidra**, sau alte unelte similare.

#### **Pasi pentru rezolvare:**
1. **Analiza string-urilor:**
   - String-urile dintr-un fisier binar pot oferi indicii valoroase.
   - In acest fisier, observam urmatorul string:
     ```
     TFC{3v3ryth1ng_1s_0p3n_5ourc3_1f_y0u try_h4rd_3n0ugh}
     ```
   - Acesta este chiar **flag-ul** pe care il cautam.

#### **Concluzie:**
Flag-ul este: TFC{3v3ryth1ng_1s_0p3n_5ourc3_1f_y0u_try_h4rd_3n0ugh}


---

## **2. 'get-password' - Dificultate: Easy**

### **Descriere**
Aceasta provocare CTF a fost publicata la **European Cyber Security Challenge 2019**, care a avut loc in Romania.

### **Fisiere furnizate**
- `get` - Un fisier binar (ELF, executabil).

### **Solutie**
Un alt mod de a analiza un fisier binar este sa verificam functia `main` si, daca este necesar, sa decompilam alte functii relevante pentru a intelege logica din spatele lor.

#### **Pasi pentru rezolvare:**
1. **Analiza functiei `check_pw`:**
   - Prin decompilarea functiei `check_pw`, observam unele operatii aplicate parolei introduse pentru validare.
   - Aceste operatii pot include comparatii cu anumite valori, transformari ale caracterelor sau algoritmi personalizati.

2. **Analiza string-urilor:**
   - In lista de string-uri din fisierul binar, observam **20 de string-uri** care ar putea fi folosite pentru validarea parolei.
   - Aceste string-uri pot servi ca indiciu pentru ghicirea parolei corecte sau pentru construirea unei solutii.

#### **Concluzie:**
Pentru a gasi flag-ul, trebuie sa analizam cu atentie functia `check_pw` si sa intelegem cum sunt procesate datele de intrare. Solutia finala depinde de implementarea exacta a acestei functii.

---

## **3. [Titlul celei de-a treia provocari CTF]**

### **Descriere**
[Inserati descrierea celei de-a treia provocari CTF.]

### **Fisiere furnizate**
- [Lista fisierelor furnizate.]

### **Solutie**
[Explicati pasii pentru rezolvare intr-un mod clar si structurat, similar exemplelor de mai sus.]

---

## **4. [Titlul celei de-a patra provocari CTF]**

### **Descriere**
[Inserati descrierea celei de-a patra provocari CTF.]

### **Fisiere furnizate**
- [Lista fisierelor furnizate.]

### **Solutie**
[Explicati pasii pentru rezolvare intr-un mod clar si structurat, similar exemplelor de mai sus.]

---

### **Nota finala**
Aceste provocari CTF din categoria **Reverse Engineering** ne invata sa folosim unelte precum **IDA**, **Cutter**, **Ghidra** sau **Radare2** pentru a analiza fisiere binare si a intelege logica din spatele lor. Este esential sa exploram atat string-urile, cat si functiile principale pentru a descoperi flag-urile ascunse.




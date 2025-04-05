# **CyberEdu CTFs - Reverse Engineering**

In aceasta sectiune, vom prezenta solutiile pentru **4 provocari CTF** din categoria **Reverse Engineering**.

---

## **1. 'source' - Dificultate: Easy**

### **Descriere**
> "I store all my secrets in binaries, no one can read them if they don't have the source code!"

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
Flagul este:
      ```
     ECSC{DAC553500B60BF700F56E456922104FA06BC144213ED2B58BEC2429F015242DB}
      ```

#### **Concluzie:**
Pentru a gasi flag-ul, trebuie sa analizam cu atentie functia `check_pw` si sa intelegem cum sunt procesate datele de intrare. Solutia finala depinde de implementarea exacta a acestei functii(a se uita la scriptul 2nd-challenge-script.py si dupa rezultatul este pus in base64-decoder.py)

---

## **3. 'spy-agency' - Dificultate: Medium**

### **Descriere**
> "A malicious application was sent to our target, who managed to have it before we confiscated the PC. Can you manage to obtain the secret message?"

Format flag: `ctf{sha256(numele locatiei din coordonate, in litere mici)}`

### **Fisiere furnizate**
- `spyagency3.zip` - Un fișier zip care conține un binar.

### **Solutie**
Aceasta provocare ne testeaza abilitatea de a extrage informatii utile dintr-un fisier binar mare.

#### **Pasi pentru rezolvare:**
1. **Extragerea indiciilor din fișierul binar:**
   - Fisierul `.zip` contine un binar de dimensiune foarte mare (1 GB). Incercati sa rulati comanda `strings` pe acesta:
     ```bash
     strings spyagency3.zip
     ```
   - Deoarece fisierul este foarte mare, comanda va rula mult timp. Totusi, nu este necesar sa asteptam sa se termine intreg procesul. Putem cauta cuvinte cheie relevante în output.

2. **Căutarea coordonatelor:**
   - Din enunt, stim ca trebuie sa gasim coordonate geografice. Folosim cuvinte cheie precum `coordinates`, `latitude`, `longitude` sau alte termeni sugestivi.
   - De exemplu, putem cauta prin filtrare:
     ```bash
     strings spyagency3.zip | grep "coordinates"
     ```
   - Vedem ca este vorba despre un sistem de fisiere si o aplicatie .apk deci cel mai probabil trebuie gasit offset-ul de la care incepe aplicatia si apoi trebuie extrasa.
   - Aplicatia o puteti gasi in repository, dupa care se navigheaza prin sistemul de fisiere ajungand la poza.
   - Gasim coordonatele ascunse in poza, de exemplu: `44.44672703736637, 26.098652847616506`.

3. **Identificarea locatiei:**
   - Folosind coordonatele gasite in metadatele pozei, gasim locatia exacta pe Google Maps si aceasta este Pizza Hut.
   - 

4. **Calcularea flag-ului:**
   - Folosind scriptul sha256-transformer.py hashuim "pizzahut":

#### **Concluzie:**
Flag-ul este: ctf{a939311a5c5be93e7a93d907ac4c22adb23ce45c39b8bfe2a26fb0d493521c4f}

## **4. 'secret-reverse' - Dificultate: Medium**

### **Descriere**
> "There is a secret message hidden in this binar."

Mesaj codificat: `46004746409548141804243297904243125193404843946697460795444349`

Format flag: `ctf{sha256(mesaj_original)}`

### **Fisiere furnizate**
- `elf_file` - Un fișier ELF.

### **Solutie**
Aceasta provocare ne cere sa decodam un mesaj ascuns intr-un fisier binar si sa calculam hash-ul SHA-256 al mesajului original.

#### **Pasi pentru rezolvare:**
1. **Analiza functiei principale:**
   - Incărcam fișierul ELF intr-un dezasamblor precum **Ghidra** sau **Cutter**.
   - Identificam funcția care prelucrează mesajul codificat. Observam că mesajul este supus unui algoritm de decodificare.
   - Observam ca se scrie citesc date intr-un fisier pe nume message.txt si se codifica.

2. **Decodificarea mesajului:**
   - Vom face un script **ctf-4base64.py** care prin brute-force, scrie in message.txt si trece prin toate posibilitatile oferind un scor pentru a reduce din timpul de cautare.
   - Astfel scriptul nu dureaza a fi rulat mai mult de 1 minut.
   - Rulam script-ul și obținem mesajul original.

3. **Calcularea flag-ului:**
   - Calculam hash-ul SHA-256 al mesajului original:


#### **Concluzie:**
Flag-ul este: ctf{9b9972e4d59d0360b5f1b80a5bbd76c05d75df5b636576710a6271c668a10ac5}

### **Nota finala**
Aceste provocari CTF din categoria **Reverse Engineering** ne invata sa folosim unelte precum **IDA**, **Cutter**, **Ghidra** sau **Radare2** pentru a analiza fisiere binare si a intelege logica din spatele lor. Este esential sa exploram atat string-urile, cat si functiile principale pentru a descoperi flag-urile ascunse.




Vigenere-cipher-dhe-Turning-Grille-Fleissner-Grille

Vigenère Cipher është një metodë klasike e kriptimit (fshehjes së mesazheve) që përdor një fjalë kyçe (keyword) për të ndryshuar shkronjat e mesazhit në mënyrë të përsëritur. 

Ndryshe nga Caesar (ku zhvendosja është gjithmonë e njëjtë) këtu:
        çdo shkronjë e mesazhit mund të ketë një zhvendosje tjetër dhe
        kjo varet nga shkronja përkatëse e fjalës kyçe


Ideja bazë:
Zgjedh një mesazh të thjeshtë (plaintext)
Zgjedh një fjalë kyçe (p.sh. "KEY")
Fjalën kyçe e përsërit mbi mesazhin
Çdo shkronjë e mesazhit zhvendoset sipas shkronjës përkatëse të fjalës kyçe.


Fillimisht, çdo shkronjë kthehet në numër: 
A = 0  
B = 1  
C = 2  
...  
Z = 25

Mesazhi:HELLOWORLD
Fjala kyçe:KEY

Përsëritet:KEYKEYKEYK


Formula e kriptimit -Për çdo shkronjë përdoret kjo formulë: C=(P+K)mod26
Ku:
P = numri i shkronjës së mesazhit (plaintext)
K = numri i shkronjës së fjalës kyçe
C = rezultati (ciphertext)

Shndërrimi në numra

Shkronja	H	E	L	L	O
P	        7	4	11	11	14

Shkronja	K	E	Y	K	E
K	       10	4	24	10	4

Llogaritja
C=(P+K)mod26
(7 + 10) mod 26 = 17 → R
(4 + 4) mod 26 = 8 → I
(11 + 24) mod 26 = 9 → J
(11 + 10) mod 26 = 21 → V
(14 + 4) mod 26 = 18 → S

Rezultati: RIJVS


Si bëhet deshifrimi?

Përdoret formula e kundërt: P=(C−K)mod26

Pra:
merr shkronjën e koduar
zbrit vlerën e fjalës kyçe
kthen rezultatin në shkronjë


Kodi implementon algoritmin Vigenère Cipher.
 Fillimisht, programi kërkon nga përdoruesi të fusë tekstin që dëshiron të enkriptojë dhe një fjalë kyçe përmes funksionit input(). Kjo fjalë kyçe përdoret për të përcaktuar zhvendosjen e çdo shkronje në tekst. Para se të vazhdojë, programi kontrollon që çelësi të përmbajë vetëm shkronja duke përdorur isalpha(), për të siguruar që algoritmi të funksionojë saktë.

Gjatë enkriptimit, programi kalon nëpër çdo karakter të tekstit. Nëse karakteri është shkronjë ai shndërrohet në një vlerë numerike (0–25) me ord() dhe i shtohet vlera e shkronjës përkatëse nga çelësi, i cili përsëritet automatikisht duke përdorur operatorin modulo sipas gjatësisë së tij. Rezultati llogaritet me formulën (p + k) % 26 dhe kthehet përsëri në shkronjë me chr(), duke ruajtur dallimin mes shkronjave të mëdha dhe të vogla. Nëse karakteri nuk është shkronjë (si hapësira apo simbole), ai mbetet i pandryshuar.

Në pjesën e dekriptimit, përdoruesi jep përsëri tekstin e koduar dhe të njëjtin çelës. Programi përdor të njëjtën logjikë, por këtë herë aplikon formulën (c - k + 26) % 26 për të kthyer çdo shkronjë në formën e saj origjinale. Kështu, kodi realizon me sukses si enkriptimin ashtu edhe dekriptimin duke përdorur parimet bazë të algoritmit Vigenère.
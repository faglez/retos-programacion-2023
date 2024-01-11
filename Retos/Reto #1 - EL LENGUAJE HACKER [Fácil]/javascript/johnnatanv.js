/*
 * Escribe un programa que reciba un texto y transforme lenguaje natural a
 * "lenguaje hacker" (conocido realmente como "leet" o "1337"). Este lenguaje
 *  se caracteriza por sustituir caracteres alfanuméricos.
 * - Utiliza esta tabla (https://www.gamehouse.com/blog/leet-speak-cheat-sheet/)
 *   con el alfabeto y los números en "leet".
 *   (Usa la primera opción de cada transformación. Por ejemplo "4" para la "a")
 */

/*
A	4
B	I3
C	[
D	|)
E	3
F	ph
G	6
H	#
I	1
J	]
K	|<
L	1
M	/\/\
N	|\|
O	0
P	|>
Q	0_
R	I2
S	5
T	7
U	(_)
V	\/
W	\/\/
X	><
Y	j
Z	2
*/

let encryptCheat = {
  A: `4`,
  B: `I3`,
  C: `[`,
  D: `|)`,
  E: `3`,
  F: `ph`,
  G: `6`,
  H: `#`,
  I: `1`,
  J: `]`,
  K: `|<`,
  L: `1`,
  M: `/\\/\\`,
  N: `^/`,
  O: `0`,
  P: `|>`,
  Q: `0`,
  R: `I2`,
  S: `5`,
  T: `7`,
  U: `(_)`,
  V: `\/`,
  W: `\/\/`,
  X: `><`,
  Y: `j`,
  Z: `2`,
  1: `L`,
  2: `R`,
  3: `E`,
  4: `A`,
  5: `S`,
  6: `b`,
  7: `T`,
  8: `B`,
  9: `g`,
  0: `o`,
};

let encrypt = (text) => {
  let encryption = "";

  for (let char = 0; char < text.length; char++) {
    let newChar = text[char].toUpperCase();
    encryption += text[char] === " " ? text[char] : encryptCheat[newChar];
  }

  console.log(encryption);
};

encrypt("Hola Johnnatan");

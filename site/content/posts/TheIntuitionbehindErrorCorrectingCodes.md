---

title: "The Intuition behind Error Correcting Codes"

date: 2023-02-13

draft: false

  
tags: ["featured", "mathematics", "discmath"]
---
*This article may require some additional technical knowledge.*

*This article has been adapted from an earlier PDF I wrote.*


#### Motivation

Alex wants to send Bernd a secret code $m$ explaining their plan to take over the world. The only problem is that local Iris-agents are jamming their communication, and therefore Alex cannot guarantee that the entire message will arrive unchanged.
Is there some way that Alex and Bernd can develop a protocol that ensures that Bernd is *guaranteed* to receive the correct message from Alex?


#### Encoding

Assume that Alex and Bernd converse in binary. In other words, their **Alphabet** A is $\\{0, 1\\}$.

Also assume they want to send a code of exactly 3 bits in other words, a list ($a_0$, $a_1$, $a_2$) $\in \\{0, 1\\}^3$.

They use a very primitive encoding function: They just copy the bitstring five times, in other words the resulting message will be the codeword ($c_0$, $c_1$, $c_2$, ... $c_{14}$)  $\in \\{0, 1\\}^{15}$.

**(15, 3) Example:**
Let $E$ be the encoding function
$$E((0, 1, 1)) = (0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1)$$

This is therefore a $(15, 3)$-encoding function.

$C = Im(E)$ is the set of all codewords and is called an error-correcting code.


As $C$ is the set of all codewords, for our example of the $(15, 3)$-error correcting code, it is guaranteed that it is a subset of $\\{0, 1\\}^{15}$ with the cardinality of $q^k = 2^3$ where $q = |\\{0,1\\}|$

In other words, there are only 8 bitstrings of length 15 that are actually error-correcting codes, namely it is all the ones which are a 3-digit bitstring repeat five times:
$$(0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)$$
$$(0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1)$$
$$...$$
$$(1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1)$$


###### Hamming Distance
The Hamming distance is nothing but the number of symbols two strings differ in.

**Example:**
Let us use the alphabet of digits as an example: $A = \\{0, 1, 2, 3, 4, 5, 6, 7, 8, 9\\}$
Given the two strings
$c_1 = (1, 1, 0, 2)$
$c_2 = (9, 1, 3, 2)$
Their hamming distance is equal to $2$, as they differ in exactly two symbols.

**(15, 3) Continued Example:**
Let us make another example with the $(15, 3)$ code. What is the minimum number of bits you have to change, to e.g., make

$$(0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)$$
into
$$(1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1)$$
?
Simple counting will give the answer of $10$. This is the Hamming distance between these two codes.


##### Minimum Distance
When speaking about error-correcting codes (reminder: error-correcting codes are sets! The actual strings are called codewords), the minimum distance is a statement about the entire error-correcting code: What's the minimum number of times you have to change a symbol on one codeword to make it into any other codeword?

This is an extremely relevant question, because it gives a measure of the "robustness" of an error-correcting code. Of course in the end we want to decode the codewords again, but if an attack is able to change only very few symbols to give use a different codeword, we will decode the wrong message! As such, the minimum distance may also be interpreted as a worst-case analysis of a given error-correcting code.

**Example:**
Let the set of error correcting codes defined over the alphabet $\\{0, 1\\}$ be
$$C = \\{00000, 11111, 00111, 10111\\} \subseteq \\{0, 1\\}^{5}$$
What is the minimum hamming distance of this error-correcting code?
The answer is $1$ as one can, e.g., change 00111 into 10111 by changing a single bit. This means, *irrelevant of the decoding function*, this error correcting code will always fail for attacks that can change a single bit.

**Example:**
Here is in turn an extremely robust example:
$$C = \\{00000000000, 11111111111\\} \subseteq \\{0, 1\\}^{11}$$
This error-correcting code has a minimum distance of $11$.
The downside is of course that there are only two codewords, and they take up a lot of space.


**(15, 3) Continued Example:**
What is the minimum distance of our $(15, 3)$ code?
As all of our inputs to the encoding function had a minimum distance of $1$ (as we used all the different bitstrings one can make from one bit) and our encoding takes each input five times, it is easy to see that the minimum distance of the error-correcting code is $d_{min}(C) = 5$.


#### Decoding

A decoding function now takes all the different elements in $A^{n}$ and converts them back into their original message in $A^{k}$ (or at least tries to).

Wait, why does it take all elements in $A^{n}$ and not just in $C \subseteq A^{n}$ as those are only our error-correcting codes?
The answer is: errors. As stated in the motivation, the goal is *to correct errors*, be they caused by interference or anything else. This means that we assume that between encoding and decoding there is a some kind of “transport" of the message which changes symbols in the codewords, maybe by a malicious attacker.


**(15, 3) Continued Example:**
Assume that the iris agents have enough jammers online that they are able to change any messages sent by Alex by at most $2$ bits. (In this example, we assume that the iris agents are completely aware of the encoding scheme, meaning that they will always choose the *worst case* scenario bits to change).

For example, they may change
$$E((1, 0, 1)) = (1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1)$$
to
$$(0, 1, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1)$$
where the first two characters were flipped.

Now the question is, what is a good decoding function for our $(15, 3)$ error-correcting codes?
A very simple function $D$ that takes advantage of how the encoding function may operate as follows:

Let us use the example of the above code
$$(0, 1, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1)$$
Write the code in rows as follows:
$$0, 1, 1$$
$$1,0,1$$
$$1, 0, 1$$
$$1, 0, 1$$
$$1, 0, 1$$
Now take the “average" (in the sense that we always pick the majority of symbols) of each column:
$$= (1, 0, 1)$$
And as we see, the code has been successfully decoded.


The question now becomes: 
Given any $(n, k)$ error-correcting code with a minimum distance $d$, what is the maximum number of errors a decoding function can correct?

And interestingly there is a very concrete answer:
Any decoding function of a given $(n, k)$ error-correcting code with minimum distance $d$ can at most correct $t = \frac{d-1}{2}$ errors.

As this is an inherent property of a given error-correcting code, we say the error-correcting code $C$ is $t$-error correcting.

**Example:**
We shall give an intuition behind why this is true in the following example:

Let us use the following encoding function:
$$D: \\{0, 1\\} \rightarrow \\{0, 1\\}^4$$
$$D((a_0)) = (a_0, a_0, a_0, a_0)$$
In other words, it uses the same "duplication strategy" as the ongoing example.

Clearly $C \subseteq \\{0, 1\\}^4$
$$C = \\{(0, 0, 0, 0), (1, 1, 1, 1)\\}$$
And therefore the minimum distance is $4$.

Now let us define $\textrm{Er}(c, i)$ to be an "Error function" taking a code word $c$ and an integer i and outputting all the different ways one can permute the code word $c$ by changing $i$ symbols.
e.g.,
$$\textrm{Er}((0, 0, 0, 0), 1)$$
$$= \\{(1, 0, 0, 0), (0, 1, 0, 0), (0, 0, 1, 0), (0, 0, 0, 1)\\}$$
and
$$\textrm{Er}((1, 1, 1, 1), 1)$$
$$= \\{(0, 1, 1, 1), (1, 0, 1, 1), (1, 1, 0, 1), (1, 1, 1, 0)\\}$$

Now notice how the two resulting sets have 
*no overlap*, in other words, given any of the resulting strings, a decoding function could easily identify from which codeword it came from. And therefore this error-correcting code is at least $1$-error correcting.

Now if we increase $i$ to $3$ we can definitely see that we have an overlap between $\textrm{Er}((0, 0, 0, 0), 3)$ and $\textrm{Er}((1, 1, 1, 1), 3)$, for example $(0, 1, 1, 1)$ can be found in both sets.
This intuitively makes sense as the error-correcting code has a minimum distance of $4$, meaning that if both of the two bitstrings are allowed to move towards each other by $3$ bits they can cross a distance of $2 \cdot 3 = 6 > 4$ bits.

This already explains the relation of $d \geq 2t$ (or $d \geq \frac{t}{2}$), but it does not explain the offset by 1.

Let us look at the case of $\textrm{Er}((0, 0, 0, 0), 2)$ and $\textrm{Er}((1, 1, 1, 1), 2)$. Notice how these two sets still have some overlap. What would you decode $(0, 0, 1, 1)$ to? $(0, 0, 0, 0)$ or $(1, 1, 1, 1)$?

Of course the problem is obvious: it has the same hamming distance to both of them, therefore one cannot decide.
This is the explanation for the offset by $1$: it is a tiebreaker for these kinds of situation.

This means that the given example error-correcting code is in actuality at most
$$\frac{d-1}{2} = \frac{4-1}{2} = 1.5 \geq t = 1$$
error-correcting.



**(15, 3) Continued Example:**
As an exercise, attempt to figure out if the given example $(15, 3)$ code with minimum distance $5$ is enough for Alex and Bernd to communicate despite the Iris-Agents' Jamming attacks. 
How many errors can any given decoding function at most correct given Alex and Bernd error-correcting code?



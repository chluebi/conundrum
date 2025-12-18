---
title: Speedrunning my Computer Science degree [100%] (1/6)
date: 2025-12-13
draft: false
tags:
  - personal
  - featured
  - speedrunning-computer-science
---
Clickbait Title: Brevity is the soul of cowards.

No, it's not "so over" for you if you did something differently here.
No, this is not accurate for everyone, even my peers.
Yes, some details have been changed for reasons. I will forget things and say wrong things, I'm not pulling up my old notes for accuracy's sake.
There will be jokes until morale improves.

#### Background
After avoiding [this video](https://youtu.be/MIvvsqJAYh0) for months, I finally relented and spent the precious 3 minutes of my life to watch it. I was disappointed and almost shocked. Surely you learned more than that in 3 years? So I'm not going to name my article after this video, but rather the [much better one with the same premise](https://youtu.be/Ju2gDvkkFa8).

### Before university
You had to make some kind of choice about your degree. School has probably prepared you relatively well for other STEM choices such as mathematics and physics. But computer science is still not a priority in the curriculum. So your enthusiasm doesn't stem from school assignments, but free time activities.

There seems to always be a video-game or gaming related activity du jour which tricks a generation of kids to learn informatics. Raise your hand when I name your favourite. Minecraft, Roblox, Factorio. Starting even earlier in life there were educational games where you assemble code in blocks.

You are aware of "Coding", "Computer Science" and the current start-up boom. YouTube feeds you [Computerphile](https://www.youtube.com/@Computerphile) and the [Tom Scott video on FizzBuzz](https://youtu.be/QPZ0pIK_wsc) starts making sense. What language is he using? "Javascript"? That's the "bootcamp" language, isnt it. You follow some awkward tutorial setting up a html page in Notepad in which you can locally run JavaScript.

Alternatively you get into making Minecraft mods and learn Java. Or Unity teaches you C#. You learn Python if you read too much Reddit. You get really good at googling and copypasting. You hang out on IRC, Skype or Discord, depending on your age. Maybe you find someone who is better than you at all this stuff and they help you install Visual Studio (sic).

You become "good at coding" compared to your peers, projects line your free-time, you lose some sleep on exciting nights. Computer Science lessons in high-school become boring. Maybe you try out competitive programming and get humbled really quickly. Still, why not try Computer Science at university? It's a good university for Computer Science and everything is computer nowadays.

You get a vague idea of the curriculum from friends, there's going to be Java. That's great, you know Java. Still you take an online course on Java just in case, it's a good university after all and you've got not so much to do during Summer break.

# Semester 1
(Notice how I need to structure it in semesters instead of years?)

To become a good computer scientist (not "coder"), you need to be at least a decent mathematician, so this semester is actually 50% maths subjects. And even the computer science subjects are at least 20% maths. That's 60% maths, wow.

### Java
The least math-y is learning to program in Java. It starts from zero and it ramps up quickly. Variables, Control-flow, functions it all goes by fairly quickly. By week 5 you know why we have the ugly ``public static void main``. 

Java is an imperative programming language (like every programming language you ever learned) which executes statements one after another. The simplest statement is a variable assignment:
```java
int x = 10;
// x == 10
```
The variable ``x`` has a value of 10 and we can re-use it further down:
```java
int x = 10;
int y = x + 5;
// x == 10 && y == 15
```
Variables can be ``int`` (Integers = normal numbers), ``float`` (Floats = real numbers) or ``bool`` (Booleans = true or false).
You can use operators like ``+``, ``&&`` or ``%`` to calculate things.

We can have conditional statements like ``if`` which only execute code if their condition is met. In this case we change the sign of x, if the number is negative, making sure x is never negative:
```java
if (x < 0) {
	x = 0 - x;
}
// x >= 0
```

We can execute the same code several times with loops. A while loop will check a condition and as long as the condition is true, it will keep on executing what is inside.
```java
// y >= 0
int x = 0;
while (y > 0) {
	x = x + 3;
	y--;
}
// y == 0 && x == 3*y
```

For-loops are just fancy while loops:
```java
// y >= 0
for (int x = 0; y > 0; y--) {
	x = x + 3;
}
// y == 0 && x == 3*y
```

Functions are one big block of code that does one thing. They can be "called" the same way we wrote functions in mathematics classes:
```java
// x >= 0
public int factorial(int x) {
	if (x == 0) {
		return 1;
	} else {
		return x * factorial(x-1);
	}
}
```


We have arrays which are basically lists of things:
```java

int[] arrayOfNumbers = {1, 2, 3, 4};
int sum = 0;
for (int i = 0; i < arrayOfNumbers.length; i++) {
	sum += arrayOfNumbers[i];
}
// sum == 10
```

Arrays are passed via reference instead of value, which means that if a function changes an array it has passed, the effects are visible:
```java
public void setToZero(int[] arrayOfNumbers) {
	for (int i = 0; i < arrayOfNumbers.length; i++) {
		arrayOfNumbers[i] = 0;
	}
}
```

Now we run our function:
```java
int[] arrayOfNumbers = {1, 2, 3, 4};

setToZero(arrayOfNumbers);

// arrayOfNumbers == {0, 0, 0, 0}
```


The thing that makes Java supposedly so cool are classes
```java
class Cat {
	public void speak() {
		System.out.println("meow");
	}
}
```
We can take this "Cat" class and we can create instances of it which are then called Objects:
```java
Cat cat1 = new Cat();
Cat cat2 = new Cat();
cat1.meow(); // prints meow
cat2.meow(); // prints meow
```

Classes can have fields which is data that is stored with each object. These fields can get instantiated in a constructor.

```java
class Cat {
	int age;

	public Cat(int age) {
		this.age = age;
	}

	public void speak() {
		System.out.println("meow");
	}
	
	public int getAge() {
		return this.age;
	}
}
```

Now we can initialise our objects with certain values and then access these values:
```java
Cat cat1 = new Cat(5);
Cat cat2 = new Cat(8);
int collectiveAge = cat1.getAge() + cat2.getAge();
// collectiveAge == 13
```


Classes can depend on other classes in a process called "inheritance". An class that inherits from another is a specialisation which can do all of the previous stuff but does more things.

```java
class Animal {
	int age;
	
	public Animal(int age) {
		this.age = age;
	}
	
	public void speak() {
		System.out.println("*vague animal noises*");
	}
	
	public int getAge() {
		return this.age;
	}
}

class Cat extends Animal {

	public Cat(int age, int cuteness) {
		this.age = age * 7; // cat years
		this.cuteness = cuteness;
	}

	public void speak() {
		System.out.println("meow");
	}
	
	public void moveTail() {
		System.out.println("Swish!");
	}
}
```

Now our cat can do all the same things as Animal, and more:
```java
Cat cat = new Cat(10, 9001);
cat.getAge() // 70
cat.speak() // prints meow
cat.moveTail() // prints Swish!

Animal animal = new Animal(1);
animal.getAge() // 1
animal.speak() // prints *vague animal noises*
```

We can also tell Java that we want to just treat a Cat as Animal. This is called "upcasting":
```java
Animal secretCat = new Cat(10, 9001);
secretCat.moveTail(); // Error! This is just an Animal it may not have a tail
```

But if we make the animal speak, then it meows!
```java
Animal secretCat = new Cat(10, 9001);
secretCat.speak(); // prints meow
```
This is due to something called "dynamic binding", whatever that means.

We can check at Runtime if something is a Cat and if so, we can "downcast" to it:

```java
Animal secretCat = new Cat(10, 9001);
if (secretCat instanceof Cat) {
	Cat cat = (Cat) secretCat;
	cat.moveTail(); // prints Swish!
}
```

Turns out this idea of Classes that inherit from others runs deep into java. Every Class (or so one might be taught in the first semester) inherits from the Object Class. Exceptions have their own class they can inherit from. Classes are supposedly why businesses love Java so much for abstracting away their logic. 

Thinking people have *opinions* on these things. Present One.
1. Oracle cleaned up our mess and now they rule us. (Shake your head in shame.)
2. Functional Programmers just don't understand how money works.
3. Modern Java with Streams seems quite capable, actually.
4. That's how it should be. Soft coffee drinkers paving the way for the hard system programmers to take over.
5. Nothing. I don't think. I just do.

You learn to solve generic problems in Java through exercises. You are using ``ArrayList<T>`` a lot. The professor mentions that this is Polymorphism and that arrays can't do it. Weird.

Testcases exist, its some magic with ``@`` but you are used to magic with ``@`` from python.

### EBNF grammars
Now that we know Java, we can talk about the actually important parts about learning how to program (yes we're still in the same subject).

Different languages will define what is allowed code and what is not. The first instance of filtering happens on the "grammar" level. A grammar is a set of rules that defines what is allowed. We can use EBNF to define grammars.

```
char <= 0 | 1
helper <= char helper | epsilon
binary_string <= 1 helper
```

This defines all binary strings (excluding the ones with zeroes at the start). Epsilon is "empty", i.e. nothing further happens. For any given binary string we can follow how it is constructed:

```
binary_string
=> 1 helper
=> 1 char helper
=> 1 0 helper
=> 1 0 char helper
=> 1 0 1 helper
=> 1 0 1 epsilon
=> 1 0 1
```

This is similar to "regexes" which you may have heard of before university, but it's just better.

### Hoare Logic and Loop Invariants
Now let's talk about how we talk about programs.

```java
int z = x + y;
x = z - y;
y = z - x;
```

What can we say about this program, what does it do?
Let's write some statements we think are true inbetween each statement. We call these statements "Hoare logic":

```java
// x == X && y == Y
int z = x + y;
// z == X + Y
x = z - x;
// z == X + Y && x == Y
y = z - y;
// z == X + Y && x == Y && y == X
```
You can see that we named the initial values of ``x`` and ``y`` to be ``X`` and ``Y``. After the last statement we can see that the values of X and Y swapped (assuming that integers behave like normal mathematical numbers). This reasoning over a program is called Hoare Logic and it allows us to give guarantees of a program's values for all inputs.

We tend to call our assumptions before the program to be "preconditions" and the resulting statements at the end to be "postconditions".

```java
// Precondition: x >= 0
int y = 2 * x;
// Postcondition: y >= 0
```
Now notice that our postcondition here just says that y is not negative, but we actually know much more about the relationship between x and y. We tend to ask for the *strongest* postcondition for any given precondition. In this case it becomes:
```java
// Precondition: x >= 0
int y = 2 * x;
// Postcondition: y >= 2 * x && x >= 0
```

We can also ask for the inverse, given a postcondition, what needs to be true:

```java
// Precondition: ?
int y = x - 2;
// Postcondition: y >= 0
```

One simple answer is for example ``x == 10``. But that's boring, that's just one simple case. We want to have the least restrictive precondition, what we call the *weakest* precondition:
```java
// Precondition: x >= 2
int y = x - 2;
// Postcondition: y >= 0
```

We can reason about these in conditionals as well:
```java
// Precondition: x >= 0
if (x <= 10) {
	x += 5;
} else {
	x -= 5;
}
// Postcondition: x >= 5
```

But loops are more complicated. Because a loop can run an indefinite number of times, we cannot just repeat our rules for every iteration. Instead we need some statement that needs to be true for the entire loop. We call this the loop invariant:
```java
// Precondition: x >= 0 && x == X
int y = 0;

// Invariant: 3*x + y == 3*X && y >= 0 
while (x >= 0) {
	y += 3;
	x--;
}
// Postcondition: y == 3*X
```
Notice how that loop invariant needs to be true for each iteration. Notice also that it does not guarantee termination of the loop (oh no).

### Big-O Notation
Moving on to an algorithms subject. We know that different programs run for different time. We know that some programs are much faster at doing the same thing than others. But now paradoxically, some programs are faster for some inputs and slower for others:

```java
fibo(int N) {
	if (N < 2) {
		return 1;
	}
	return fibo(N-2) + fibo(N-1);
}

fibo_fast(int N) {
	int a = 1;
	int b = 1;
	for (int i = 0; i <= N - 2; i++) {
		int next = a + b;
		a = b;
		b = next;
	}
	return b;
}
```

A naive way to talk about speed of programs is to just talk about how many "steps" it takes to execute the program for a few inputs. In this case we may be able to see that ``fibo_fast`` takes fewer steps than ``fibo`` as soon as N gets larger and larger.

Formally we say the runtime of ``fibo`` grows asymptotically faster than the runtime of ``fibo_fast``. With some induction we can prove the number of statements that ``fibo`` executes grows at an exponential rate in terms of $N$. That is very slow for big N. On the other hand, our fast method can be analysed to have runtime which grows at a linear rate. This can also be written as $$T(\\textrm{fibo}_\\textrm{fast}) \\in O(n)$$
Okay but what does $O$ even mean? It's the "Big-O" notation and it seems like many never learn its proper mathematical meaning.
$$O(g(n)) = \\\\{f \\in \\mathbb{R}^\\mathbb{R}| \\exists c > 0, \\\\; \\exists k \\geq 0, \\\\; \\forall n \\geq k, \\\\; 0 \\leq f(n) \\leq c \\cdot g(n)\\\\}$$
Intuitively: We do not care about adding values or constant factors, we just care about everything that grows as quickly or slower than $g$.

From this it also follows trivially that $O(n) \\subseteq O(n^2) \\subseteq O(2^n)$ etc.

The easiest way to prove that $f \\in O(g(n))$ is via a limit proof:
$$\\lim_{n \\rightarrow \\infty} \\: \\frac{f(n)}{g(n)} = 0$$
You will learn to do this informally, if you haven't already. Including questionable applications of L'Hôpital's rule.

e.g.
$$\\lim_{n \\rightarrow \\infty} \\: \\frac{n^2}{2^n} = \\lim_{n \\rightarrow \\infty} \\: \\frac{2n}{2\\cdot 2^n} = \\lim_{n \\rightarrow \\infty} \\: \\frac{2}{4\\cdot 2^n} = \\lim_{n \\rightarrow \\infty} \\: \\frac{1}{4\\cdot 2^n} = 0$$

The [master theorem](https://en.wikipedia.org/wiki/Master_theorem_(analysis_of_algorithms)) has a silly name. It's not even the coolest theorem of algorithms.
### Algorithms
Algorithms were a buzzword 5 years ago but you now know they are (simply) just common procedures to fulfil a well-defined purpose. They are also incredibly hard to come up with. You learn about [Karatsuba's](https://en.wikipedia.org/wiki/Karatsuba_algorithm) and [Strassen's](https://en.wikipedia.org/wiki/Strassen_algorithm) algorithms.

You know how much the internet loves sorting list algorithms, and now you realise why. It's just what every CS 101 class teaches at the start. Time to start hating on Bubble-sort because it has $O(n^2)$ behaviour and Insertion sort is not much better. This is also where you learn that algorithms should be judged based on their worst-case behaviour. This is why despite being called "[Quicksort](https://en.wikipedia.org/wiki/Quicksort)", it falls in the class of algorithms with $O(n^2)$ runtime for its behaviour on a fully sorted list.

The king and queen of sorting lists are [Mergesort](https://en.wikipedia.org/wiki/Merge_sort) and [Heapsort](https://en.wikipedia.org/wiki/Heapsort). The latter involves a dreadful datastructure you are only now wrapping your head around. You feel silly for all the people who told you that Quicksort is the best when Mergesort is obviously superior. Not only is it superior, it is optimal! You prove that comparison-based sorting can never go beyond $O(n \\cdot \\textrm{log}(n))$ runtime.

But why do we even care about sorting a list? Because then we can search it! Binary-search is your first encounter with "divide-and-conquer" tactics and it is probably still the best algorithm ever invented. When you implement it by yourself for the first time you get the indices wrong and cause an infinite recursion loop.

Indeed, divide and conquer seems incredibly effective at defining the data-structure of binary trees which can dynamically maintain sorted data. [Balanced binary trees](https://en.wikipedia.org/wiki/Self-balancing_binary_search_tree) guarantee fast accesses. They have invariant which can be kept up in very fast runtime, but they use a lot of programmer brainpower to implement.

You learn dynamic programming over a wide range of problems. You argue with friends about dynamic programming versus memoisation, because someone showed you a HashMap. Greedy Algorithm becomes a dirty word.

### Graphs
Another application for algorithms! Graphs have a number of vertices and edges connecting these vertices. You can take walks or paths along these graphs from one vertex (fun singular) to another. Many navigational problems like maps can be modelled and solved within graph theory. Graphs are connected if you can find a path from each vertex to another. Otherwise you have at least one disconnected "island".

Given a starting vertex and end vertex in a graph, we can explore the graph for paths in two main ways: [Breadth-first search](https://en.wikipedia.org/wiki/Breadth-first_search) and [Depth-first search](https://en.wikipedia.org/wiki/Depth-first_search). The former uses a queue, meaning that it will keep on exploring where the distance from the start is the shortest. This means the moment it reaches the end, we know it has done so over one of the shortest paths. The latter uses *recursion* (or a stack) which means it keeps on exploring until it hits a dead-end. It can solve a research tree in Factorio.

Several problems profit from modelling the edges to have specific weights. You may consider these as the "lengths" of the edges, or just how much it hurts to walk over them. This means that breadth-first search with its simple idea of every edge being equal will end up not exploring the fastest path. Instead you will now need to always select the nearest point from the start with a [Heap data-structure](https://en.wikipedia.org/wiki/Dijkstra%27s_algorithm). You sigh, having hoped that you would never need to learn to implement one. At least you don't need to implement that dreadful "Fibonacci-Heap" you read about on Wikipedia.

Things are getting ridiculous, edge weights may be negative destroying the pretty symmetries that Dijkstra's algorithm relies on. [Bellman-Ford](https://en.wikipedia.org/wiki/Bellman%E2%80%93Ford_algorithm) seems like bruteforcing. You find out that if you need to get all routes from each node to another, you can use [Floyd-Warshall](https://en.wikipedia.org/wiki/Floyd%E2%80%93Warshall_algorithm) (cool) and even [Johnson's Algorithm](https://en.wikipedia.org/wiki/Johnson%27s_algorithm) (lame, cheater). 

A [MST](https://en.wikipedia.org/wiki/Minimum_spanning_tree) answers the question of "what if I want to connect all villages in my country to a train network but want to build as little track as possible". To calculate it, it turns out that you can simply add the smallest edge that still connects different things together and three different algorithms you learn about do that slightly differently.


### Linear Algebra
Are you tired of math yet? I hope not, we're only getting started.

You learned about vectors in the before times, but now is the first time you learn about "vector space". Vectors are a way to model any algebra where the elements can be added together and scaled by constant factors. For example points in 3d space behave like the vector space $\\mathbb{R}^3$ describes.

You learn that linear sets of equations can be solved in vector spaces with [Gaussian elimination](https://en.wikipedia.org/wiki/Gaussian_elimination):
$$
\\begin{align*} 2x_1 + 3x_2 - x_3 &= 8 \\\\ -4x_1 + x_2 + 2x_3 &= 3 \\\\ x_1 - 2x_2 + 5x_3 &= -1 \\end{align*} $$
Can be written as:
$$ \\begin{pmatrix} 2 & 3 & -1 \\\\ -4 & 1 & 2 \\\\ 1 & -2 & 5 \\end{pmatrix} \\begin{pmatrix} x_1 \\\\ x_2 \\\\ x_3 \\end{pmatrix} = \\begin{pmatrix} 8 \\\\ 3 \\\\ -1 \\end{pmatrix}$$
And then be turned into row-echelon form
$$
\\begin{pmatrix} 1 & -2 & 5 & | & -1 \\\\ 0 & -7 & 22 & | & -1 \\\\ 0 & 0 & 11 & | & 9 \\end{pmatrix}
$$
Which gives us nice solutions for $x_1, x_2, x_3$ which I will not write down because my example ends up being ugly.

If a matrix has a solution like this for every vector, it is called invertible and we can calculate the inverse through a similar process. The [LU-decomposition](https://en.wikipedia.org/wiki/LU_decomposition) can be used similarly to also solve these linear equations for a matrix efficiently once created.

Now not all matrices have these nice solvable systems, some contain "linearly-dependent rows" and after Gaussian elimination you may end up with something like
$$
\\begin{pmatrix} 1 & 1 & 2 & | & 1 \\\\ 0 & 0 & 5 & | & -1 \\\\ 0 & 0 & 0 & | & 1 \\end{pmatrix}
$$
Now turns out in this case this is no longer solvable due to no values $x_1, x_2, x_3$ fulfilling the last row. But in some cases we may get
$$
\\begin{pmatrix} 1 & 1 & 2 & | & 1 \\\\ 0 & 0 & 5 & | & -1 \\\\ 0 & 0 & 0 & | & 0 \\end{pmatrix}
$$
And now we not only have 1 solution, but infinitely many!

Formally we can say that given an equation $Mx = c$ with $M$ being square, we always have a solution if $M$ has "full-rank" i.e. independent rows. Otherwise we have infinitely many solutions if $c$ is in the "null-space" or "kernel" of $M$ or none if it isn't. Turns out the kernel of a matrix is also linear and a so-called sub-space of it. There are four fundamental sub-spaces and their [dimensionalities are related](https://en.wikipedia.org/wiki/Master_theorem_(analysis_of_algorithms)). 

Two vectors can be orthogonal to one another if their cartesian product is zero. They are [orthonormal](https://en.wikipedia.org/wiki/Orthonormality) if they both have a length of 1. How do we measure the length? With a "norm". A function that for a given vector space gives us a way to measure the length of vectors. (Not to be confused with measure theory.)

We call a square matrix orthogonal if all of its vectors are pairwise orthonormal. (Why we don't call the matrix orthonormal then is a mystery to me.) Turns out that this means $Q^T Q = I$ where $I$ is the identity matrix. Orthogonal matrices have the great property of not changing the length of a vector, meaning that multiplying with them is always some kind of rotation and mirroring process without scaling. The existence of the [QR-decomposition](https://en.wikipedia.org/wiki/QR_decomposition) then means that we can extract the scaling part from any matrix and look at a part that only does mirroring and scaling. Rotation matrices are famously QR.

QR-decompositions are very helpful in solving the (linear) least-squares problem. You know that line-fitting function for datapoints in your favorite Office program? No? Well it makes sure your line defined by a few parameters is as close as possible to all the points by minimising the sum of squared distances. It's really hard to naively optimise a full set of distances, especially if you need to adjust more than 2 parameters. Luckily this particular problem of squared distances can be modelled in n-dimensional space as a projection. $A^T A x = A^T b$ may look the same as $Ax = b$ but it actually doesn't just fail if no solution exists, instead it will find the solution with the least-square distance.

We can measure how a matrix changes vector length with its [determinant](https://en.wikipedia.org/wiki/Determinant). One of the earliest concepts in Computer Science with one of the worst calculations in the general case. You learn how to calculate it for smaller matrices. The determinant can also tell you about if a matrix is singular, i.e. has a kernel larger than the zero vector. This alone already makes it almost worth it.

Getting to the big boy decompositions now. Matrices have eigenvectors, these are the vectors which the matrix simply "stretches" by a given eigenvalue. Each eigenvalue has an eigenvector except when they don't. Except for when it has more than one, thats fine. As long as the geometric multiplicity of it is not smaller than the algebraic multiplicity of it. What's that? Okay so there's this thing called the characteristic polynomial...

Anyway, all matrices that are diagonalizable can be written as $M = PDP^{-1}$ where $P$ contains the eigenvectors and diagonal matrix $D$ contains the eigenvalues. $P$ defines a base change of the normal vector space into one where $D$ can *just* apply scaling and then we move everything back to $P^{-1}$. It's a bit like manoeuvring yourself around a football until you can kick it perfectly straight to the goal and then walking back to your bench. GOAL!

Now, I assume future employers won't accept your explanation of geometric varieties as why your program using cool eigenvalues crashed on the newest matrix. So let's instead use *singular* values and instead of a single matrix we $P$ we need two matrices to do your rotation stuff. This gives us the $SVD$ decomposition $M = U \\Sigma V^H$. Now our singular values are no longer allowed to be complex or negative because all the complex rotation work is done by the other guys. I promise you it's better.


### Logic, Sets and Functions
We can say that something $X$ is true or false. We can combine $X \\land Y$ and know it is only true if both are true. We can create arbitrarily complicated formulae out of these atoms, $\\land$, $\\lor$, $\\neg$. Some of these formulas are always true if another is true, we say one formula is implied by another. The formula that is implied by all formulas is $\\top$ and the one that is implied by none is $\\bot$.

Now consider that we have a set of things, for example $X = \\\\{x_1, x_2, x_3\\\\}$. Now we also have ways to check if something holds for values in a set, for example $p$ is only true for $x_2$, we write $p(x_2)$ holds.

$\\forall$ means "forall", so if we say $\\forall x, p(x)$ we mean the statement "for each element in $X$ we know that the predicate $p$ holds". This is not true in our case, because we can see that for example $p(x_1)$ does not hold. $\\exists$ means "exists". $\\exists x, p(x)$ is true because we can choose $x_2$ and $p(x_2)$ holds. Indeed, $\\forall$ and $\\exists$ are exactly linked in such a way that the negation of $\\forall$ implies there exists at least a single negation. The barber shaves himself.

Let's look back at our collections of things, we called them sets. We know a bunch of sets already, like the natural numbers $\\mathbb{N}$ or the real numbers $\\mathbb{R}$. We can take elements in a set and then say they are contained as follows: $1 \\in \\mathbb{N}$ and $0.5 \\not\\in \\mathbb{R}$. We say that if one set is contained within another, that it is a subset, for example $\\mathbb{P} \\subset \\mathbb{N}$ where $\\mathbb{P}$ is the set of primes. We can define sets with predicates as follows:
$$\\mathbb{P} = \\\\{p | p \\neq 1 \\land \\forall x, \\neg (1 < x < p) \\lor \\neg (\\exists m, p = m \\cdot x)\\\\}$$
Simple really, as long as you stare it a bunch of times. Speaking of a bunch of times, $\\times$ is a symbol to combine sets into sets of tuples. It is associative or not depending on who you ask. Math hasn't advanced far enough yet to tell us.

Given a set, we can have different predicates defined upon it and these predicates can have different properties. The most interesting number as always is $2$, so let's look at predicates which are defined between two values. $x < y$ defines that $x$ is smaller than $y$ which we all know. We probably also intuitively understand that if $x$ is smaller than $y$ and $y$ is smaller than $z$, then $x$ is smaller than $z$. This is called *transitivity*. What $<$ is not is *symmetric*, because we cannot just swap $x < y$ to $y < x$ and still have it be true. Indeed it is *antisymmetric*, because its always wrong for all values. It is also not reflexive, because $x < x$ does not hold.

We call predicates which are transitive, symmetric and reflexive "[equivalence relations](https://en.wikipedia.org/wiki/Equivalence_relation)" and they basically behave like equality but more things are allowed to be equal. All the values which are equal to one-another are collected in an equivalence class. An easy equivalence relation is collecting all the odd numbers in one equivalence relation and all the even numbers in another. We may call this $\\equiv_2$ because it distinguishes based on if values are divisible by 2 or not.

We call predicates which are transitive, anti-symmetric and reflexive together with their carrier set "[posets](https://en.wikipedia.org/wiki/Partially_ordered_set)". These basically imply an order on the set where can say that some values are somehow smaller or larger than others. If we can say for all values that they are either smaller or larger than another, the order is *total*, this is what you expect from your normal $\\leq$ or $\\geq$.

Now it turns out that posets get a lot more interesting if you don't enforce total order. Namely the [Hasse Diagram](https://en.wikipedia.org/wiki/Hasse_diagram) doesn't stay a simple line, but rather becomes this cool web. Now if we can always choose any values in this Hasse Diagram and find a value that is above all of them (join) and a value that is below all of them (meet) then we call it a [Lattice](https://en.wikipedia.org/wiki/Lattice_(order)). Not to be confused with a [Lattice](https://en.wikipedia.org/wiki/Lattice_(group)) even if the Venn diagram of people who know these two concepts is practically a circle we just accept they have the same name. Poor Wikipedia Disambiguation Page. The most notable lattice is the one formed of the divides-by relation $|$ on the set of natural numbers $\\mathbb{N}$.

Now here's the thing, functions are just relations. They are weird relations, where we make sure that each value is only "connected" with one other value and they tend to map from one set to another. So you know what a function is of-course. Take an input, get an output. We go from domain to co-domain. If we hit every value in the co-domain we call the function surjective. If we don't hit any value twice, we call the function invective. If a function does both, it's a bijection and is invertible, i.e. there exists an inverse function $f^{-1}$ Wait but doesn't that mean that only sets of the same size can have bijections between them? For finite sets sure.

Infinite sets are confusing and school probably always hand-waved them anyway. Infinity is not a number. But sets can be infinitely sized. Let's talk about cardinality instead of size. It doesn't make that much sense quantifiying this with numbers anymore, but amazingly, we can talk about if one set is larger than another through injections/surjective.

Consider the set of all natural numbers $\\mathbb{N}$ and the set of all even numbers $E$. Now obviously $E \\subset \\mathbb{N}$, so case closed, E is smaller than $\\mathbb{N}$. Well, not exactly. You see we can define a function $f(n) = 2 \\cdot n$. Now notice that this function hits every even value eventually, and no value is hit twice. So this is a bijective function and therefore $E \\sim \\mathbb{N}$, i.e. they have the same cardinality. We call sets that have the same cardinality (or less but are still infinite, grumble grumble) as $\\mathbb{N}$ countably infinite. $\\mathbb{Z}$ has the same cardinality as $\\mathbb{N}$ due to bijective functions like $f(n) = -1^{n-1} \\cdot \\lceil\\frac{n}{2}\\rceil$.

Now, amazingly, the same does not hold for $\\mathbb{R}$ (or $P(\\mathbb{N})$). They are *larger* than $\\mathbb{N}$ due to something called the [diagonalisation argument](https://en.wikipedia.org/wiki/Cantor%27s_diagonal_argument), which given any supposed surjective function from $\\mathbb{N}$ to $\\mathbb{R}$ can find us a real number not yet mapped. It's magical but also highly useful. You need to know it for the exam. No no no, not by heart, you need to be able to make it for new sets. Stop crying please, it's not that bad yet.


### Modular Arithmetic and Algebras
Now that we have the general concept of relations, let's focus on a specific type: Modular arithmetic. Consider the equivalence relation $\\equiv_n = \\\\{(a, b) \\in \\mathbb{Z} \\times \\mathbb{Z} \\\\; | \\\\; n \\textrm{ divides } (a - b) \\\\}$. Turns out the equivalence classes of this are exactly all the numbers which have the same remainder when divided by $n$. So we have stuff like $1 \\equiv_3 4 \\equiv_3 31$.

Turns out that addition and multiplication still retains the same equivalence relationship. That means
$$(a \\equiv_n b \\land c \\equiv_n d) \\rightarrow a + c \\equiv_n b + d$$
$$(a \\equiv_n b \\land c \\equiv_n d) \\rightarrow a \\cdot c \\equiv_n b \\cdot d$$
This gives us a lot of very strong guarantees to manipulate terms in modular arithmetic. Namely because polynomials are just addition and multiplication if $p$ is a polynomial then we can directly say
$$a \\equiv_n b \\rightarrow p(a) \\equiv_n p(b)$$
Furthermore, if we look at multiplication in specific, we notice that if we repeatedly do it, then we end up back at the same place (assuming $p$ is prime and $x$ is not divisible by $p$):
$$x^{p-1} \\equiv_p 1$$
This is called [Fermat's Little Theorem](https://en.wikipedia.org/wiki/Fermat%27s_little_theorem) to distinguish from the [big theorem](https://en.wikipedia.org/wiki/Fermat%27s_Last_Theorem) which I could prove right now but the margins on this blogpost are too small. The little theorem is a direct consequence of the much cooler [Lagrange's Theorem](https://en.wikipedia.org/wiki/Lagrange%27s_theorem_(group_theory)) which is also absolutely relevant but more annoying to explain.

Turns out that depending on which $n$ we do modular arithmetic on, we have different properties. In specific, multiplication is badly behaved for everything that has a common divisor with $n$. But for everything else, we have a marvellous property: Division. Or rather multiplication by an inverse. Given $a$ co-prime with $n$ we know there exists $a^{-1}$ such that
$$a \\cdot a^{-1} = a^{-1} \\cdot a \\equiv_n 1$$
For example the multiplicative inverse for $7$ in modulo $11$ is $8$, because $7 \\cdot 8 = 56 = 55 + 1 \\equiv_{11} 1$. We can find the modular multiplicative inverse of any number by using the [Extended Euclidean Algorithm](https://en.wikipedia.org/wiki/Extended_Euclidean_algorithm). You should learn it by heart.

Given the set of numbers $Z_n$ (which are all the non-negative integers smaller than $n$ including $0$), we write $Z_n^*$ as removing all the values that are co-prime with $n$ and $0$. The size of this new set can be calculated with the [Euler Totient Function](https://en.wikipedia.org/wiki/Euler%27s_totient_function).

Now, here's the awesome part: We don't even need to talk about modular arithmetic or numbers or anything at all to define these theorems. Rather abstracting away the numbers, we can talk about Algebra. Not the algebra you knew in school, but rather the study of structures.

The monoid is to sets what the monad is to categories of endofunctors. In a monoid you have a set, an operator like $+$ or $\\cdot$ and a few guarantees: You have an element which when used on other elements, does not change them. It is called the neutral element. For example for $+$ we tend to write $0$ for the neutral element and in $\\cdot$ we write $1$. The other property is associative, which means you don't need to use parentheses.

Now monoids are cool, but groups are better. They additionally guarantee that each element has an inverse. This means we can undo our operation. Note that neither monoids nor groups guarantee that the operation is symmetric, so we may have $x \\star y \\neq y \\star x$.

Why are we talking about these monoids and groups? Because modular arithmetic is a great example! $\\langle Z_n; +\\rangle$ is a group, another prominent example is $\\langle {Z_n}^\\star; \\cdot \\rangle$ . This means we can apply our fancy Lagrange's theorem on them. For that we can look at the order of a group, which is just its number of elements, boring. But now if we look at any single one element of a group, it will have its own order! Namely the order is how many times you can repeatedly apply the operation to the element until we get back to the original. In $\\langle Z_5^*; \\cdot\\rangle$ the order of $4$ is $2$ because $4^2 = 16 \\equiv_5 1$.

Now it turns out that groups have certain properties and structures that helps us differentiate them from each other, for example it turns out that $\\langle Z_4; +\\rangle$ and $\\langle Z_2 \\times Z_2; +\\rangle$ behave differently, despite having the same number of elements. We say that two groups behave the same, if they are isomorphic to each other, i.e. if there exists an $f: A \\rightarrow B$ such that
$$\\forall a_1, a_2 \\in A, \\\\; f(a_1) \\star f(a_2) = f(a_1 \\cdot a_2)$$
This concept of isomorphism is very powerful, but you don't know that yet. One useful isomorphism consists between cyclic groups of order $n$, these are groups in which every element has the order of the group. It turns out we can prove that all these cyclic groups are isomorphic to each other. A famous cyclic group of size $n$ is $\\langle Z_n ; + \\rangle$, which basically means that cyclic groups are never more complicated than just addition, they just look more complicated.

All of this group stuff gives us some pretty cool guarantees like associativity and hardness of the discrete log allowing for baby's first cryptographic primitives like [DH](https://en.wikipedia.org/wiki/Diffie%E2%80%93Hellman_key_exchange) and [RSA](https://en.wikipedia.org/wiki/RSA_cryptosystem). Turns out that it's all just isomorphic to addition doesn't make these things unsafe, because finding isomorphisms is hard.

Now if we have a set that behaves well with both $+$ and $\\cdot$, then we may call it a ring. A ring gives us a group with $+$ and a monoid with $\\cdot$ which means we can add normally and not divide. That sounds an awful lot like $\\mathbb{Z}$. And indeed that supports no division except by its [units](https://en.wikipedia.org/wiki/Unit_(ring_theory)) $1$ and $-1$. That's pretty cool. Also distributivity etc. applies which gives us symmetry in addition for free.

Indeed we can create rings of many sizes simply by making polynomials modulo some $n$. For example $Z_2[x]$ describes all polynomials which only have binary coefficients. And indeed under addition they behave the same way as their corresponding binary strings under ``xor`` also known as ``^`` by people who interface more with pointers than exponents. Isomorphism! 

Finally, let's combine all our powers to ask for even more: A group structure in terms of addition and multiplication. This means we can divide now! Fields be praised! (They are called fields, im not just praising agriculture.) And indeed our old friend $\\mathbb{R}$ fulfils this. Also their small sibling $\\mathbb{Q}$ does it as well, whilst being countably infinite. But what about finite fields? Galois fields? Who is Galois? Some guy.

We can construct finite fields by taking our rings modulo an integer and taking them modulo *again* but this time an irreducible polynomial. What is an irreducible polynomial? It's like a prime number but a polynomial. Given such a finite field $Z_n[x]_{p(x)}$ we indeed can find that all polynomials within it have a multiplicative inverse. How do we find it? Extended Euclidean Algorithm again, but even more complicated.

### Proof Systems
Now we had our fancy logic, but turns out that we have not yet discussed how we are supposed to actually prove any of these things. Nonono not just proving stuff by induction, but what a proof even is.

Well turns out that statements are either true or false and we hope to create a system where true statements never imply false statements, we call this *consistent*. We also want to be able to prove all of our true statements so that our system is *complete*.

One proof system is that of [Propositional Logic](https://en.wikipedia.org/wiki/Propositional_logic) which is the one previously discussed. But we can now formally prove statement like $A \\land B \\vdash B$. Well "formally" is an overstatement, we tend to use a bunch of words still. Inevitable unless we want to create some meta-system first.

Stuff gets more complicated with [Predicate Logic](https://en.wikipedia.org/wiki/First-order_logic) where we can use predicates and $\\forall$ and $\\exists$. But we can still establish general statements which are true *for every interpretation* of our predicates. For example $\\forall x, p(x) \\vdash \\exists x, p(x)$.

Given a statement $F \\vdash G$, we can prove it by arguing that for every interpretation $A$ with a non-empty set of elements (also called the Universe $U$) that assigns all predicates, functions and free variables in $F$ and $G$ it holds that if A(F) holds then A(G) holds.

We can also blankly prove some statements to be tautologies, i.e. to always hold. For example the famous  [barber shaving](https://en.wikipedia.org/wiki/Barber_paradox):
$$\\neg \\exists y, (\\forall x, \\neg p(x, x) \\leftrightarrow p(y,x))$$


## Continue reading
Check out [Part 2](https://chluebi.github.io/conundrum/posts/speedrunningmycomputersciencedegree10026/).
















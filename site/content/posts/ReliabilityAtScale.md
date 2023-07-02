---

title: "Reliability At Scale"

date: 2023-07-02

draft: false

  
tags: [featured, informatics, philosophy]
---
A framing device for the role of Informatics in our shared world.

*This is phrased as if it is an objective theory which has found truth in the world. It is not. It is written in that style because that style lends itself to being a heavily abstracted theory. All mistakes are my own.*


### Theory

Informatics is principally the study of manipulation of information. This manipulation is typically done along a given goal, which consists of the description of the input and the desired output. A so-called computation of this output can be called **reliable** if from the described input the output is produced according to the specification.

This mention of reliability very well allows for things like partial success (only gives the correct output 10% of the time) or randomness (shuffling a deck of cards). Both of those things can still be described in the documentation of what the desired output should be. As long as the computation conforms to them, it may be called reliable.

As Informatics was birthed in the theoretical field, it naturally inherits this reliability. In concrete terms, using the Turing Machine as an example, if we can construct a Turing Machine which provably computes a desired output, the reliability is on as firm ground as is logically possible. This is of course because the proof relies on logic itself.
The Turing Machine is immensely powerful. So powerful that I may dare say that the limits of what it can compute need not be considered in application sufficiently close to the real world. 

Therefore, we may say that wherever there is information, computation can be reliably applied to solve every problem *in the theoretical world*.


### Interfaces

I want to expand the notion of ["The Unreasonable Effectiveness of Mathematics"](https://en.wikipedia.org/wiki/The_Unreasonable_Effectiveness_of_Mathematics_in_the_Natural_Sciences)
to "The Unreasonable Effectiveness of Abstraction in Solving Problems in the real world". We teach children math by working this exactly backwards: We introduce them to $<\mathbb{N}_0,0,+>$ by showing one apple and two apples, then bringing them together and asking how many apples we have now. Then we explain that this real life example may be represented by symbols on a page, which in turn represent an algebra structure.
$$1+2=3$$
The fascinating part of course is that once we make this connection, we can study just the algebra to figure out rules. And it turns out that the rules also hold in real life.

Another example closer to informatics is the single source shortest path problem in a graph. This is very applicable to real life, most naturally because quick traversal of some graph-like structure is desirable. We turn the situation into an abstract object, then run the computation to get an output, which we put back into the real world.

I want to put special focus on these transition points between practical situation and the abstract world of theory. This is the job of what I like to dub "interfaces".

#### Input and Output Interfaces
These are the most obvious points where theory and reality rub together. To know how we want to represent the apple amounts, we first have to count them. The counting action is the input interface. Counting is quite trivial, but now consider what the required input interface is for the shortest path problem described before. We will need to construct a graph of something in reality. This can be anything from a simple visual check to the work of hundreds of mapmakers for years. Input and output interfaces are not trivial, and one should pay close attention to who controls the flow of information from real life to the theoretical world.

Because input and output interact with the real world in the most explicit way, they often have high cost associated with them, it is often most efficient to keep oneself in the theoretical i.e., digital realm as long as possible. 

Examples of entire fields dedicated to interfaces are things like Computer Vision for input interfaces and Robotics for output interfaces. Consider that one of the earliest uses of computing in practice was ballistics of missiles, and that was mostly this easy because the problem of "exploding your target" could be reduced "get to the target at high speed". It would've taken a lot more effort if they instead wanted to give the target some flowers.

#### Computation Interfaces
Whereas input and output interfaces had no hand in the actual computation of the problem in the abstract realm, computation interfaces are the ones who exactly facilitate that. The Turing Machine is a single entity which is both "the thing which is doing the computations" and "the instructions of how to do the computations". In the real world this tends to split up into what is colloquially called "the hardware" and "the code".

The hardware principally is an interface to turn a [Universal Turing Machine](https://en.wikipedia.org/wiki/Universal_Turing_machine) into a real life object. The universal part of the Turing Machine describes its ability to execute any program given by the code. The code is the result of an interface transforming the abstract description of the computation into some real life object, often a file, which is in turn stored on the hardware. These interfaces are inherently linked, because any code written has to be compatible with the hardware it should run on. This where you both find your human programmers and tools like compilers.


#### Humans are good interfaces
Humans, in their endless complexity and ability, are so powerful they can indeed at any point in time become any of the interface types mentioned. Just consider that a job like data entry is mainly a human using their very sophisticated vision and motor control in concert with a keyboard as an input interface. Arguably, even more powerful humans are at output interfaces: The ability to persist in the world and do fine motor manipulations are invaluable to actually getting something done in the real world. Evolution!

One does not tend to see humans much as hardware, mostly because it is arguably the interface with the most monotonous and least flexible job. Instead, humans are incredibly suited for telling said hardware what to do. Consider that it is called programming **language**, because it should be legible to human programmers.


#### The 5 steps to solving a problem
From the these interfaces, we can describe the five areas that one is concerned with when solving the problem:

0. Solving the abstract problem
1. Turning Real-Life into the input for the abstract problem (Input Interfaces)
2. Putting the output into practice (Output Interfaces)
3. Creating Physical Objects that can compute the output (Hardware Computation Interfaces)
4. Turning the abstract computations of step 0 into a form which step 3 can execute (Codewriting Computation Interfaces)

A quirk of these categories is that they are all specific to a given problem. Consider solving a physical Sudoku as the problem. The Input interface in this case is of course recognizing the physical Sudoku, with, e.g., Computer Vision. But of course, recognizing the written digits can be a problem in and of itself. Which brings me to the next section.


### Modularity
The concept of modularity as used here is the idea that you can solve one problem, package up the solution to that problem to then use it as a building block to solve another problem. I would hesitate to call modularity an inherent property of informatics, but it is an inherent trend of informatics. The fact that we can reliably, reproducibly solve a problem means that it becomes very efficient (in terms of effort) to re-use that solution.

Compatibility is a child of modularity. The idea that things in one representation should be able to be turned into a different representation only becomes relevant once a problem in that new representation has already been solved. A very bare-bones example of this is a [transpiler](https://en.wikipedia.org/wiki/Source-to-source_compiler).

This extreme efficiency of modularity means that large swaths of labour in informatics are spent not on actual problems in the real world but finding solutions which can later be building blocks to solving said problems. Why? Because once a problem is solved once, it can be solved infinitely many times.

### Scale
There are many things in the world which solve problems. A hammer solves the problem of a nail. Of many nails, even. Once you built the tool for the job, it can do a lot of solving. But you still only have one tool.

The theoretical world is not concerned with things like "existence". As such, it is also not concerned with how many of a thing exist. But what it is concerned with is consistency, reproducibility, reliability. If this can be transferred into the real world, we can harness it as much as we want. Because it is consistent.

Of course, if you only have one computer, it is just as limited as the single hammer. But compared to the hammer, the computer is universal. This is where the incentive structure beautifully collapses into why informatics is so powerful: Computers are universal, and therefore you can produce them without needing to know which problems they are supposed to solve. Therefore, no matter what you want to solve, you need just a computer. This in turn means computers can be produced at absurd rates. And now they're everywhere.

Consistency begets Universality.
Universality begets Scale.

Writing code to solve the shortest path problem in one programming language can be compiled to run on practically any computer in the world. Consider the theoretical benefit which can be gained from just [a few hours of work](https://xkcd.com/1205/).

There are of course limitations to scale: Notably in the areas of distribution of software (nowadays mostly solved by the internet), in the compatibility of software to hardware (nowadays partially solved by compilers) and by the fact that computers are still physical objects which take up physical space and **energy**. Scale at solving subproblems inside a larger problem is also [known and studied](https://en.wikipedia.org/wiki/Parallel_computing).

Despite all this, informatics is still unique in the insane cost/benefit it can enable at solving problems **reliably at scale**.
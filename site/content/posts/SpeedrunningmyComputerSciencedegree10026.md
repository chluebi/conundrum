---
title: Speedrunning my Computer Science degree [100%] (2/6)
date: 2025-12-15
draft: false
tags:
  - personal
  - featured
  - speedrunning-computer-science
---
Clickbait Title: Lazy evaluation.

#### Background
See [Part 1](https://chluebi.github.io/conundrum/posts/speedrunningmycomputersciencedegree10016/).

### Interim
As previously said, this entire post is mostly motivated by spite. Now, sadly, this can be interpreted as some kind of exceptionalism or superiority complex which I hope to thoroughly avoid. The spite is instead rooted in being misrepresented to a wider audience of people, specifically ones which may be interested in studying Computer Science.

I think the tone is hard to judge here, because speedrunning tends to convey some level of effortlessness and the jokes make it feel as if the narrator feels above the material. Neither is true and I hope indeed that by sheer effort that goes into writing so much, I prove that I do this because I love the subject matter.

Note also this is very autobiographical and other people will remember other facts better or worse than me. Indeed, other people may have completely different experiences. I know some of them and they do not study Computer Science anymore, having moved on to greener pastures. I wish them the best.

Don't use this as a study guide or a substitute for actual material.

# Semester 2
Remember when we talked about actual code instead of just maths? Me neither.

### Completeness and Limits
$\\mathbb{R}$ and $\\mathbb{Q}$ are both fields, but one of them is notably "fuller" than the other. So where all the extra numbers in $\\mathbb{R}$ (also called the [irrationals](https://en.wikipedia.org/wiki/Irrational_number)?). Well in all of the gaps!

Let's define two sets $X$ and $Y$ and $X \\cap Y = \\emptyset$ with all values in $X$ being smaller than values in $Y$. Then we can always find a value $s$ inbetween, i.e. larger than all values in $X$ and smaller than all values in $Y$. 

Wait is that not trivial? In $\\mathbb{Q}$ we can always find a number between two other numbers. For example by doing $s = x + \\frac{y-x}{2}$. Well, sets are a lot more complicated than numbers! Consider $X = \\left\\\\{x \\in \\mathbb{Q}|x \\cdot x \\leq 3\\right\\\\}$ and $Y = \\left\\\\{x \\in \\mathbb{Q}|x \\cdot x > 3\\right\\\\}$. Notice that both sets are only defined via rational numbers, but if we try to find some kind of rational number which gives us the upper bound for $X$ or the lower bound for $Y$ we end up with trying to use better and better approximations for $\\sqrt{3}$. Indeed the formal maths-y way to talk about this is "[completeness](https://en.wikipedia.org/wiki/Real_number#Dedekind_completeness)".

Now $\\mathbb{R}$ contains all of these numbers, what do we do with them? Let's look at a simpler set $X = \\left\\\\{1 - \\frac{1}{n} \\in \\mathbb{Q}| n \\in \\mathbb{N}\\right\\\\}$. We know from completeness that it has a least upper bound. But what is this least-upper bound? Let's write it as a series instead: $n \\in \\mathbb{N}, 1 - \\frac{1}{n}$.

We can argue that it is monotonically increasing (increases by at least a little bit every step), and it seems like we get closer and closer to $1$. Now here's the crux: We can play a game with a supposed friend about this. Our friend claims that clearly it will never get very close to $1$. So we ask them, okay give us a value $\\delta$ and we shall prove to you that all values in the series after some point $N$ have a smaller distance from it. In formulas:
$$\\forall \\delta > 0, \\exists N \\geq 0, \\forall n > N, |(1 - \\frac{1}{n}) - 1| < \\delta$$
See how useful these quantifiers are! Now let's prove it. We shall build a machine that chooses the correct $N$ for any $\\delta$. Simplify:
$$\\forall \\delta > 0, \\exists N \\geq 0, \\forall n > N, \\frac{1}{n} < \\delta$$
We know that $\\forall A, \\forall n > A, \\frac{1}{n+1} < \\frac{1}{A}$. This gives us the easy choice of $N = \\lceil\\frac{1}{\\delta}\\rceil+1$:
$$\\forall \\delta > 0, \\forall n > \\lceil\\frac{1}{\\delta}\\rceil+1, \\frac{1}{n} < \\delta$$
Notice that for $\\delta \\geq 1$ we have $\\lceil\\frac{1}{\\delta}\\rceil = 1$ and therefore:
$$\\forall \\delta > 0, \\forall n > 2, \\frac{1}{n} < \\delta$$
which is true because $\\frac{1}{n} < \\delta$ for $n > 2$.

For $\\delta < 1$ we have $\\lceil\\frac{1}{\\delta}\\rceil+1 \\geq \\frac{1}{\\delta}+1 > 1$ and therefore we can rewrite it as:
$$\\forall \\delta > 0, \\forall n > \\frac{1}{\\delta}+1, \\frac{1}{n} < \\delta$$
Now we know $n > \\frac{1}{\\delta} + 1 \\Rightarrow \\frac{1}{n-1} < \\delta$ and therefore $\\frac{1}{n}  < \\frac{1}{n-1} < \\delta$.

What we just proved is something called "the limit of the series $1 - \\frac{1}{n}$ is $1$" or $$\\lim_{n \\rightarrow \\infty} 1 - \\frac{1}{n}$$
Turns out that some series don't have a nice limit like this, instead they diverge, either by going towards some kind of infinity or just never settling down at one point. For example
$$\\lim_{n \\rightarrow \\infty} \\left(-1\\right)^n$$

Now turns out that these limits can also be used in a slightly different way to argue about any variable "tending towards" something:
$$\\lim_{x \\rightarrow x_0} f(x) = c \\iff \\forall\\delta > 0, \\exists \\epsilon > 0, |f(x_0+\\epsilon) - c| < \\delta \\land |f(x_0-\\epsilon) - c| < \\delta$$
And we can prove these limits similarly. This is the [epsilon-delta limit](https://en.wikipedia.org/wiki/Limit_of_a_function#(%CE%B5,_%CE%B4)-definition_of_limit) of a function which you've learned in blackpenredpen videos.

Turns out that this does not always happen! Consider the step function
$$ H(x) = \\begin{cases} 0, & \\text{if } x < 0 \\\\ 1, & \\text{if } x \\ge 0 \\end{cases} $$
If we end up trying to approach the limit at $x=0$ we end up finding that if we approach from the negative side we stay at $0$ and from the positive side we get $1$. We can also write this like that:
$$\\lim_{x \\rightarrow 0^-} H(x) = 0$$
$$\\lim_{x \\rightarrow 0^+} H(x) = 1$$
We can also talk about the behaviour of functions if they get larger and larger (with no upper bound), we then say that the limit is "equal" (eek) to $\\infty$ or for ones getting smaller than any value we can find $-\\infty$:
$$\\lim_{x \\rightarrow 0} \\frac{1}{x^2} = \\infty$$
If a function has a limit for each value, i.e. we can always approach from both sides and end up at the same value, then the function is "continuous". All bounded normal functions you know are continuous, so it's a bit boring. But there are also some weird functions which are continuous, so watch out! A function is uniformly continuous if you don't need to build a new epsilon delta machine for each value and instead just can use the same one for all values.

Continuous functions never have these weird "jumps" or "gaps" in them, which means that the [intermediate value theorem](https://en.wikipedia.org/wiki/Intermediate_value_theorem) applies.

### Derivatives
Now, we have our continuous functions and we have this concept of approaching from both sides. Now imagine approaching from both sides *again*, but this time we split the difference. Imagine taking a point on a function and then moving it a little bit along our function. Then draw a line between both points. This line (or rather its steepness) says something about how the function is moving (up or down) between the two points. Now here's the genius part: We move the points together, like infinitely small together.

We define the derivative as follows:
$$f'(x) = \\lim_{h \\rightarrow 0} \\frac{f(x + h) - f(x)}{h}$$
Note that this is again a function! We're creating functions out of functions. Now you can prove all of your silly derivative rules you learned in high-school rigorously! Try it on this:
$$f(x) = |x|, f'(x) = ?$$
What do you mean it doesn't work? $|x|$ is a continuous function. Well turns out that there are continuous functions that are not differentiable! Even worse [they look very cool](https://en.wikipedia.org/wiki/Weierstrass_function). See all those sharp corners? This is a great indicator for a non-differentiable function! Luckily all your favourite functions are differentiable.

Now that we've defined the derivative we can of-course repeatedly apply it. So we can calculate the $n$-th derivative! Many of our best friends are again infinitely derivable or "[smooth](https://en.wikipedia.org/wiki/Smoothness)". Second-Derivatives intuitively tend to measure the curvature of a function.

Now turns out that because derivatives approximate a function's behaviour around a certain point, if we just use all of the derivatives we tend to be able to approximate the function around a point $a$:
$$f(x) = f(a) + \\frac{f'(a)}{1!}(x-a) + \\frac{f''(a)}{2!}(x-a)^2 + \\frac{f'''(a)}{3!}(x-a)^3 + \\cdots$$
This totally works every time and [you should never question it](https://en.wikipedia.org/wiki/Analytic_function). This is called a [Taylor series](https://en.wikipedia.org/wiki/Taylor_series). A lot of your best friends have very famous Taylor series approximations, indeed stuff like $e^x$, $\\sin$ and $\\cos$ can be defined purely through these. Everything [is a polynomial](https://en.wikipedia.org/wiki/Power_series)! Now these power series don't need to be built from derivatives, they can be defined however you want. And there's a bunch of ways to find out [if they converge](https://en.wikipedia.org/wiki/Power_series#Radius_of_convergence). Watch out, infinite sums are weird! Else you might end up calculating $-\\frac{1}{12}$.

### Integrals
Consider the following: If a derivative describes the infinitesimally small change a function does at a certain point, what do we get if we add all of these small changes up again? The function!
$$\\int f'(x) dx = f(x)$$
Now what is that weird $\\int$ symbol? It is basically the continuous version of the sum $\\Sigma$ : Instead of splitting up an interval into finitely many pieces with a length, in the limit we have infinitely many partitions. Now for each of these partitions we take the largest value of the function and create our little rectangles we sum up from it. But hey why not also take the smallest value? If the function is well-behaved (i.e. integrate-able) they should agree!


So let's calculate this sum of values of a function from $a$ to $b$ of $f(x)$:
$$\\int_a^b f(x)$$
Now it turns out that there tends to be a function of $F(x)$ called the anti-derivative of $f$ which exactly fulfils the following property:
$$\\int_a^b f(x) = F(b) - F(a)$$
So if we can find $F(x)$ then calculating these infinite sums becomes really easy. But of course you already know all the boring rules for this from school. Consider taking part in an [Integration Bee](https://youtu.be/6wgntpgO-Kc) and get humbled in speed.

### More Graph Algorithms
Algorithms are everywhere, or at least they were in 2017, now they've all been replaced with AI. Well here we still learn them because we are so nostalgic about them!

Back to graphs, some graphs are [Eulerian](https://en.wikipedia.org/wiki/Eulerian_path) which means we can take all of the edges without visiting any edge twice in one nice tour. Perfect if you want to see all bridges but I suppose hate repetition? Turns out the criterion for this is surprisingly local, with each vertex just needing to have an even degree. Or if you have a starting and end point in mind, those two are allowed to be odd. The algorithms to actually compute the path are annoying!

You know what's even more annoying? NP-completeness! What is that? No idea, but I heard you can win a million dollars. One of those things is the [hamiltonian cycle](https://en.wikipedia.org/wiki/Hamiltonian_path)problem. The big cousin of the eulerian cycle where you can only visit each vertex once but want to visit all of them. Closely related is the  [travelling-salesperson problem](https://en.wikipedia.org/wiki/Travelling_salesman_problem). They both have algorithms but those run in exponential time, horrible.

You know what's even more horrible? coloring! Coloring a graph that is. We can color the vertices of a graph in $N$ different colors to get an $N$-coloring as long as no two vertices with the same color are connected via an edge. Now there is a very easy greedy algorithm which can find 2-coloring for us. Three-coloring at least still has some smartness to it. But in the general case? Bad, very bad. Although there is a level of Boltzmann-intelligence to the greedy coloring algorithm: Given it chooses the correct order of vertices to color, it can always find the optimal solution that uses the least colors. The problem is finding that correct order.

Remember depth-first-search? We finally have a use for it. Given a starting point as a root, we can now create a tree from it and all the edges which don't fit in it are called back-edges and their existence in any given graph is exactly the reason we cannot find a topological sort.

Now what if you want to get married on a graph? Let's find a [Matching](https://en.wikipedia.org/wiki/Matching_(graph_theory))! We can choose any edges and then the two vertices of that edge are monogamously married, so we cannot choose them again. A set of edges like that is a matching. Turns out constructing these matchings is possible eagerly until we get a local maximum. But depending on how lucky we are there's a better *maximum matching* and if we can even get every vertex involved a *perfect matching*.

We can make every matching better if we find an augmenting path: It's a path which starts and ends at two vertices which are not involved in the matching yet. Now we know that a path consists of distinct edges. The most number of edges from the matching we can have involved in this augmenting path is actually not that many: The first and last edge can't be in it, because the starting and end vertices are free. So we can only alternate edges in-between. Either way, we shall now simply choose to remove all the edges from the path from the matching and then following the path alternatingly add an edge to the match and then again not. Doing this in a smart way is [the algorithm](https://en.wikipedia.org/wiki/Hopcroft%E2%80%93Karp_algorithm) for finding maximum matchings.

Got room for one more graph problem? This one is a so-called [max-flow problem](https://en.wikipedia.org/wiki/Maximum_flow_problem). Imagine a weighted graph with a well-defined sink and a source and each edge having a weight which defines how much "capacity" it can take. Now imagine water pumping out of the source and wanting to flow to the sink. What is the maximum "flow-rate" of water that can flow into the sink?

We can define a flow as a function that tells us in each edge how much water is flowing through it. Notably this flow has to respect the capacity of our pipes, as well as not allowing to make water disappear or reappear randomly. Now one way to reason about the maximum flow of this network is for any given flow $f$ to calculate how much more water could flow through each pipe (bounded by capacity). This is the "residual network". Now given any path from source to sink in this residual network we can take the minimum of all left-over residue capacities and direct more water along that entire path to the sink, and therefore increase our flow. This is the "[Ford-Fulkerson Algorithm](https://en.wikipedia.org/wiki/Ford%E2%80%93Fulkerson_algorithm)"  or if you don't like arguing about integer capacities there's [alternatives](https://en.wikipedia.org/wiki/Edmonds%E2%80%93Karp_algorithm).

Now let's talk about the *totally unrelated* topic of "cuts" in networks. Let's say we split the network vertices into two parts, one part contains the source the other the sink and the two parts are within themselves connected. Then for any given flow we can determine how much water is flowing from the source set to the sink set. Now here's the fascinating part: If we find the cut which the smallest such flow (in terms of capacities) from one part to the other, then it is [equal to the maximum flow](https://en.wikipedia.org/wiki/Max-flow_min-cut_theorem). Some intuition on this: Because one part contains the source and the other the sink, surely everything that flows from the source to the sink, needs to flow across your minimal cut still. But also if there was a cut larger than this, then everything also needs to flow across *that* cut and therefore that would imply a larger max flow. Totally unrelated.

### Probability
Given a set of $\\Omega$ of core events, we can give each of these core events a probability of happening: $\\textrm{Pr}[\\omega_i]$. At any point only one core event will happen. Now we can construct larger events as sets of those core events. For example we can roll a dice with $\\Omega$ being numbers $1$ through $6$, with $E$ being the even rolls and $O$ the odd rolls. Given a fair dice, we know all core events have a chance of $\\frac{1}{6}$ and therefore $E$ and $O$ each have a chance of $\\frac{1}{2}$.

These events may overlap, be combined and subtracted from one another like normal sets and normal set rules apply. In particular there's a very cool way to argue about if you know one event happened, another will happen too. Consider the following: I tell you a rolled a dice and a number above $3$, what's the chance I rolled an even number? We define this as follows:
$$\\textrm{Pr}[\\textrm{Even}|\\textrm{Number above 3}] = \\frac{\\textrm{Pr}[\\textrm{Even } \\cap \\textrm{ Number above 3}]}{\\textrm{Pr}[\\textrm{Number above 3}]} = \\frac{2}{3}$$
In a way we constrain the space of all the possible outcomes to only the ones of our dependent event and then count all the probabilities in which our new event happens. Speaking of counting, I hope you did not sleep in your combinatorics class.

Two events are independent if $\\textrm{Pr}[A|B] = \\textrm{Pr}[A]$, allowing for a bunch of easier rewrite rules and making our life easier in all calculations.

Random variables are functions which have different values depending on core events. We can quantify each event of a random variable having a certain value. Let $\\Omega$ describe all 36 outcomes of rolling two (fair) dice. We can define $S$ as the sum of those dice. Then as every good Catan player knows we have $\\textrm{Pr}[S = 7] = \\frac{7}{36}$.

Given $X$ and $Y$ as the values of the two dice we can make the following statements: $X$ and $Y$ are [uniformly distributed](https://en.wikipedia.org/wiki/Discrete_uniform_distribution) from $1$ to $6$, i.e. every value has the same probability. Let $1_{X > 3}$ be the variable which is exactly $1$ when $X > 3$ and otherwise $0$. This is called [Bernoulli-distributed](https://en.wikipedia.org/wiki/Bernoulli_distribution). There are many other distributions for random variables like [Binomial Distribution](https://en.wikipedia.org/wiki/Binomial_distribution) or [Geometric Distribution](https://en.wikipedia.org/wiki/Geometric_distribution). A set of Random variables is independent if for each event $X_i = x$ it is independent of all $\\cup$ and $\\cap$ combinations of the other events. Pairwise independence does not suffice for [evil reasons](https://en.wikipedia.org/wiki/Independence_(probability_theory)#Pairwise_and_mutual_independence).

Given any random variable, we can calculate its [expected value](https://en.wikipedia.org/wiki/Expected_value) $E[X]$ by finding out what the "average value" the variable has over all core events, weighted by their probability:
$$E[X] = \\sum_{\\omega_i \\in \\Omega} \\textrm{Pr}[\\omega_i] \\cdot X(\\omega_i)$$
The expected value is linear, which makes everything much easier. Never calculate a big sum when you could just be using the linearity of the expected value.

Given the expected value $\\mu$ of a variable $X$ we can now calculate its variance:
$$\\textrm{Var}[X] = E[(X - \\mu)^2]$$
Intuitively, the variance measures how much the values of a random variable are away from the average. A variable which never changes value has a variance of $0$. The variance is additive for independent random variables. It squares constant factors, due to the square in its formula.

There are bunch of inequalities you can apply to random variables which dependen on the expected value or the variance, making it so that you can get some great bounds on them. [Markov's inequality](https://en.wikipedia.org/wiki/Markov%27s_inequality), [Chebyshev's inequality](https://en.wikipedia.org/wiki/Chebyshev%27s_inequality) and [Chernoff Bounds](https://en.wikipedia.org/wiki/Chernoff_bound) are very useful indeed.

Because we understand probability now, we can use it to add controlled randomness to our algorithms. But isn't randomness always worse than knowing what you want? Yes probably, but sometimes we don't know what we want and always doing the same thing is actively worse. Considering quicksort: Now that we can randomly choose the pivot, we can actually prove that the average runtime is $O(n \\log n)$, so that's why quicksort doesn't suck!

Indeed there are two main ways to argue about random algorithms: Either we run the algorithm and wait for it to stop. Because it is randomised we now have an indeterminate runtime, we call those Las Vegas algorithms. Instead we may have an algorithm with a definite runtime but a chance of failure. We call this a Monte-Carlo algorithm.


### Geometric Algorithms
Now let's look at another class of algorithms which happen in some n-dimensional space. Given a set of points we want to find the convex hull (i.e. the set of all points which can be arrived at by any weighted average between our original set of points). Specifically we can prove that there will always be a subset of these points that define said convex hull. 

The easiest way to do this is to [wrap it like a gift](https://en.wikipedia.org/wiki/Gift_wrapping_algorithm): Start at the left-most point (guaranteed to be in the hull) and check for all the lines you could draw from it to all other points and choose the one where all points are to the right of the line. Then repeat with the new point that is connected through the line. If we [sort the points smartly first](https://en.wikipedia.org/wiki/Graham_scan) we get a better algorithm.

Now another algorithm in the geometric realm is to find the smallest enclosing circle of a set of points. Now it turns out we can prove that such a circle always intersects at max three of the points in the set, so the actual difficulty is finding these three points. There is quite a trivial algorithm if you are aware of probabilities: Simply choose three points, draw a circle and then double the "weighting" of all points outside the circle, so that they are more likely to be chosen. All the points which need to be on the circle as to be enclosed end up doubling incredibly quickly, giving us $O(n \\log n)$ runtime. There are some [better algorithms](https://en.wikipedia.org/wiki/Smallest-circle_problem).

Now some of these algorithms generalise really well into higher dimensions and some don't. There are some really smart ways to deal with a huge set of "[linear programs](https://en.wikipedia.org/wiki/Linear_programming)" in any dimension. For example max-flow may actually be encoded as linear constraints. Fascinatingly we may also think about it as wanting to find the highest point of an n-dimensional polygon. In this world our augmenting flow paths were actually us climbing along edges of this polygon until we get to the top.

### Parallelism
Having learned Java now, we may indeed notice that we can run two Java programs at the same time without much slowdown. This is because computers can run programs in parallel, indeed they are designed to do so. And indeed many programming languages help you facilitate this in different ways.

The main problem with having "concurrency" in a single program tends to be that you have several different threads acting on the same data. This means that certain sequential guarantees [go out of the window](https://en.wikipedia.org/wiki/Race_condition). Java has [some guarantees](https://en.wikipedia.org/wiki/Java_memory_model). But really it will still shock you. And indeed if you wanted to always have as much guarantee as possible, making all your variables [atomic](https://en.wikipedia.org/wiki/Atomicity_(database_systems)), you may see some heavy performance hits.

So the name of the game tends to be minimising the data that two threads are concurrently working on. Often this can be done by smartly *splitting* the workspace (as seen in divide-and-conquer) algorithms and then having a single sequential thread do all the work. Ideally you want to be able to spawn "virtual threads" which may or may not be connected to actual hardware threads. Java for example allows you to have a Threadpool or an Executor. For similar reasons we also want to be able to sleep threads until they are woken up again by certain events.

Another approach is the idea of pipe-lining: If we can split up the work needing to be done between different specialised machines, we can simply put workload 1 into machine A, then when its done put workload 1 into machine B, and put workload 2 into machine A etc. The general example used here tends to be a washing machine and a dryer. It's a good idea to remind computer science students of these concepts.

A bunch of algorithms may be parallelised through iterative applications of things like ``map``, ``reduce`` and ``filter`` operations.

How fast can we actually go with our many threads? Surely we can go infinitely fast if we have infinitely many threads? Well... remember we still tend to want to have one single result and some agreement between threads on the result, otherwise we could also just run the program on a different computer. So there will inevitably be sequential parts $W_s$ in our program next to the parallel parts $W_p$. Let $W$ be the total work on our program and $T$ the time spent on it.
$$W = W_s \\cdot T + W_p \\cdot T \\cdot p$$
Where $p$ is our number of processors. Now let's say we have infinitely much work lined up, so the limiting factor is just through how much we can get through, now let's compare how much work we can get done with $1$ processor vs $p$ Processors and call that the speedup $S$:
$$S = \\frac{W_s \\cdot T + W_p \\cdot T \\cdot p}{W_s \\cdot T + W_p \\cdot T} = \\frac{W_s + W_p \\cdot p}{W_s + W_p} = \\frac{W_s + W_p \\cdot p}{W}$$
If we normalise this to $W = 1$ we get the speedup described by [Gustafson's law](https://en.wikipedia.org/wiki/Gustafson%27s_law):
$$S = W_s + W_p \\cdot p = W_s + (1 - W_s) \\cdot p$$
You can see here that if we increase $p$ to infinity we indeed get an infinite speedup!

But now what if our work is instead constant. I.e. we cannot infinitely scale and instead we can simply reduce the time we take. Then we have this new definition (the units are horrible here, physicists close your eyes):
$$T = W_s + \\frac{W_p}{p}$$
$$S = \\frac{W}{W_s + \\frac{W_p}{p}}$$
With $W = 1$:
$$S = \\frac{1}{W_s + \\frac{1-W_s}{p}}$$
In [Amdahl's](https://en.wikipedia.org/wiki/Amdahl%27s_law) world we are never escaping the best case scenario where the parallelizable part takes basically no time, but the sequential part keeps slowing us down.

### Parallel Primitives
Some areas of code need to have only one thread allowed to at any point in time. We can put a so-called [lock](https://en.wikipedia.org/wiki/Lock_(computer_science))in front of them that only one thread at any one time can acquire and gets released once the thread leaves the locked area. A thread may acquire several locks, although if you do not pay attention to your topological sorting you end up with a [deadlock](https://en.wikipedia.org/wiki/Deadlock_(computer_science)).

There's a lot of ways to implement locks, the simplest is the very silly [spinlock](https://en.wikipedia.org/wiki/Spinlock) where you will inevitably find that if its hit too much you will gain no benefits from concurrency. Exponential backoff, where each thread waits longer before accessing the lock again may help. But better to use something like [Peterson's lock](https://en.wikipedia.org/wiki/Peterson%27s_algorithm) or the [Bakery lock](https://en.wikipedia.org/wiki/Lamport%27s_bakery_algorithm). If we allow more than one thread in our critical section we call this a [semaphore](https://en.wikipedia.org/wiki/Semaphore_(programming)). Another primitive is the barrier which waits for n-threads to reach it until it lets all threads pass.

A lot of these locks will rely on something called [CAS](https://en.wikipedia.org/wiki/Compare-and-swap) which given a memory location will check if it has the given value and if yes set it to a new value. If no, it will simply return false. It [does not solve all of our problems](https://en.wikipedia.org/wiki/Compare-and-swap#ABA_problem), but a lot of them. Doing everything atomically means we can build complex agreements between threads, something called [consensus](https://en.wikipedia.org/wiki/Consensus_(computer_science)). Indeed CAS has a [consensus number](https://en.wikipedia.org/wiki/Consensus_(computer_science)#Consensus_number) of infinity, allowing as many threads as we want to agree on something.

Taking an idea from databases, things you know exist but not how they work, we can also go for a completely new radical approach. We can frame all of our changes to shared memory as a "[transaction](https://en.wikipedia.org/wiki/Transactional_memory)" which gets "committed" at the very end of our codeblock. It may either succeed if it doesn't conflict with any other accesses or it may fail if the underlying data was changed meanwhile.

We may also consider algorithms which are completely distributed to the point that separate nodes make only tiny decision to build a larger consensus, in the most extreme this may be something like distributed dataflow or [sorting networks](https://en.wikipedia.org/wiki/Sorting_network). There's also actor models like [MPI](https://en.wikipedia.org/wiki/Message_Passing_Interface).

Lots of our usual datastructures will need to be equipped with a lock as well or else we break their consistency when accessing them in parallel. But this tends to be slow, so alternatively we can develop [new datastructures](https://en.wikipedia.org/wiki/Skip_list) which are safe for parallel programming.

### Logical Circuits
Last semester we learned about logic. Now we can learn about logic again. Instead of just silly formulas we shall represent everything as logical gates. We first start with the [semiconductor](https://en.wikipedia.org/wiki/Semiconductor), abstract all the yucky voltage and physics away to just interpret signals as either $0$ or $1$. Now with the semiconductor we can construct a bunch of gates, including the ``NAND`` gate. Turns out this is all we need to represent every possible logical interaction, due to [functional completeness](https://en.wikipedia.org/wiki/Functional_completeness). Indeed we can basically create every logical function now, including complicated additions and multiplications.

There's a bunch of smart physics ways to design a way for us to not just run a signal through a circuit but [for the circuit to remember that signal](https://en.wikipedia.org/wiki/Memory_cell_(computing)). But now that we have state in our system, we will want to keep the entire system synchronised with a [clock signal](https://en.wikipedia.org/wiki/Clock_signal). With this we can have systems which may be in a specific state and advance to other states depending on logic and input. Voila, computing! We tricked a rock (silicon) into thinking (doing bit-wise operations).

In the simplest case we may consider only a finite (and small) number of states. Then we can represent each state with a node and edges between nodes which describe how the state changes every clock cycle depending on the input signal. If the output only depends on the state, we call this a [Moore machine](https://en.wikipedia.org/wiki/Moore_machine), if it also depends on the input it's a [Mealy machine](https://en.wikipedia.org/wiki/Mealy_machine).

Now consider a machine which does not only have a small number of states but can read and write data to some kind of memory. We can "program" this machine by writing instructions into its memory which it will execute one by one, manipulating its memory, potentially doing complex operations purely from simple repeated arithmetic calculations. This is called the [Von Neumann Architecture](https://en.wikipedia.org/wiki/Von_Neumann_architecture) model.

In our current times, this is a very simplified model of what a CPU does. In practice we say that the CPU fetches an instruction from memory, decodes it into the actual state of the CPU needed to then execute the instruction. This is the [fetch-decode-execute](https://en.wikipedia.org/wiki/Instruction_cycle) cycle. Generally we also tend to distinguish between a small set of registers which are very easily accessible to the CPU and the large block of memory addressable, giving us storage at the cost of speed.

What instructions our CPU has to follow and what kind of registers it has tends to be defined in its [Instruction Set Architecture](https://en.wikipedia.org/wiki/Instruction_set_architecture). The most well-known ones are x86 which is in your Windows PC and ARM which is in your phone. But don't worry about what they do, they're basically the same anyway.

Whereas the ISA defines the abstract behavior of the CPU so that programmers know what they can use, the  [Microarchitecture](https://en.wikipedia.org/wiki/Microarchitecture) is the nitty-gritty of the implementation. Why do we need this distinction? Turns out Von Neumann was kind of full of shit with the idea of doing instructions just sequentially.

First of all, we probably don't want to have to fit a single instruction in every clock cycle. Some instructions are just slower than others and this means needing to slow our entire clock down. Instead let's give each instruction as many cycles as it needs. Generally we need one cycle for fetching, one for decoding and then a bunch of others for execution. A simple addition between registers may execute in only a few cycles, whilst more complicated operations may stall us for longer. This is the idea of a [multi-cycle processor](https://en.wikipedia.org/wiki/Multi-cycle_processor).

Right, having put the idea of a multi-cycle processor in place, we can actually get to the good stuff. Let's pipeline our entire processor: All of our different logical parts that don't interfere with each other can just happen in parallel. The next instruction can already be fetched whilst the current one is decoding and the previous is executing. Now we've got a whole [instruction pipeline](https://en.wikipedia.org/wiki/Instruction_pipelining)!

Now we're hitting a new performance wall: We cannot execute the next instruction before the previous one finished because they may interfere with each other! Well... who says all instructions interfere with each other? Some may simply, not. Consider the following x86 instructions:
```asm
add ecx, esi
add edi, edx
```
We say ``ecx += esi`` and then ``edi += edx``. These are completely separate in their logic and may therefore happen in parallel! As long as we avoid [hazardous](https://en.wikipedia.org/wiki/Instruction_pipelining#Hazards) instructions, we can execute a lot more in parallel that first thought.

Right, let's do this arithmetic computation in a sound manner. Given an execution of values like the following
```java
w = a + b;
x = a + a;
y = w + c;
z = y + x;
```
We first identify the dependencies of each computation based on previous computations: ``y = w + c`` requires ``w = a + b`` to finish. ``z = y + x`` has to wait for both ``x = a + a`` and ``y = w + c``.  So we can already send the values to the first two instructions ``w = a + b`` and ``x = a + a`` off, as well as the ``c`` in ``y = w + c`` as soon as that instruction decodes. As soon as we get ``w`` computed, we can fill it in the waiting arithmetic unit which now has all values to calculate ``y``. Once ``x`` and ``y`` are ready finally ``z`` can be calculated. This is the essence of [Tomasulo's algorithm](https://en.wikipedia.org/wiki/Tomasulo%27s_algorithm).

Alright, this was it with the elegance, mainly. Sure we can get some performance by [forwarding data](https://en.wikipedia.org/wiki/Operand_forwarding) more directly across decoded instructions. But really I need another big hit. This requires more specialisation. What do programmers need? Depends on who you ask, but it turns out they have a lot of things they tend to over and over. For example they may add vectors to each other. Perfect, let's define an instruction where they can add several numbers to each other at the [same time](https://en.wikipedia.org/wiki/AVX-512). Several instructions one after another, potentially on multiple data inputs? Let's get [specialised hardware](https://en.wikipedia.org/wiki/Systolic_array) just to do that!

Alright, there's these people called graphic developers and they work so much with floating points doing complex calculations, it is actually worth it to give them a special machine which can hundreds of floating point operations in parallel so they can render their polygons on screen. In a simple model we may consider a [GPU](https://en.wikipedia.org/wiki/Graphics_processing_unit) to have several warps which can act on independent data as long as they're all decoding the same instructions.

Now, we've made the distinction between registers and memory. We also know we have few registers but practically limitless memory, but the memory is very slow, especially reading from it. Knowing from programmer usage patterns we also know that memory tends to not be accessed randomly, but rather programmers tend to read and write from the same memory and if they read/wrote from one region, the area around that region is [much more likely to be hit next](https://en.wikipedia.org/wiki/Locality_of_reference). This is why instead of directly accessing our slow memory, we build a [cache](https://en.wikipedia.org/wiki/Cache_(computing)) on top, often with [several layers](https://en.wikipedia.org/wiki/Cache_hierarchy). Our cache distinguishes memory addresses into separate blocks which get loaded into memory as a whole if only one address within the block is hit, aiding local access patterns. The cache will also have a [policy](https://en.wikipedia.org/wiki/Cache_replacement_policies) that considers what to keep in the cache and what to replace, once the cache is full.

Speaking of slow memory, another thing that is slow is waiting for branches. Branches are part of our code where the next instructions differ depending on some result from our code. This tends to happen with if-statements, loops, conditional jumps etc. For this reason, we tend to just *guess* which branch we take. Well, we [predict](https://en.wikipedia.org/wiki/Branch_predictor) it and then just act as if that is the case, meaning we fill up our pipeline etc. and may already precompute entire results. But if we're wrong we have to flush the entire pipeline! So we better predict correctly, based on certain heuristics, mostly leveraging what happened the last few times we took this branch (this is very useful for loops which may take the same direction for a single branch thousands of times).

Also turns out that on the operating system level, the memory we tend to access is actually "[virtual](https://en.wikipedia.org/wiki/Virtual_address_space)" and we just pretend infinite space. Instead we have a certain physical address space we split up into pages, these pages then get mapped to virtual pages and we then let programs write to these virtual pages, continually mapping new ones and recording which physical address maps to which virtual address in a [page table](https://en.wikipedia.org/wiki/Page_table).



## Continue reading
Read [Part 1](https://chluebi.github.io/conundrum/posts/speedrunningmycomputersciencedegree10016/) if you haven't yet.
(Part 3 Coming Soon)















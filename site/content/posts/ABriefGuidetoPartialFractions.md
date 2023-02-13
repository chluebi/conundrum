---

title: "A Brief Guide to Partial Fractions"

date: 2023-02-13

draft: false

  
tags: ["mathematics", "analysis"]
---

### Motivation
Given a complicated fraction, it is often favorable to split it into two separate fractions as such:
$$\frac{1}{6x^2 - 5x + 1} = \frac{2}{2x-1} + \frac{-3}{3x-1}$$
But *how* to do that can be very obtuse, so here is a general guide for the most reliable (but also most time-consuming) method which uses systems of linear equations.


### Step 1: Factoring the bottom part
This is self-explanatory, try to find any way you can split up the bottom part of your fraction into two parts. In the given example:
$$6x^2 - 5x + 1 = (2x-1)(3x-1)$$
This may be done by finding the roots of the polynomial (via the midnight formula) or just trying a few values out.


### Step 2: Establishing a system of linear equations
Now we know our target fraction will look something like this:
$$\frac{1}{6x^2 - 5x + 1} = \frac{A}{2x-1} + \frac{B}{3x-1}$$
Importantly we now need to choose $A$ and $B$ as to get the correct part in the top of the fraction.
Remember how fractions are added:
$$\frac{A}{2x-1} + \frac{B}{3x-1} = \frac{A(3x - 1) + B(2x-1)}{(2x-1)(3x-1)} = \frac{A(3x - 1) + B(2x-1)}{6x^2-5x+1}$$
And this then has to be equal to:
$$= \frac{1}{6x^2-5x+1}$$
So now we have a condition:
$$A(3x - 1) + B(2x-1) = 1$$

Now to get the system of linear equations we split the equation up into two, constants and factors of $x$:
$$x(3A + 2B) + (-A-B) = x0 + 1$$
Note that these two parts act completely independently of each other, which means we can just write them as two separate equations:
$$3A + 2B = 0$$
$$-A - B = 1$$

#### Step 3: Solving the system of linear equations
Almost done now! We just have to solve the system of linear equations. This may be done with any method you want, including the Gauss algorithm. Considering the numbers you get out are often quite nice, it may be advised to just "try numbers".

In any case, the result will be:
$$A = 2, B = -3$$
So we can insert it into the original equation and get:
$$\frac{1}{6x^2 - 5x + 1} = \frac{2}{2x-1} + \frac{-3}{3x-1}$$

#### Notes
There are even more complicated approaches which allow for the direct splitting into three separate fractions, but these are more complicated as you need to pick specific factors.

Just because you *can* use this technique does not mean you should. If for example your top part is still a polynomial and not just a constant, I highly recommend trying long division first.

Also, polynomials in the top part are your friend during integrating, they're often your inner derivative, as the following example shows:

$$\int \frac{24x - 10}{6x^2 - 5x + 1} dx = 2 \int \frac{12x-5}{6x^2 - 5x + 1} dx = 2 \ln \left(|6x^2 - 5x + 1|\right)$$

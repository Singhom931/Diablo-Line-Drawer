# Diablo-Line-Drawer
Diablo's Line Drawer is an alternative Line Drawing Algorithm that avoids Heavy Calculations.

The Most Widely and Commonly used Line Drawing Algo is Bresenham's Line Drawing Algorithm,
For all Mordern Computers this is easy to use and fast,accurate,etc.

But for someone like me who makes virtual computers inside videogames like Minecraft
there's alot of divisons and multiplications in Bersenham's Algo which makes computation slower
and also makes the virtual computers physically massive in size.

This Algorithm aims to solve this issue by avoiding multiplications, using comparisions instead of divisons
and using a division alternative that doesn't involve decimal values or fractions.

Also Avoiding heavy calculations inside loops and replacing them with addition and subtraction.

Explanation:

Starting with Slope this algo doesn't calculate slope as dx/dy or dy/dx instead it compares if dx==dy ,dx>dy or dy>dx for 3 possible slope cases.

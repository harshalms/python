'''CodeForces
A. Stickers and Toys
time limit per test2 seconds memory limit per test256 megabytes
inputstandard input outputstandard output

Your favorite shop sells 𝑛 Kinder Surprise chocolate eggs. 
You know that exactly 𝑠 stickers and exactly 𝑡 toys are placed in 𝑛 eggs in total.
Each Kinder Surprise can be one of three types:
1. It can contain a single sticker and no toy;
2. It can contain a single toy and no sticker;
3. It can contain both a single sticker and a single toy.
But you don't know which type a particular Kinder Surprise has. 
All eggs look identical and indistinguishable from each other.
What is the minimum number of Kinder Surprise Eggs you have to buy to be sure that, 
whichever types they are, you'll obtain at least one sticker and at least one toy?
Note that you do not open the eggs in the purchasing process, that is, 
you just buy some number of eggs. It's guaranteed that the answer always exists.
Input
The first line contains the single integer 𝑇 (1≤𝑇≤100) — the number of queries.
Next 𝑇 lines contain three integers 𝑛, 𝑠 and 𝑡 each (1≤𝑛≤109, 1≤𝑠,𝑡≤𝑛, 𝑠+𝑡≥𝑛) — the number of eggs, 
stickers and toys.
All queries are independent.
Output
Print 𝑇 integers (one number per query) — the minimum number of Kinder Surprise Eggs 
you have to buy to be sure that, whichever types they are, you'll obtain at least one sticker and one toy
Example
input
3
10 5 7
10 10 10
2 1 1
output
6
1
2
'''
def MinKinderSurprise(n, s, t):
    k = s + t - n # k are of a type which contain both a single sticker and a single toy.
    s = s - k
    t = t - k
    if s == 0 and t == 0:
        return 1
    else:
        return max(s, t) + 1
if __name__ == "__main__":
    T = int(input())
    for i in range(T):
        n, s, t = map(int, input().split())
        print(MinKinderSurprise(n, s, t))
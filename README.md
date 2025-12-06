# Bubble-Sort-Simulation
## Why I Chose bubble sort
I chose to visualize bubble sort with early exit, because I believe that it is a good introduciton into sorting algorithms, the proccess it uses to sort is simple, and easy to understand. With other sorting algorthims, the steps for the proccess maybe overcomplicated and hard to understand, while bubble sort only has a O(n^2) time complexity at its worst case, making it relatively simple to follow compared to different sorting algorithims. Through bubble sort's simplicity we can introduce the user to more complicated topics through a simple example, like how time complexities change in worst case versus best case, and how sorting algorithms check if a swap needs to be made. Bubble sort also is very easy to follow, because of how it sorts, checking each item indiviually, then moving to the next until the whole list is sorted. This simplicity is much easier to follow then other algorithims that include recursions, or partitions, which get in the way of learning the basics, such as comparison, swaps, and passes.

## Demo video/gif/screenshot of test
<img width="1895" height="813" alt="image" src="https://github.com/user-attachments/assets/f8c5f01b-44bb-4c20-bf3a-cd0d94fd0756" />
<img width="1905" height="847" alt="image" src="https://github.com/user-attachments/assets/68365f1c-66a6-463f-99ff-8647afef1e5e" />
<img width="1802" height="414" alt="image" src="https://github.com/user-attachments/assets/5f52944d-3742-4af8-a07a-10f97cdb53c3" />
<img width="1789" height="150" alt="image" src="https://github.com/user-attachments/assets/5a8cbca0-5cac-4cbd-bd94-e5826bf68658" />

## Problem Breakdown & Computational Thinking 
<img width="861" height="569" alt="Sort Colors(2)" src="https://github.com/user-attachments/assets/5bf4027f-ae89-43ee-b754-df538b6220f0" />

### Decomposition
Bubble sort consisits of an outer loop which tracks the number of passes, and an innner loop which does the comparisons and swapping. The outer loop initializes a swapped variable to detect if a swap is made for the early exit, and a variable to track where in the list we are. The inner list then checks if a swap needs to be made between the first two elements, if so then they are swapped and the swapped variable is set true, if not the list moves onto the next element, until a full pass is finished. Once a pass is dont we check if a swap is made, if so we continue, otherwise we break and the list has early exited. We keep doing this until the list doesn't swap any elements, meaning its fully sorted.

### Pattern recognition
This algorithm uses a nested while loop to trace through the list, an if statement to compare two values in the inner loop and then swap them, before moving on throughout the list, this continues until the list is fully sorted.

### Abstraction
The details that are shown by my simulation are:
- each pass
- each check
- whether a swap was made
- if the loop early exited

### Algorithm Design
Input:
- integers seperated by commas

Proccessing:
- running bubble sort on the input list
- appending each step to a log

Output:
- a completed step-by-step log
- sorted list

## Steps to Run
Enter numbers, with each number seperated by a comma, then hit the button labeled "Run Bubble Sort".
A log should then appear, with each step the algorithm takes to sort everything.

## Hugging Face Link
https://huggingface.co/spaces/dooperboop/Bubble-Sort-Simulation/tree/main

## Author & Acknowledgment
AI was used to create most of the code for this app, as I was unfamiliar with how gradio worked. I used AI to assist the creation of the my app, while the text used is my work entirely. The AI used in this project was used to create the idea I envisioned within gradio, because of my unfamiliarity with the program.

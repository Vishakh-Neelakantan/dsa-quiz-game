# # This code implements a quiz game on algorithms and data structures.
# # It randomly selects 5 questions from a pool of 100 variants and evaluates the user's answers.


from rich.console import Console
from rich.prompt import Prompt
from rich.panel import Panel
import random

console = Console()

question_pool = [
    {
    "question": "Which data structure is ideal for implementing a browser's back button functionality?",
    "options": ["A. Queue", "B. Tree", "C. Stack", "D. Heap"],
    "answer": "C"
  },
  {
    "question": "Which traversal technique visits all nodes at the current depth before moving to the next depth level?",
    "options": ["A. Inorder", "B. Preorder", "C. Depth First Search", "D. Breadth First Search"],
    "answer": "D"
  },
  {
    "question": "Which of the following algorithms does not guarantee the best solution but is faster for optimization problems?",
    "options": ["A. Greedy", "B. Dynamic Programming", "C. Divide and Conquer", "D. Brute Force"],
    "answer": "A"
  },
  {
    "question": "Which data structure allows fast insertion and deletion from both ends?",
    "options": ["A. Queue", "B. Stack", "C. Deque", "D. Array"],
    "answer": "C"
  },
  {
    "question": "Which tree has the property that every parent has at most two children?",
    "options": ["A. Ternary Tree", "B. Binary Tree", "C. AVL Tree", "D. B-Tree"],
    "answer": "B"
  },
  {
    "question": "Which algorithm is used for solving the single-source longest path in a DAG?",
    "options": ["A. Dijkstra", "B. Bellman-Ford", "C. DFS with topological sort", "D. Kruskal"],
    "answer": "C"
  },
  {
    "question": "What is the worst-case time complexity of inserting an element in a binary search tree (unbalanced)?",
    "options": ["A. O(log n)", "B. O(n)", "C. O(n log n)", "D. O(1)"],
    "answer": "B"
  },
  {
    "question": "Which sorting algorithm selects the smallest element and places it at the beginning in each iteration?",
    "options": ["A. Bubble Sort", "B. Merge Sort", "C. Selection Sort", "D. Quick Sort"],
    "answer": "C"
  },
  {
    "question": "Which data structure is best suited for implementing a scheduling system with priority?",
    "options": ["A. Stack", "B. Queue", "C. Binary Heap", "D. Linked List"],
    "answer": "C"
  },
  {
    "question": "Which algorithm solves the longest common subsequence problem?",
    "options": ["A. Greedy", "B. Divide and Conquer", "C. Backtracking", "D. Dynamic Programming"],
    "answer": "D"
  },
  {
    "question": "Which data structure supports O(1) average-case lookup, insert, and delete?",
    "options": ["A. Hash Table", "B. Binary Search Tree", "C. AVL Tree", "D. Stack"],
    "answer": "A"
  },
  {
    "question": "In which scenario is a trie data structure most useful?",
    "options": ["A. Storing graph edges", "B. Sorting numbers", "C. Prefix-based word search", "D. Balancing search trees"],
    "answer": "C"
  },
  {
    "question": "Which of the following algorithms does not perform comparison-based sorting?",
    "options": ["A. Merge Sort", "B. Heap Sort", "C. Radix Sort", "D. Quick Sort"],
    "answer": "C"
  },
  {
    "question": "What is the best-case time complexity of linear search?",
    "options": ["A. O(n)", "B. O(n log n)", "C. O(1)", "D. O(log n)"],
    "answer": "C"
  },
  {
    "question": "Which of the following is true for AVL Trees?",
    "options": ["A. Balanced only during insertion", "B. Unbalanced Binary Tree", "C. Self-balancing Binary Search Tree", "D. Does not support deletion"],
    "answer": "C"
  },
  {
    "question": "Which graph representation is most space-efficient for sparse graphs?",
    "options": ["A. Adjacency Matrix", "B. Edge List", "C. Incidence Matrix", "D. Adjacency List"],
    "answer": "D"
  },
  {
    "question": "Which of the following is used to convert infix expression to postfix?",
    "options": ["A. Queue", "B. Stack", "C. Tree", "D. Hash Table"],
    "answer": "B"
  },
  {
    "question": "What is the minimum number of nodes in a complete binary tree of height h?",
    "options": ["A. 2^h - 1", "B. h", "C. h^2", "D. log h"],
    "answer": "A"
  },
  {
    "question": "Which data structure is ideal for constant time insertion and deletion at both ends?",
    "options": ["A. Array", "B. Deque", "C. Stack", "D. Queue"],
    "answer": "B"
  },
  {
    "question": "Which algorithm technique is used in solving the Tower of Hanoi problem?",
    "options": ["A. Greedy", "B. Divide and Conquer", "C. Dynamic Programming", "D. Backtracking"],
    "answer": "B"
  },
  {
    "question": "Which of the following ensures O(log n) time for insertions and deletions in a tree?",
    "options": ["A. Binary Search Tree", "B. AVL Tree", "C. Binary Tree", "D. Trie"],
    "answer": "B"
  },
  {
    "question": "Which search algorithm does not require the input to be sorted?",
    "options": ["A. Binary Search", "B. Linear Search", "C. Ternary Search", "D. Interpolation Search"],
    "answer": "B"
  },
  {
    "question": "Which of the following operations is not efficient in an array?",
    "options": ["A. Random Access", "B. Insert at end", "C. Delete at beginning", "D. Update by index"],
    "answer": "C"
  },
  {
    "question": "Which algorithm guarantees finding the minimum spanning tree with a greedy approach?",
    "options": ["A. Dijkstra's", "B. Kruskal's", "C. Bellman-Ford", "D. Floyd-Warshall"],
    "answer": "B"
  },
  {
    "question": "Which data structure is preferred for implementing undo-redo operations?",
    "options": ["A. Queue", "B. Heap", "C. Stack", "D. Linked List"],
    "answer": "C"
  }
    # Add more questions...
]

def play_game():
    score = 0
    selected_questions = random.sample(question_pool, 5)

    console.print(Panel.fit("[bold blue]📘 Welcome to the Algorithms & Data Structures Quiz![/bold blue]\n[dim]Answer 5 questions. +1 for correct, -1 for incorrect. Good luck![/dim]"))

    for idx, q in enumerate(selected_questions, 1):
        console.rule(f"[bold yellow]Question {idx}[/bold yellow]")
        console.print(f"[bold]{q['question']}[/bold]\n")

        for option in q["options"]:
            console.print(option)

        user_answer = Prompt.ask("[bold cyan]Your answer (A/B/C/D)[/bold cyan]").strip().upper()

        if user_answer == q["answer"]:
            console.print("[green]✅ Correct![/green]")
            score += 1
        else:
            console.print(f"[red]❌ Incorrect![/red] The correct answer was [bold]{q['answer']}[/bold].")
            score -= 1

    console.rule("[bold green]🏁 Game Over![/bold green]")
    console.print(f"[bold cyan]Your final score is: [yellow]{score}/5[/yellow][/bold cyan]")

def main():
    play_game()

if __name__ == "__main__":
    main()
    
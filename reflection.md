# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
- List at least two concrete bugs you noticed at the start  
  (for example: "the hints were backwards").

Glitches Observed

First try: guess 88
secret was 60, but app kept telling me guess higher
-New Game button doesn't clear the screen and start a new game until i refresh browser: shows message "Game over. Start a new game to try again." but does nothing
-higher lower appears to be exactly inversed or just totally wrong
-Says I have 1 attempt and out of attempts at the same time
-scoring system inconsistent

**Bug Reproduction Log**

Document at least 3 bugs you found. Add rows as needed.

| Input           | Expected Behavior                 | Actual Behavior                            | Console Output / Error                                               |
|--------------   |-----------------------------------|--------------------------------------------|----------------------------------------------------------------------|
|51,50,35,25,15,10| hints guide me to the actual value| hints have no correlation                  |Out of attempts! The secret was 84. Score: -35                        |
|50,25,35,24,26,25| hints guide me to the actual value| hints have no correlation                  |Out of attempts! The secret was 6. Score: -35                         |
|New Game button  | clear screen and start new game   | game remains the same after completed game |Game over. Start a new game to try again.                             |                        

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?: Claude
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).:

Suggested that the instruction of the app "guess a number" 1-100 didnt change to match difficulty
I verified by running the app
I asked the AI to run suggested changes to fix

- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed? I ran the app again trying to trigger the specific bugs
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.

  Using Pytest I ran a test to fix the hint guess direction. It showed me tests with the new changes and the tests passed

- Did AI help you design or understand any tests? How?
Yes I ran the prompt format "generate a pytest case in test/test_game_logic.py that specifically targets the bug you just fixed." and the AI gave me follow up instructons and test results

---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?:
It is a simple effective method to run webapps and I wuld recommend it

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.: Testing. I want to implement more testing in personal projects
- What is one thing you would do differently next time you work with AI on a coding task?: Be more specific with instructions
- In one or two sentences, describe how this project changed the way you think about AI generated code.: AI wants to make sure I am in control by asking for confirmation for certain unmentioned changes/issues

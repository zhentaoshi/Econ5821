
# Toolkit for Daily Work

## Programming: From R to Python (with Jupyter for demos)

I used to use R as my primary language. Over time, I switched to Python for most new work, largely because it has become the common language across:

- data work (pandas, polars)
- econometrics/statistics (statsmodels, linearmodels)
- optimization and simulation (scipy)
- teaching and tooling (notebooks, scripting, automation)

This is not an argument that Python is "better" than R. It is a pragmatic choice: I want one language that my students can reuse across courses and projects, and that integrates well with modern tooling.

### Jupyter notebooks for demonstration

For teaching and quick demos, Jupyter notebooks remain extremely useful:

- You can mix explanation, math, code, and plots in one place.
- Students can run cells step-by-step and see intermediate results.
- Notebooks make it easy to show "what happens if we change X?"

My personal rule is to separate *demonstration* from *production*:

- Notebooks are great for teaching, prototypes, and exploratory work.
- For research code that needs to be reusable and testable, I move core logic into scripts or modules and keep notebooks as thin front-ends.

This way, the notebook remains readable, and the computational parts stay reproducible.

## Version Control: GitHub as the Backbone

GitHub is the most important platform in my workflow because it makes "work" durable and shareable. Version control is not just for software engineers; for teaching and research, it helps with:

- Keeping lecture notes and code synchronized across devices.
- Rolling back accidental changes.
- Tracking what changed (and why) over time.
- Collaborating with students and research assistants without emailing files.

### A simple, sustainable Git habit

For most teaching repos, I try to keep a simple structure:

- One repository per course (or per major project).
- Clear folders for data, code, and notes.
- A short README describing how to run key files.

And I try to keep commits small and meaningful. A commit message like "update lecture 3 notes" is often enough; for research code, I write more descriptive messages because the history becomes part of the documentation.

## IDE: VS Code as the "One Place" Workspace

I use VS Code as my main IDE because it can be the one place for:

- writing (Markdown and LaTeX)
- coding (Python, R, and more)
- version control (Git integration)
- running tasks (terminals, scripts, and automation)

The biggest productivity gain is not any single feature - it is the reduction in context switching. When I can edit notes, run code, inspect outputs, and commit changes without leaving the same workspace, I spend less time "setting up" and more time actually working.


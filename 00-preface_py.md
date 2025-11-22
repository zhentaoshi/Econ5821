# Preface


Programming is an essential skill for researchers in economic analysis.
In the time of big data, empirical economic research becomes main stream.

I believe the best way to learn programming is to follow examples. These notes contain executable examples that illustrate Python usage and econometric computational ideas.

Econometrics is interdisciplinary study involving economics, statistics, operational research, and computational science. No matter how beautiful is the theory,
it will be of little use if it cannot be implemented. Thus econometric procedure must be accompanied with computational code. Given that many existing methods
are encapsulated in canned packages, they do not cover new methods, which must be developed by econometricians who propose these procedures.

Our econometric procedures are difficult to commercialize.
To facilitate spread, one way is to offer to code for free. The world runs on open-source software.
Many open source software is indispensable for our daily work, for example, Linux, Python, R, and LaTeX.

These lecture notes are products of an ongoing writing project.
They are not intended to be comprehensive.
I don't want to reinvent wheels.
I refer to the relevant papers and surveys when there are excellent writings for mature topics.


## The Impact of AI to Programming

AI-assisted tools now automate many low-level tasks—scaffolding code, translating between languages (e.g., Python and R), generating documentation and tests, and surfacing relevant examples. This shifts the bottleneck from typing code to specifying problems precisely, designing data and software architecture, validating results, and maintaining reproducible workflows. AI can speed prototyping and learning, but outputs can be incorrect. Human review, testing, and version control remain essential.

Students still need to learn programming. Core skills in Python/R, data structures, numerical computing, debugging, testing, and performance are what let you evaluate and adapt AI-generated code, integrate it into real projects, and ensure correctness and reproducibility. In practice, you will use AI as an accelerator: write clear prompts, constrain solutions, verify with unit tests, read source docs, and profile/benchmark critical code. The competitive edge comes from combining conceptual understanding with engineering discipline-—-clean data pipelines, transparent notebooks, reliable environments, and defensible empirical results.

## Personal Reflection


## Prerequisite

For this course, please install [Python 3](https://www.python.org/) - the Anaconda distribution is a gentle starting point.
An integrated development environment (IDE) is also highly desirable.
It makes programming user-friendly and enjoyable.
[VS Code](https://code.visualstudio.com/) with the Python extension .

## Structure

The book version can be partitioned into three parts: Python, Econometrics, and Machine Learning.

The first two lectures cover basic Python and Python for data science. They teach skills about efficient array manipulation, parallel computing, and remote computing.
The following two lectures cover simulation exercises and simulation-based methods in econometrics.
The last two lectures talk about machine learning methods. Machine learning is relatively new for economists. Most economics programs only introduce a few
algorithms but do not cover the theoretical components. We try to provide a review starting from the conventional nonparametric statistical methods.

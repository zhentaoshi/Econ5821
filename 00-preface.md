# Preface


Programming is an essential skill for researchers in economic analysis.
In the time of big data, empirical economic research becomes main stream.

I believe the best way to learn programming is to follow examples. These notes contain executable examples that illustrate Python usage and econometric computational ideas.

Econometrics is interdisciplinary study involving economics, statistics, operational research, and computational science. No matter how beautiful is the theory,
it will be of little use if it cannot be implemented. Thus econometric procedures must be accompanied with computational code. Given that many existing methods
are encapsulated in canned packages, they do not cover new methods, which must be developed by econometricians who propose these procedures.

Our econometric procedures are difficult to commercialize.
To facilitate spread, one way is to offer to code for free. The world runs on open-source software.
Many open source software is indispensable for our daily work, for example, Linux, Python, R, and LaTeX.

These lecture notes are products of an ongoing writing project.
They are not intended to be comprehensive.
I don't want to reinvent wheels.
I refer to the relevant papers and surveys when there are excellent writings for mature topics.


## The Impact of AI to Programming

AI-assisted tools now automate many low-level tasks---scaffolding code, translating between languages (e.g., Python and R), generating documentation and tests, and surfacing relevant examples. This shifts the bottleneck from typing code to specifying problems precisely, designing data and software architecture, validating results, and maintaining reproducible workflows. AI can speed prototyping and learning, but outputs can be incorrect. Human review, testing, and version control remain essential.

Students still need to learn programming. Core skills in `Python/R`, data structures, numerical computing, debugging, testing, and performance are what let you evaluate and adapt AI-generated code, integrate it into real projects, and ensure correctness and reproducibility. In practice, you will use AI as an accelerator: write clear prompts, constrain solutions, verify with unit tests, read source docs, and profile/benchmark critical code. The competitive edge comes from combining conceptual understanding with engineering discipline---clean data pipelines, transparent notebooks, reliable environments, and defensible empirical results.


## Prerequisite

For this course, please install [Python 3](https://www.python.org/)---sthe Anaconda distribution is a gentle starting point.
An integrated development environment (IDE) is also highly desirable.
It makes programming user-friendly and enjoyable.
[VS Code](https://code.visualstudio.com/) with the Python extension .

## Structure

The book version can be partitioned into three parts: Python, Econometrics, and Machine Learning.

The first two lectures cover basic Python and Python for data science. They teach skills about efficient array manipulation, parallel computing, and remote computing.
The following two lectures cover simulation exercises and simulation-based methods in econometrics.
The last two lectures talk about machine learning methods. Machine learning is relatively new for economists. Most economics programs only introduce a few
algorithms but do not cover the theoretical components. We will provide a review starting from nonparametric statistical methods.



## Personal Reflection

-- about `R` (Written in 2017)

Thirty years ago aspiring young econometricians picked up GAUSS.
Twenty years ago the new blood began with MATLAB.
R raised ten years ago when the time came to my generation.
I have been using R since I started my postgraduate study in Peking University in 2005.
R helps me with my daily research and teaching.

There are other candidates in statistical programming, for example Matlab, Python, Julia and Fortran.
Each language has its own pros and cons.
R has many advantages.
First, it inherits the standard program syntax from C. It is quick to learn for anyone with prior programming experience.
Moreover, once you master R, it is easy to switch to other language, if not R, in your workplace in the future.

Second, backed by a vast statistician community, R enjoys a large selection of packages, including the most recent ones.
When they publish a paper, often times statisticians write and upload a companion R package to facilitate user adoption.

Third, R is free.
It was the primary reason that I chose it at the very beginning.
In the era of cloud computing, an algorithm written in R is easier to share, test, and improve.
Anyone can run R code on any platform, free of license and fee headache.

R is not without limitations. For example, speed is a concern when running big and complex jobs.
However, it will not be an issue in the problems that we will encounter in the first-year postgraduate study.

Lastly, learning a language is a non-trivial investment of our precious time.
It is much more important to master one language with fluency than to know several languages.

R is not the only language available for computing. Why not Python?
Python is a general purpose language, not a scientific computing language.
We need to import external modules even for basic numerical operations.
For example, I personally don't like `np.mean`, `np.var` and `np.log`, and its index rule starting from 0.
For basic matrix manipulation, the default behavior of `numpy` is different from R.

Why not Julia? Julia is too young to have a big community.
We would wait until it grows into more stable status.
Moreover, the speed advantage does not help much in interactive usage in empirical research.

Over the years, I have had a taste of both Python and Julia.
In my opinion, R so far best suits our purpose of learning a computing language for statistics and econometric analysis.

I was an expert in MATLAB, which is proprietary. I wrote those first few papers during and after my Ph.D study. However, I was never a fan of MATLAB's syntax, what was worse was its ugly functions.
MATLAB may still linger in some areas in engineering, but it is a dinosaur fossil buried under the wonderland of big data.

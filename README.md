# Test Driven Python

## Learn Python using Test Driven Development!

This is a project designed for Python beginners who want to learn the ins and outs of Python. The project contains two main sections: `lessons` and `tests`. `lessons` contains a number of directories, inside each of which is a challenge that's described in an `index.html` file. Unit tests for the chanllege live in the `tests` directory. 

This project was inspired by the Learn Ruby course at [TestFirst.org](http://testfirst.org/).

## How to use this project

### I want to learn Python

If you've never used Python before, open the `index.html` file in the top level folder of this project to get started. You can always open any file that ends in `.html` in your web browser. These will be a little bit easier to read than just looking at the raw files themselves.

Each of the directories in `lessons` contains a single challenge. Create the appropriately named file inside that directory, (for lesson 0 your filename should be `hello_world.py`) to run the tests. The file **must** be in the right directory for the unit tests to evaluate whether it works or not.

If you already have python, pip, and virtualenv installed on your computer, and you know how to set up your virtual environment then install `requirements.txt`. Then hop into `lessons/lesson_0_hello_world` and check out the `index.html` file in there for more instructions.

### I want to use this project to teach Python

Awesome! Please let me know by starring the repo or dropping me a line on [twitter](https://twitter.com/JLUnrein). I would love to know how it works out for you.

Have each of the students in your class or workshop clone the repo locally. I recommend walking through the first two lessons as a group or with a live code demo. This will get students used to the directory structure and to how to run unit tests. Have them start solo or paired work with one another on Lesson 2: FizzBuzz.

## How to contribute to this project

To contribute to this project, fork the repo and open a pull request.

### Improve existing lesson content, language, or styling

If you've used this project to learn Python or if you've used it in a class I would love your feedback!

I'm sure there are sections of the written material for the challenges that could be clearer or more explicit. If you have ideas for how to improve unit tests for an existing lesson or on how lessons can be written more lclearly, please open an issue detailing your proposed improvements. 

If you would like to fix the issue yourself, please comment on the issue, fork the repo, and open a pull request.

I'm also no prize when it comes to visual design, so if you think you can improve on it, **please do**.

### Adding new lessons

If you would like to add a new lesson that you think would meaningfully contribute to the cirriculum, please fork the repo and open a pull request. Each new lesson will need the following:

- A Python package in `lessons` that follows this convention: "lesson_{}_{}".format(lesson_number, challenge_name)
- An `index.html` file detailing the lesson specs and a brief introduction to any new concepts introduced in the lesson (ex: new data structures, etc.)
- A test file with specs that match the outline in your `index.html` file.
-- Please include comments at the top with an abbreviated version of your instructions and notes from `/lessons/your_lesson/index.html`

Note: The first few lessons are designed to build in complexity. If you're including a lesson that belongs in the more basic lessons of this project, please choose an appropriate lesson number. We'll figure out the details of how it should fit in during the pull request discussion. If it's a more complex challenge that includes several concepts covered in previous challenges, please choose the next available lesson number.

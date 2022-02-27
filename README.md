# Coding interview prep

This is a collection of coding challenges that I've solved, in preparation for
coding interviews. I've also included some tips for acing your interview.

I know my preparation works because I was successful at the two on-site
interviews I've had so far. For transparency, the first company did reject me
due to my lack of work experience as a software developer, but they assured me
they were happy with my interviews. I'm now a full stack web developer in
London. You can check out my CV at
[bluprince13.com/cv](https://bluprince13.com/cv).

I focus on Python in this repo. For a Java/Kotlin approach, checkout
https://github.com/gravindran2412/coding-interview-prep

> :warning: I do not intend for you to actually read the code that I've written.
> It's not ultra efficient or well styled. My hope is just that seeing how I
> prepped for my interviews inspires you to do your own prep.

## Structure of this repo

Challenges are grouped into folders by type, e.g., arrays, hash tables.

> :information_desk_person: I have also solved some coding puzzles for
> [Advent of Code](https://adventofcode.com/) under the `adventofcode` folder.
> This was just for fun. The puzzles here are generally way harder and time
> consuming than what I'd expect in an interview.

One file per challenge. Links to the challenge, e.g. on
[HackerRank](https://www.hackerrank.com), are provided at the top of each file.
Each file contains my solution, comments, and also unit tests to check the
solution.

You probably won't need to write unit tests for your interview. I write them
because I'm too lazy to check my solutions manually. Laziness is a virtue. To
run the unit tests, just invoke the file with Python. For example,
`python fizzbuzz.py`.

The solutions are generally not as perfect as I'd like them to be. However, if
you want me to explain a particular solution better, just ask me and I can
polish it up. I'm a nice guy. :stuck_out_tongue:

## How to prep for coding challenges

Here are some good resources for preparing for the coding interview.

- [HackerRank's interview preparation kit](https://www.hackerrank.com/interview/interview-preparation-kit)

  Most of the problems I practised on are from here. However, I prefer working
  on my Mac with the [VSCode](https://code.visualstudio.com/) editor. Therefore,
  I would solve the problems locally and then upload the solution to HackerRank
  once I thought it was ready.

- [Cracking the coding interview playlist](https://www.youtube.com/watch?v=GKgAVjJxh9w&list=PLX6IKgS15Ue02WDPRCmYKuZicQHit9kFt&index=1)
- [Cracking the coding interview](https://www.youtube.com/watch?v=4NIb9l3imAo&t=587s)
- [Cracking the coding skills](http://www.crackingthecodinginterview.com/uploads/6/5/2/8/6528028/cracking_the_coding_skills_-_v6.pdf)
- [Top 10 Algorithms for Coding Interview](https://www.programcreek.com/2012/11/top-10-algorithms-for-coding-interview/)

Don't worry if you find some of the challenges really hard. There were plenty
that I couldn't solve without looking for hints in other people's solutions. On
some, I would spend an entire day trying to crack the puzzle! To be honest,
knowing how to solve these coding challenges doesn't really help much in the day
job as a programmer, but I do believe it's a reasonably good proxy for gauging a
person's problem solving abilities / the way we think.

## Topics worth understanding

It's not enough to just be able to solve coding challenges. There are a few
other topics that you need to be really familiar with. Listed below are some of
these topics and links to learning resources that I recommend.

### Data structures

See
[Hacker Rank data structures playlist](https://www.youtube.com/playlist?list=PLI1t_8YX-Apv-UiRlnZwqqrRT8D1RhriX)

### Sorting algorithms

See
[Sorting Algorithms YouTube playlist](https://www.youtube.com/playlist?list=PL2_aWCzGMAwKedT2KfDMB9YA5DgASZb3U).

### Big-O

I can't stress how important it is to internalize this. Practice evaluating the
complexity of your coding challenges until it's second nature to you.

- [Big-O Notation](https://www.youtube.com/watch?v=v4cd1O4zkGw)

### System Design and Object Oriented Design

I'm not very good at these and I really struggled with the design questions that
came my way. However, it's a very interesting subject and something that I'm
excited about mastering in my programming career.

If you are applying for an entry level job, you may not need to prepare for
this. Do confirm what the company expects from you for your interview.

- [Grokking the System Design Interview](https://www.educative.io/courses/grokking-the-system-design-interview)


  This is a paid resource, but it's the only one I came across that had good
  examples of System Design interview type questions. Highly recommended by moi.

- [Grokking the Object Oriented Design Interview](https://www.educative.io/courses/grokking-the-object-oriented-design-interview)

  - Free alternative:
    [tssovi/grokking-the-object-oriented-design-interview](https://github.com/tssovi/grokking-the-object-oriented-design-interview)
- [Coding and system design interview questions (YouTube playlist)](https://www.youtube.com/playlist?list=PLA8lYuzFlBqAy6dkZHj5VxUAaqr4vwrka)
  - [System Design Interview Question: DESIGN A PARKING LOT - asked at Google, Facebook](https://www.youtube.com/watch?v=DSGsa0pu8-k)
  - [Amazon interview question: System design / Architecture for auto suggestions | type ahead](https://www.youtube.com/watch?v=xrYTjaK5QVM)
- [System Design Interview - checkcheckzz](https://github.com/checkcheckzz/system-design-interview/blob/master/README.md)
- [System Design Primer - donnemartin](https://github.com/donnemartin/system-design-primer)
- [S.O.L.I.D. Principles of Object-Oriented Design](https://www.youtube.com/watch?v=GtZtQ2VFweA)

### Agile

I wasn't tested on this at any point, but I think it's good to have at least an
awareness of what Agile is: a set of values and principles.

- [What is agile?](https://www.youtube.com/watch?v=Z9QbYZh1YXY&vl=en)
- [Agile manifesto](https://agilemanifesto.org)
- [Agile principles](https://agilemanifesto.org/principles.html)

## Parting words of wisdom

Normally in a coding interview, I forget that I'm interviewing and end up
completely absorbed in the thrill of solving the problem. I think that's a good
thing. Try to enjoy the experience and not worry too much. It's also okay to
mess up as long as you keep your cool. Messing up obviously happens a lot in the
day job, and seeing that you can handle it well will probably score you some
brownie points.

It's also okay to fail. I have failed so many times that I have lost count. I
have even done, and failed, interviews where I had no intention of joining the
company, but I just wanted the practice so that I had a better chance of nailing
the interviews that mattered. :stuck_out_tongue: What doesn't kill you makes you
stronger. :smiley:

[Tweet me](https://twitter.com/vipinajayakumar) if this repo has been useful to
you. :smiley: I wish you all the best at your interviews and your programming
career. May the force be with you. Don't be evil.

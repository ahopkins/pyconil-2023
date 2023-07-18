<!-- .slide: data-timing="30" -->

![PyCon IL 2023](/images/pycon-il-logo.png "Title")  <!-- .element: class="logo" -->

## Journey thru `this`  <!-- .element: class="sanic" -->
Adam Hopkins

```python
from datetime import date

date(2023, 7, 4)
```

notes:
- First, I want to thank the organizers for putting on this event
- Second, hats off to all of the speakers. I know I've learned a lot so far today

---

<!-- .slide: class="info-slide" data-timing="60" -->

![Adam Hopkins](/images/AMH.png "Adam Hopkins")  <!-- .element: class="profile small" -->

```python
class Adam:
    work = PacketFabric("VP of Software Engineering", 2020)
    oss = Sanic("Core Maintainer", 2018)
    home = Israel("Negev", 2014)

    async def run(self, *inputs: Union[🥨, ☕]) -> None:
        while True:
            await self.work.do(inputs)
            await self.oss.do(inputs)
        
    def sleep(self):
        raise NotImplementedError
```
- 🇮🇱
- ![Sanic](/images/sanic-framework-logo-circle-128x128.png)
- ![PacketFabric](/images/PacketFabric-logo-emblem.png)

notes:
- Made aliyah in 2014, I live in the South in a small Yishuv
- I spend a lof of my free time in OSS, specifically with Sanic
- VP of Software Engineering at PacketFabric
  - oversee several teams of developers building software solutions to automate our private network as a service solution

---
<!-- .slide: data-auto-animate data-timing="15" -->

## What exactly is `this`  <!-- .element: class="sanic" --> talk about? 
<!-- .element: class="r-fit-text" -->

notes:
- What should I talk about?
- The answer was simple...

---
<!-- .slide: data-auto-animate data-timing="45" -->

## What exactly is `this`  <!-- .element: class="sanic" --> talk about? 
<!-- .element: class="r-fit-text" -->

🤷‍♂️ <!-- .element: class="r-fit-text" -->

notes:
- Look to past speaking engagements

---
<!-- .slide data-timing="45" -->

## **Sanic** <!-- .element: class="sanic" --> or **Mayim** <!-- .element: class="mayim" -->
<!-- .element: class="r-fit-text" -->

notes:
- I've given a lot of talks about Sanic and Mayim
- too narrowly focused
  - Sanic is web framework 
  - Mayim is a DB access layer
  - neither is general interest enough for this collective audience

---
<!-- .slide data-timing="45" -->

![PacketFabric](/images/PacketFabric-logo-emblem.png)

notes:
- could be about
  - challenges of deploying/scaling production Python
  - interesting projects with task management, event driven reconciliation loops
- Not personal

---
<!-- .slide data-timing="50" -->

![SanicBook](/images/SanicCoverFinal.png) <!-- .element: class="book" -->

notes:
- I told some people I know that I have no idea what to talk about
  - The response: You wrote a book. Use that.
- My book has a narrow focus, but I tried to make the message broad
  - speaks to the value of open source
  - level up developer skills
  - Python and Sanic are just the vehicle
- I don't want this to be about me or be a sales pitch

---
<!-- .slide data-timing="60" -->

![Aliyah](/images/aliyah.jpg)

notes:
- I suppose a kind of a unique and interesting story
- But not what you came for
- However...
  - One thing I always share is the concept of journey

---
<!-- .slide: data-auto-animate data-timing="45" -->

## Journey
<!-- .element: class="r-fit-text" -->

notes:
- The process of getting from point A to point B
- You've often hear the phrase:
> The end justifies the means

- This concept of "the journey" is the opposite of that

---
<!-- .slide: data-auto-animate data-timing="45" -->

## Journey
<!-- .element: class="r-fit-text" -->

> The destination is often not the point.
> 
> Rather, the path taken is what builds memories and fulfills the soul.

notes:

> The destination is often not the point.
> Rather, the path taken is what builds memories and fulfills the soul.

- There's a lot to unpack in this statement
- Before we go too far into this concept let's bring this back to the world of software development

---
<!-- .slide: data-timing="90" -->

```assembly
section .data
    buffer db 20h

section .text
    global _start

_start:
    mov ecx, 5
    mov eax, 1
    jecxz _done

_mul:
    imul eax, ecx
    loop _mul

    mov edi, eax
    mov esi, buffer + 20h
    mov byte [esi], 0

_cnv:
    xor edx, edx
    mov ebx, 10
    div ebx
    dec esi
    add dl, '0'
    mov [esi], dl
    test eax, eax
    jnz _cnv

    mov eax, 1
    mov edi, 1
    lea edx, [buffer + 20h]
    sub edx, esi
    syscall

_done:
    mov eax, 60
    xor edi, edi
    syscall
```
<!-- .element: class="fragment no-max small" -->

notes:
- You are tasked with writing a program to calculate the factorial of a number
- A reminder:
  - a factorial is the product of all positive integers less than or equal to n
- Take a moment and think how you would do this
- Go!
- Did anyone write the code in their head in Assembly?
  - of course not
  - hard to write
  - hard to read
  - difficult to rationalize in our heads the low-level operations for even a simple task
- let's jump a few levels of abstraction higher...

---
<!-- .slide: data-timing="75" -->

```python
import functools as f
import operator as o

def fac(n):
    return f.reduce(o.mul, range(1, n+1), 1) if n>=0 else None
```
<!-- .element: class="fragment semi-fade-out" data-fragment-index="1" -->

```python
def factorial(n: int) -> int:
    factorial = 1

    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers")
    elif n == 0:
        return factorial

    for i in range(n):
        factorial *= i + 1
    return factorial
```
<!-- .element: class="fragment no-max" data-fragment-index="1" -->


notes:
- second version has no hidden knowledge of stdlib
- more readable, easy to follow
- Clearly the end result of the code is not the only thing that matters
  - writing "good code" also means writing code that is easy to
    - read
    - understand
    - maintain
- to further prove my point...

---
<!-- .slide: data-timing="90" -->

## Code Review
<!-- .element: class="r-fit-text" -->

notes:
- ... let's talk about code review
- What is the purpose of code review?
  - Not to find bugs (or at least primarily), that's for tests
  - Not to find style issues, that's for linters
  - Instead, it's to share knowledge
    - We suggest patterns to improve and grow as developers
    - Code base becomes stronger
- If coding was about the destination:
  - We would write code that is as terse as possible
  - We'd never refactor
  - No need for code review (other more efficient ways to find bugs)

---
<!-- .slide: data-timing="75" -->

## I ❤️ ![Python](/images/python-logo.png)
<!-- .element: class="i-heart-python" -->

notes:
- Okay, since we're talking about journey, I need to give you a little taste of my own journey with Python
- Been using Python since early 2000s
- Switched to it from PHP
- Whitespace has meaning
  - Forces readability
  - made my code better to look at
  - I felt like I was writing poetry

---
<!-- .slide: data-timing="60" -->

## ✒️ Poetry
<!-- .element: class="r-fit-text" -->

notes:
- While on the idea of poetry and Python, we're finally narrowing in on what I actually want this talk to be about
  - At this point I've been up here rambling for 10 minutes, and you are still not sure what I'm talking about.
  - Stick with me, there's a point coming
- To be clear, I am not talking about the Python packaging tool
- On this point in the timeline, we're still about 20 years in the past
  - pip was still 5-7 years away
- What I want to talk about is this...

---
<!-- .slide: data-timing="100" -->

```text [1|2-22|4-5|6-7|10|13-14]
>>> import this
The Zen of Python, by Tim Peters

Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!
```
<!-- .element: class="no-max" -->

notes:
- Baked into Python is an instruction manual to becoming a better developer
- It is part of the ethos of the language and became a manifesto for how I could become a better developer
- all I needed to do was follow the rules, what could be easier?
- Let's take a quick look through some of them
- good stuff here, but one threw me for a loop

---
<!-- .slide: data-auto-animate data-timing="10" -->

```text [16:]
There should be one-- and preferably only one --obvious way to do it.
```
<!-- .element: class="wrap" -->

notes:
- Read it...
- hmm...

---
<!-- .slide: data-auto-animate data-timing="60" -->

```text [16:]
There should be one-- and preferably only one --obvious way to do it.
```
<!-- .element: class="wrap" -->

There's a problem with this...

... I don't know what that one way is. 😬 😕
<!-- .element: class="fragment" -->

notes:
- I can remember the feeling I had when I first read this
- having a pit in my stomach
- because ...
  - I'm a newbie and I need to know the single best-practice pattern?
  - I went thru a phase where I was obsessed with finding the best way to do things
    - spend hours reading thru forums online
    - reading code
    - writing and rewiting the same code over and over
- this lead to...

---
<!-- .slide: data-auto-animate data-timing="10" -->

## Panic
<!-- .element: class="r-fit-text sanic" -->

notes:
- this lead to a feeling of panic ...

---
<!-- .slide: data-auto-animate data-timing="10" -->

## Panic
## Fear
<!-- .element: class="r-fit-text sanic" -->

notes:
- from there, it was a short jump to fear ...

---

<!-- .slide: data-auto-animate data-timing="10" -->

## Panic
## Fear
## Inadequacy
<!-- .element: class="r-fit-text  sanic" -->

notes:
- which culminated in a deeply-rooted feeling of inadequacy

---

<!-- .slide: data-auto-animate data-timing="75" -->

## Panic
## Fear
## Inadequacy

notes:
## Feeling when I read this many years ago
- these 3 things were debilitating
- If I don't know the "one way"
- I will never be a good developer
- There's some hidden knowledge out there, that I will never have

## Feeling when asked to speak at this conference
- identical
- What have I got to share that is worth hearing?

---
<!-- .slide: data-timing="210" -->

![Adam Hopkins](/images/adam-dark.png "Adam Hopkins") <!-- .element: class="faded" -->
<!-- .element: class="r-stretch" -->

notes:

## Digression
- I'm not a programmer, at least not a classically trained software engineer
  - I've been doing web development for 25+ years
- No computer science degree
  - learned at GW International Affairs
  - meaning lots of polisci and languages
  - Went on to law school and practiced law for a number of years as an attorney
- For the first 10 years of my career, I was a lawyer
- Hobby
- No formal training, bootcamp
- I learned thru experimentation and failure
- Of course during that time period I still did a lot of development work, including some side projects
- Dave Rogers story
  - no future in that
  - you need a real job
  - the Internet is just a fad
- When asked about connection between law and development
  - set of tools, framework -> go solve a problem

## Life is a journey
- The flow of life is not linear
- I found myself living in the middle of the desert in a 50sqm caravan with my wife and 3 kids
- My Hebrew was not good enough to practice law
- I was lucky enough to find a job as a developer

---
<!-- .slide data-timing="90" -->

## **Imposter** <!-- .element: class="sanic" -->  Syndrome
<!-- .element: class="fragment r-fit-text" -->


notes:
- But it was not easy
  - thrust into a new career with no background
  - I was not prepared
  - Sure, I had years of experience at the time
  - But, was I a *REAL*  developer?
- ...
- If not figured out that feeling of panic/fear/inadequacy is called imposter syndrome

## Imposter Syndrome
- psychological pattern in which an individual doubts 
  - their skills, 
  - talents
  - accomplishments 
  - and has a persistent internalized fear of being exposed as a "fraud"
- I think everyone in this room knows what I'm talking about
  - I think everyone experiences this
  - Either currently, or at some point in their past

---
<!-- .slide: data-timing="105" -->

## **1** <!-- .element: class="fragment fade-in-then-out" --> **2** <!-- .element: class="fragment fade-in-then-out" -->  **🙈** <!-- .element: class="fragment fade-in-then-out" -->
<!-- .element: class="r-fit-text" -->

notes:
- I'm going to prove it
- Play a game, I'm going to invite someone up here on stage in front of the audience for a live coding demo
- Don't look yet, but under everyone's chair is a card
  - Most will be white
  - One will be black
  - Count of three
- ...
- imposter syndrome is a manifestation of insecurities we all have
  - as we compare ourselves to our peers

---
<!-- .slide: data-timing="45" -->

#### Meet Arthur

![Arthur 1](/images/arthur/1.jpg)
<!-- .element: class="r-stretch" -->

notes:
- Meet Arthur
- Arthur wants to be an artiest
- struggles with his inner-voice
- he believes himself an amateur, incapable of producing anything of value
- Looks to other artists and tries to copy them
  - never quite capable of reproducing their work

---
<!-- .slide: data-timing="60" -->

#### Panic, Fear, Inadequacy

![Arthur 2](/images/arthur/2.jpg)
<!-- .element: class="r-stretch" -->

notes:
- Arthur battles the same feelings of panic, fear, and inadequacy
- aside:
  - imposter syndrome is not unique to developers
  - exists in all facets of life
  - Any olim out there? You know this feeling
- let's take a dip into Arthur's journey...

---
<!-- .slide: data-timing="30" -->

```text
>>> import this
The Zen of Python, by Tim Peters
```

notes:
- Like my own, let's see if we can use the Zen of Python
- going to pick select lines and explore where they take us
- alright, ready?...


---
<!-- .slide: data-timing="10" -->

<!-- .slide: data-auto-animate -->

```text [4:]
Beautiful is better than ugly.
```

notes:
- First up...

---
<!-- .slide: data-auto-animate data-timing="130" -->

```text [4:]
Beautiful is better than ugly.
```

![Arthur 3](/images/arthur/3.jpg)
<!-- .element: class="r-stretch" -->

notes:
## Arthur
- embarks on a quest experimenting with new mediums and techniques
- amazes himself with his work and progress, but,
  - works in secret
  - afraid to show his work to anyone
- vulnerability 
  - incapable of sharing with those closest
  - the ones least likely to judge you
- The inner-voice of self-doubt is winning

## Coding
- as new developers, we can relate to this
- coding is like art
  - as a form of expression
  - subjectivity of beauty
    - anecdote about disagreement with `black` and `isort` with Tronic
- I can relate to Arthur here
  - early days of coding, I was afraid to show my code to anyone
  - snippets on webdeveloper.com
  - felt I needed to apologize for my code

---
<!-- .slide: data-timing="125" -->

```text [6:]
Simple is better than complex.
```

![Arthur 4](/images/arthur/4.jpg)
<!-- .element: class="r-stretch" -->

notes:
## Arthur
- Arthur struggles to find his own style
- He keeps trying to silence his inner-voice by showing off what he knows
  - more color
  - more detail
  - more shading
  - more complexity
  - it becomes a mess, and he needs to start over
  - Becomes a never-ending loop

## Personal anecdote
- once wrote a templating engine in PHP
- was very involved because it encapsulated so much logic in OOP
- I was proud of it
- Someone else came along and wrote the same thing in 20 lines of code
- We try to over compensate for our insecurities by adding more
  - Look, see what I know how to do
  - Never do we stop to think, do I really need a metaclass here?
  - Is this actually a good use case for a decorator?

---
<!-- .slide: data-auto-animate data-timing="90" -->

```text [10:]
Readability counts.
```

![Arthur 5](/images/arthur/5.jpg)
<!-- .element: class="r-stretch" -->

notes:
## Arthur
- meets a new friend, Ross
  - cool, calm, and collected
  - effortlessly produces beautiful work by painting happy little trees
  - teaches: beauty of artwork is in the understanding and connection between the artist and the viewer
    - the art is just the medium
    - the relationship between the artist and the viewer is what matters

## Coding
- This is where that subjectivity and beauty of code comes in
- because code is not itself the end, but rather the means, we know its intended audience is other developers
- when asked to give advice to new developers...

---
<!-- .slide: data-auto-animate data-timing="45" -->

> Know what you don't know.

![Arthur 5](/images/arthur/5.jpg)
<!-- .element: class="r-stretch" -->

notes:
- Works on 2 different levels
  - One - understand your own limitations
    - be willing to ask for help
  - Two - Even better, when you know the limits
    - you can research and push the boundaries
    - For the past year I've always copy/pasted this same code snippet, maybe now I should figure out what it does

---
<!-- .slide: data-timing="35" -->

```text [18:]
Now is better than never.
```

![Arthur 6](/images/arthur/6.jpg)
<!-- .element: class="r-stretch" -->

notes:
## Arthur
- feeling inspired by Ross, Arthur decides to take a leap of faith
- of course he is anxious and nervous
- the inner-voice is still there, but for now he has the courage to silence it


## My own journey
- I want to talk a little bit about how I silenced my own inner-voice
- To understand, I think you need to know a little more about my OSS journey

---
<!-- .slide: data-timing="80" -->

![Sanic](/images/sanic-framework-logo-white-824x200.png)


notes:
- discuss my own rationale for OSS
- How I got into it and why I continue to do it

---
<!-- .slide: data-timing="15" -->

```text [18:]
Now is better than never.
```

![Arthur 6](/images/arthur/6.jpg)
<!-- .element: class="r-stretch" -->

notes:
- let's come back to where we left off with Arthur
- he's feeling a bit nervous about his painting
  - he swallowed a bit of pride and is taking a big leap bit making his work public
- ...

---
<!-- .slide: data-timing="140" -->

```text [19:]
Although never is often better than *right* now.
```

![Arthur 7](/images/arthur/7.jpg)
<!-- .element: class="r-stretch" -->

notes:
## Arthur
- ouch
- So, right now, Arthur's a bit of a failure.
  - Or, at least he feels like one

## Coding
- But that's okay, failure is part of the process
  - Our code is not bulletproof until its been error-tested
  - Video of Dev reacting to QA tester
    - completely distraught at the number of bugs and what was thought to be a great design turned out to be complete garbage
- What separates senior developers from junior developers
  - not their knowledge
  - not their experience
  - rather, the number of times they've failed, and how they've learned from it
  - To move forward, you need to have the scars to prove it

---
<!-- .slide: data-auto-animate data-timing="15" -->

## How can we **overcome** <!-- .element class="sanic" --> imposter syndrome?
<!-- .element: class="r-fit-text" -->

notes:
- we've talked about embracing failures
- but, there's obviously more to it than that

---
<!-- .slide: data-auto-animate data-timing="60" -->

## How can we **overcome** <!-- .element class="sanic" --> imposter syndrome?
<!-- .element: class="r-fit-text" -->


> In the balance between humility and confidence,
> lies the cure.

notes:
- humility, we need to be willing
  - to admit our mistakes
  - to know our limits
  - and to be willing to ask for help
- confidence, we need to be willing
  - to take risks
  - to try new things
  - and to be willing to fail
- not an easy thing to achieve
- in my own personal experience, I've found a path that largely lead me thru the valley of the open source community
  - it need not be the same for all
  - but you nonetheless need to find your own path and your own balance
  - your own voice

---
<!-- .slide: data-timing="50" -->

```text [13:]
Errors should never pass silently.
```

![Arthur 8](/images/arthur/8.jpg)
<!-- .element: class="r-stretch" -->

notes:
## Arthur
- Getting back to Arthur, after the fiasco at the art show
  - Ross teaches him how to accept his failures
  - Arthur learns to balance humility and confidence and channel his failure into his artwork

## Coding
- In coding, we have a similar concept
  - Zen of Python teaches us:
    - `Errors should never pass silently`
  - Python generally embraces this concept, and supports it with a robust exception handling system
  - We should always be aware of our mistakes and log them for analysis

---
<!-- .slide: data-timing="150" -->


![Gatsby](/images/gatsby.jpg)
<!-- .element: class="r-stretch" -->

notes:
- The Great Gatsby, by F. Scott Fitzgerald
- apologize for spoiler, but it's been out for 100 years
- cool, calm, collected, in power
- mythical figure
- inside, he's a broken man
  - constant doubt of his own worth and authenticity
  - pursuit of Daisy is an attempt to solidify his place in society
  - ultimately his facade crumbles and leads to his downfall

---
<!-- .slide: data-timing="45" -->

```python
class JayGatsby:
    def __init__(self):
        ...
```

notes:
- We create objects like this all the time
- In the end, Jay Gatsby's inability to define `self` becomes his undoing
  - web of lies, parties, and superficial relationships in an attempt to recreate himself
  - His fake persona and real heritage are in such conflict that it all implodes
  - he failed to embrace his own unique qualities and background

---
<!-- .slide: data-timing="60" -->

```python
class Adam:
    work = PacketFabric("VP of Software Engineering", 2020)
    oss = Sanic("Core Maintainer", 2018)
    home = Israel("Negev", 2014)

    async def run(self, *inputs: Union[🥨, ☕]) -> None:
        while True:
            await self.work.do(inputs)
            await self.oss.do(inputs)
        
    def sleep(self):
        raise NotImplementedError
```

notes:
- Earlier I presented you with this code
  - playful attempt at creating a public bio
- Hidden in this code definition is an explicit absence of a definition of self
- defining self is incredibly complicated
- Reducing myself to code is a disservice and bound for failure
- leads me back to the original fear of imposter syndrome ...

---
<!-- .slide: data-auto-animate data-timing="90" -->

```text [16:]
There should be one-- and preferably only one --obvious way to do it.
```
<!-- .element: class="wrap" -->


notes:
- The Zen of Python has this line that always troubled me
  - The Zen is a helpful set of guidelines,
  - but broken in this case
- This one line fails to allow for the complexity of the human condition and individual expression
- To be reductionist is to exclude the very thing that makes us human
- Because Humans write code, and humans are complex, we cannot ignore this
  - there cannot possibly be only one way to do it
  - indeed there are infinite ways, some perhaps more "right" than others
  - since code is a journey, it is meant for human consumptions
  - therefore, it is a reflection of the author, it is impossible to define a single objective "obvious way"
  - sidetable LLMs, while ChatGPT and Copilot are amazing tools, they are not a replacement for human creativity
    - they do not downplay or rebut my point here
- I want to suggest there's a better way to write this maxim...

---
<!-- .slide: data-auto-animate data-timing="10" -->

```markdown [16:]
There should be one-- and preferably only one --obvious way **FOR YOU** to do it.
```
<!-- .element: class="wrap" -->

notes:
- We can write it to embrace the individual and the subjective perspective of the code author
- *READ IT*

---
<!-- .slide: data-auto-animate data-timing="10" -->

```markdown [16:]
There should be one-- and preferably only one --obvious way FOR YOU, **in this instance**, to do it.
```
<!-- .element: class="wrap" -->

notes:
- perhaps should recognize that a single author could achieve something in many ways
- but, we will ignore that for now, settling on a simpler version

---
<!-- .slide: data-auto-animate data-timing="10" -->

```markdown [16:]
There should be one-- and preferably only one --obvious way FOR YOU to do it.
```
<!-- .element: class="wrap" -->

notes:
- there it is, there is my improvement to the Zen of Python
- Now, let's jump back to the Arthur story...

---
<!-- .slide: data-auto-animate data-timing="30" -->

```markdown [16:]
There should be one-- and preferably only one --obvious way FOR YOU to do it.
```
<!-- .element: class="wrap" -->

![Arthur 9](/images/arthur/9.jpg)
<!-- .element: class="r-stretch" -->

notes:
- armed with his own understanding of self-worth, he can finally be free to be himself
- he's learned to embrace his own unique qualities and background
- confidence
- unique voice
- he's finally defeated the inner-voice of self-doubt with the unique voice of humble self-confidence

---
<!-- .slide: data-timing="30" -->

## Break the **Cycle** <!-- .element class="sanic" -->

notes:
With that said...
- know what you don't know
- use your weaknesses as a strength
- develop a balance of humility and confidence

---
<!-- .slide: data-timing="45" -->

## The **Challenge** <!-- .element: class="sanic" -->
<!-- .element: class="r-fit-text" -->

notes:
- Before I wrap up I want to issue everyone a challenge
- We're at the beginning of the Summer
  - I've always thought of it as a time period where I can grow and experiment
  - I can set targets for myself to learn a new technology by the end of the Summer
  - So, we are going to do that together
- By EOS, share your own unique voice
  - Blog
  - Tweets
  - Videos
  - Post on a forum, SO, Reddit, or GH
- Content: something you're passionate about, you've learned, or you're excited about
- Here are the rules ...

---
<!-- .slide: data-auto-animate data-timing="20" -->

Simple is better than complex

notes:
- keep it simple
- Write something as short as "Why I love list comprehensions"
- If you are inspired to write an in depth article on training LLMs, go for it

---
<!-- .slide: data-auto-animate data-timing="20" -->

Simple is better than complex <!-- .element class="faded" -->

Now is better than never

notes:
- don't wait for the perfect time
- You have until the end of the summer
- Use the shvung

---
<!-- .slide: data-auto-animate data-timing="20" -->

Simple is better than complex <!-- .element class="faded" -->

Now is better than never <!-- .element class="faded" -->

There should be one—and preferably only one—obvious way **FOR YOU** <!-- .element class="sanic" --> to do it.

notes:
- Don't worry about what others think
- This is about you and your opinions
- Be humble and be confident

---
<!-- .slide: data-auto-animate data-timing="10" -->

Simple is better than complex <!-- .element class="faded" -->

Now is better than never <!-- .element class="faded" -->

There should be one—and preferably only one—obvious way **FOR YOU** to do it.
<!-- .element class="faded" -->

**#BreakTheCycle** <!-- .element class="sanic" -->

notes:
- And this is the hashtag you should use for sharing your content

---
<!-- .slide: data-auto-animate data-timing="10" -->

**#BreakTheCycle** <!-- .element class="sanic" -->

@AdmHpkns

notes:
- By EOS I expect a bunch of tweets to my handle with this hashtag

---
<!-- .slide: data-auto-animate -->

**#BreakTheCycle**

![Adam Hopkins](/images/adam-dark.png "Adam Hopkins") <!-- .element: class="faded" -->
<!-- .element: class="r-stretch" -->

[@AdmHpkns](https://twitter.com/AdmHpkns)

[@admhpkns@fosstodon.org](https://fosstodon.org/@admhpkns)

[amhopkins.com](https://amhopkins.com) | [asherdesign.myportfolio.com](https://asherdesign.myportfolio.com/)

notes:
- Also, tomorrow I'll be doing a sprint on Sanic

# qss-inst [![Build Status](https://travis-ci.com/kosukeimai/qss-inst.svg?token=JxpGcfuMTdnnLSenfvSD&branch=master)](https://travis-ci.com/kosukeimai/qss-inst)

## Instructors' private repository for *[Quantitative Social Science: An Introduction](http://imai.princeton.edu/tmp/secure/qss.pdf)* (QSS) (Princeton University Press, 2017)

This repository contains the original `R Markdown` (Rmd) files for
exercises and their solutions.  Feel free to use them for your
teaching.  We will be adding more exercises and so check back this
repository regularly.

1. [Introduction](INTRO)
2. [Causality](CAUSALITY)
3. [Measurement](MEASUREMENT)
4. [Prediction](PREDICTION)
5. [Discovery](DISCOVERY)
6. [Probability](PROBABILITY)
7. [Uncertainty](UNCERTAINTY)

We welcome your contributions too.  Please improve the existing
exercises and add new ones so that other instructors can use them.  To
do this, create a fork, add an exercise, and then make a pull
request.

In addition, you might want to look at the following resources:

- [QSS main repository](https://github.com/kosukeimai/qss) contains
  all the data sets used in the manuscript

- [QSS swirl repository](https://github.com/kosukeimai/qss-swirl)
  contains [Swirl](http://swirlstats.com/) exercises for the book
  manuscript

## Practicalities

Precompiled student and instructor versions of all exercises in the
book can be downloaded as part of the [latest
release](https://github.com/kosukeimai/qss-inst/releases/latest).

## Compiling it yourself

### Prerequisites

The packages in `DESCRIPTION` should be installed in your local R
distribution.

If you plan to make pdf course materials, you should also have a LaTeX
distribution.

### Procedure

```
Rscript dist.R student
```

compiles *student* versions of all exercises in pdf and html, and
bundles them into one large zip archive `qss-student.zip` and
chapter-specific archives.

The student version of an exercise contains a pdf and an html version
of the questions, the data students must use, and an empty Rmd files
for their answers.

```
Rscript dist.R
``` 

compiles instructor versions of all exercises in pdf and html, and
bundles them into one large zip archive `qss-instructor.zip` and
chapter-specific archives.

The instructor version of an exercise contains a pdf and html version
of the questions, worked answers, and the data and resources necessary
to compile them the Rmd file.

Slightly more control over what is produced is possible by sourcing
`dist.R` from your R session and calling the `make_bundles` function
directly.

## Alternatively...

Each folder contains an Rmd file that can be loaded into RStudio or
similar and will compile using `rmarkdown::render`.  See `dist.R` for
more details.


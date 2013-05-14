=================================
Python Programming for Scientists
=================================

About
=====

This are the sources for a talk the author (Alexander Eberspächer) has given
at the informal student's seminar at the X. informal Billiard Workshop of
the German Research Unit 760 at Riezlern, Kleinwalsertal. A slightly enhanced
version has been presented to our working group, too.

The presentation meant to be both a very short introduction to the Python
programming language as well as a short demonstration of advanced topics such
as use of scientific packages (NumPy, SciPy). Python as a glue language was
targeted, too. So the talk tried to kill two birds with one stone: it tried to
introduce Python to people without prior exposure and it also tried to show
some advanced topics to experienced Python users. Wrapping other languages was
introduced with the aim of speeding Python computations up.

Slides
======

If you are only interested in the pdf slides, here's a direct link:
https://github.com/aeberspaecher/PythonForScientists/raw/master/talk.pdf

Dependencies
============

You'll need Pygments for the syntax highlighted LaTeX snippets to work.

Notes
=====

In the directory ``Pygsnippets`` you'll find the code snippets that appear
on the slides, too.

The folder ``Code`` contains the code I have used for the benchmarks. The
Cython and f2py files contain some hints on the creation of shared objects.

In comparison to slides I used in the Riezlern talk, there are some new
slides. Additionally, minor bugs have been fixed. Let me know if you find
more. The new slides are a bit more advertising Python as the old ones did.

A note on style: the slides show some Python like ``return np.sinc(x[:])**2``
with ``x`` being a NumPy array. Yes, of course the slice operator ``[:]`` part
is unnecessary and slows everything up (a bit). However, I just like this
synatx as it really makes clear that ``x`` is an array. I guess I aquired this
habit doing a lot of Fortran over the past years.

Some references
===============

Scientific Python
-----------------

- EuroSciPy lecture notes: http://scipy-lectures.github.com/
  (recommended!)

- H.-P. Langtangens slides: http://heim.ifi.uio.no/~hpl/scripting/all-nosplit/
  Also check Langtangens book "Python Scripting for Computational Science".

OpenMP
------

- OpenMP for Fortran:
  http://www.openmp.org/presentations/miguel/F95_OpenMPv1_v2.pdf
  (recommended)

mpi4py
------

- Documentation (also on using it with C/Fortran....):
  http://mpi4py.scipy.org/docs/mpi4py.pdf


Some further links
==================

Python in teaching
------------------

- Ärnd Bäcker, Computational Physics Education with Python (in Computing in
  Science & Engineering 9, 2007):

  http://ieeexplore.ieee.org/xpls/abs_all.jsp?arnumber=4160252&tag=1

  The whole isssue of the journal is dedicated to Python:

  http://users.cse.ucdavis.edu/~cmg/Group/readings/pythonissue_1of4.pdf
  http://users.cse.ucdavis.edu/~cmg/Group/readings/pythonissue_2of4.pdf
  http://users.cse.ucdavis.edu/~cmg/Group/readings/pythonissue_3of4.pdf
  http://users.cse.ucdavis.edu/~cmg/Group/readings/pythonissue_4of4.pdf

Software engineering
--------------------

An aspect of daily work everyone of us can greatly benefit from...

- http://software-carpentry.org/
- http://www2.ccr.buffalo.edu/halfon/courses/Resources%20for%20Students%20and%20Postdocs/other_docs/Wilson_2006_American%20Scientist.pdf

=================================
Python Programming for Scientists
=================================

About
=====

This is the source for a talk the author (Alexander Eberspächer) has
given at the informal student's seminar at the X. informal Billiard
Workshop of the German Research Unit 760 at Riezlern, Kleinwalsertal.

It was meant to be both a very short introduction to the Python
programming  as well as a short demonstration of advanced topics
such as scientific packages (NumPy, SciPy). Python as a glue
language was targeted, too.

Slides
======

If you are only interested in the pdf slides:
https://github.com/aeberspaecher/PythonForScientists/blob/master/talk.pdf

Dependencies
============

You'll need Pygments for the syntax highlighted LaTeX snippets to work.

Notes
=====

In the directory ``Pygsnippets`` you'll find the code snippets that
appear on the slides, too.

The folder ``Code`` contains the code I have used for the
benchmarks. The Cython ad f2py files contain some hints on the
creation of shared objects.

In comparison to presentation I gave in Riezlern, there are two new
slides. Minor bugs have been fixed. Let me know if you find more.

Some references
===============

Scientific Python
-----------------

- EuroSciPy lecture notes: http://scipy-lectures.github.com/
  (recommended!)

- H.-P. Langtangens slides: http://heim.ifi.uio.no/~hpl/scripting/all-nosplit/

OpenMP
------

- OpenMP for Fortran: http://www.openmp.org/presentations/miguel/F95_OpenMPv1_v2.pdf
  (recommended)

mpi4py
------

- Documentation (also on using it with C/Fortran....): http://mpi4py.scipy.org/docs/mpi4py.pdf

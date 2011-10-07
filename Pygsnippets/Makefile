PYG = pygmentize -P style=autumn
OBJECTS = controlStructures.tex\
	Functions.tex\
	HelloWorld.tex\
	DataTypes.tex\
	Files.tex\
	NumPy.tex\
	SciPy.tex\
	Cython1.tex\
	Cython2.tex\
	sincSquare.tex\
	F2PY1.tex\
	F2PY2.tex\
	sincSquareNumPy.tex\
	mpi4py.tex\
	Pitfalls1.tex\
	Pitfalls2.tex\
	logMap.tex\
	magic.tex

# pattern rules:
%.tex: %.py
	$(PYG) -o $@ $<

%.tex: %.pyx
	$(PYG) -o $@ $<

%.tex: %.f90
	$(PYG) -o $@ $<

pygsnippets: $(OBJECTS) Makefile

clean:
	rm *.tex

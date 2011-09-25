COMPILER = pdflatex
CFLAGS = -halt-on-error
OBJECTS = talk.tex\
	Intro.tex\
	Basics.tex\
	Advanced.tex\
	Glue.tex\
	Summary.tex

# ultimate target

talk: $(OBJECTS)
	make -C Pygsnippets
	$(COMPILER) $(CFLAGS) talk.tex
	evince talk.pdf&

bib: $
	bibtex talk
	
# other targets

# Dependencies

talk.pdf: $(OBJECTS)

# clean up rule

clean:
	rm Pygsnippets/*.aux
	rm -f *.aux *.log *.out *.snm *.toc *.nav

texfile = slides

$(texfile).pdf:
	pdflatex $(texfile).tex
	pdflatex $(texfile).tex

clean:
	rm -f *.log *.aux *.bbl *.blg *.out *.toc *.nav *.snm *~ $(texfile).pdf

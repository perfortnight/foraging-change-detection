all: paper.pdf

paper.pdf: main.tex 
	pdflatex main.tex
	pdflatex main.tex
	bibtex main.tex
	pdflatex main.tex
	pdflatex main.tex

plot_results.eps: plots/results.gnuplot 
	gnuplot plots/results.gnuplot


clean:
	rm -f *log *aux *bbl *converted-to.pdf main.pdf *spl

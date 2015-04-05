all: paper.pdf

paper.pdf: typeinst.tex 
	pdflatex typeinst.tex
	pdflatex typeinst.tex
	bibtex typeinst.tex
	pdflatex typeinst.tex
	pdflatex typeinst.tex

plot_results.eps: plots/results.gnuplot 
	gnuplot plots/results.gnuplot


clean:
	rm -f *log *aux *bbl *converted-to.pdf typeinst.pdf *spl

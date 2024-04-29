# usage to build all:
# 	make
# usage to build a single file:
# 	make file=session-1
# usage to watch for changes:
# 	make file=session-1 watch

all:
	latexmk -pdflatex="pdflatex -shell-escape %O %S" $(file)

force:
	latexmk -pdflatex="pdflatex -shell-escape %O %S" -g $(file)

clean:
	latexmk -c

watch:
	latexmk -pvc -pdflatex="pdflatex -shell-escape %O %S" $(file)

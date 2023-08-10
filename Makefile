# usage to build all:
# 	make 
# usage to build a single file:
# 	make file=session-1 	
# usage to watch for changes:
# 	make file=session-1 watch

all:
	latexmk -lualatex="lualatex -shell-escape %O %S" $(file)

force: 
	latexmk -lualatex="lualatex -shell-escape %O %S" -g $(file)

clean:
	latexmk -c

watch:
	latexmk -pvc -lualatex="lualatex -shell-escape %O %S" $(file)

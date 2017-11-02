FILE = "BlockAuth.py"
ROOT = $(shell pwd)

compile:
	@printf "Building ./src/${FILE}..."
	@docker run -it --rm -v '${ROOT}/src:/compile/src' coz/neo-boa-compiler ${FILE}
	@printf " DONE\n"
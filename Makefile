FILE = "BlockAuth.java"
ROOT = $(shell pwd)

DEFAULT: build

build:
	@printf "Building ./src/${FILE}..."
	@docker run -it --rm -v '${ROOT}/src:/build/files' blockauth/neoj-docker-builder ${FILE}
	@printf " DONE\n"

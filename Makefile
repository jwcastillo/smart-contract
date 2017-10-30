BYTE_FILE = "BlockAuth.class"
JAVA_FILE = "BlockAuth.java"
ROOT = $(shell pwd)

DEFAULT: build

build:
	@printf "Building ./src/${JAVA_FILE}..."
	@docker run -it --rm -v '${ROOT}/src:/build/files' coz/neoj-builder ${JAVA_FILE}
	@printf " DONE\n"

compile:
	@printf "Building ./src/${BYTE_FILE}..."
	@docker run -it --rm -v '${ROOT}/src:/compile/src' coz/neoj-compiler ${BYTE_FILE}
	@printf " DONE\n"
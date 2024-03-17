.PHONY: clean build run

clean:
	rm -rf build

build: clean
	cmake -S . -B build/
	cd build/ && make
	cd ..

run: build
	clear
	@./build/AlgosWithC
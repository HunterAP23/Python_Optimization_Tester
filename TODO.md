### Workflow
1. Develop application to utilize the `gooey` library for GUI
2. Manage application dependencies with `poetry`
3. Lint code with `black` and `isort` libraries
4. Format and check for errors in code with `flake8`
5. Check if minimum support Python version changed with `vermin`
6. Compile code with `cython`
7. Build application into singular executable with embedded Python runtime with `pyinstaller`
8. Use `pre-commit` CI to run through steps 3 to 7 before a commit is sent out
9. Use GitHub Actions to run through steps 3 to 7 for each os (Windows, Linux, and MacOS)
10. Use GitHub Actions to create a new release if a push or pull request is made onto the main branch.


### In Progress

- [ ] Update GitHub Actions
  - [ ] Set up Poetry
  - [ ] Add Cython compilation step
    - [ ] Check if individual compiler scripts exist - if yes then compile, else skip this job
    - [ ] Compile with `python src/setup.py build_ext`
  - [ ] Update pyinstaller steps to include compiled code
    - [ ] Check for and include compiled code
      - [ ] `*.pyd` for Windows
      - [ ] `*.so` for Linux and MacOS
    - [ ] Check for and include related libraries (such as `Gooey` and `wxPython`)
  - [ ] Add support for Pypy builds
    - [ ] Add Cython compile steps
    - [ ] Add Pyinstaller build steps
    - [ ] Add release steps
  - [ ] Add support for Anaconda builds
    - [ ] Add Cython compile steps
    - [ ] Add Pyinstaller build steps
    - [ ] Add release steps
- [ ] Create OS-agnostic Python script to handle compilation
  - [ ] Handle PYD and SO files depending on OS (Windows OR Linux / MacOS)
  - [ ] Multithreaded compiling
    - Need to work on performance cores only, if the system has heterogeneous core layout (performance / efficiency cores)
  - [ ] Time the compilation with `timeit` library
  - [ ] Support arguments:
    - [ ] Clean: delete existing C / C++ / PYD / SO files before compiling
    - [ ] Force: compile the files even if the PYD/SO files already exist and the code is unchanged
    - [ ] Threads: limit the number of threads that can used for compiling individual scripts (1 thread per compile)
    - [ ] Measure Time: whether or not to measure the time it takes to compile the individual scripts
    - [ ] Loops: Number of compilations loops to use for measuring compilation time (requires `Measure Time` to be true)
  -
  

### Done ✓
- [x] Add Cython Compilation
  - Build app with `python .\src\setup.py build_ext`
  - Fix build locations
- [x] Migrate off of `pipenv` and onto `poetry`
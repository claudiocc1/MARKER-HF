# MARKER-HF, standalone C++ package

## MARKER-HF application

To build the MARKER-HF application on linux
```
g++ -std=c++11 -o MARKER-HF MARKER-HF.C
```

To buid the MARKER-HF application on MacOS
```
clang++ -stdlib=libc++ -o MARKER-HF MARKER-HF.C
```

MARKER-HF-32.exe and MARKER-HF-64.exe are 32 and 64 bit precompiled applications
for Windows.  They were cross-compiled from Linux with
```
linux_prompt> /bin/sh build_forWindows_fromLinux 
```
(requires installation of [mingw](https://arrayfire.com/cross-compile-to-windows-from-linux/) in inux)

Then to calculate  MARKER-HF from the 8 covariates from the command line:
```
linux_or_mac_prompt> ./MARKER-HF 80 12 100 16 30 1000 4.2 27
-0.102185
```
or
```
blah
```

The order of the 8 covariates is
```
BPDIAS CREATN BUN HGB WBC PLT ALB RDW
```

In case of problems with the inputs MARKER-HF prints out an error message

## Mortality

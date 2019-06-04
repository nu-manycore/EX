* for build (for gcc)
- gcc -fopenmp main.c bitmap.c

* for exec
- a.out [# of threads] [input image] [output image]

(a.out 2 logo.bmp out.bmp)

- image should be 24bit bmp
- With the sample main.c, [# of threads] is meaningless because the program is not parallelized.


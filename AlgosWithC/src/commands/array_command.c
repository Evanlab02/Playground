/**
 * Array command file.
 */
#include <stdio.h>
#include <time.h>

void accessArray(int index) {
  char DEBUG_PREFIX[] = "\033[0;35m[DEBUG]\033[0;37m";
  char INFO_PREFIX[] = "\033[0;34m[INFO]\033[0;37m";
  int ARRAY[] = {48,2,725,702,251,95,850,181,57,100,140,427,395,988,655,77,782,508,826,958,5,596,844,230,902,707,246,989,595,744,639,478,383,504,245,668,322,389,192,177,620,273,883,434,896,441,94,413,790,564,423,5,768,738,375,850,177,254,367,669,767,614,307,657,354,960,903,293,80,283,484,317,148,560,288,969,602,888,8,209,957,246,663,696,26,765,372,714,456,478,980,765,836,74,803,604,850,407,355,376};

  clock_t t;
  t = clock();

  int value = ARRAY[index];

  t = clock() - t;
  double time_taken = ((double)t)/CLOCKS_PER_SEC;
  printf("%s Took %f seconds to execute.\n", DEBUG_PREFIX, time_taken);
  printf("%s RESULT: %d\n", INFO_PREFIX, value);
}

void array() {
  accessArray(50);
}
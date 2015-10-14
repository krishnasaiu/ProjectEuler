#include <iostream>
#include <cmath>
#include <cstdio>
using namespace std;

int main() {
  int T;
  scanf("%d", &T);
  while(T--){
    int N;
    scanf("%d", &N);

    long long result = -1;
    for (int c = 0; c <= N/2; ++c) {
      for (int b = 0; b < N-c && b < c; ++b) {
          int a = N-b-c;
          if (a > b) continue;
          if (a*a + b*b == c*c)
            result = max(result, (long long) a*b*c);
      }
    }
    printf("%lld\n", result);
  }
  return 0;
}

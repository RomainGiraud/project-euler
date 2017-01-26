// g++ main.cpp -o main -std=c++11

#include <iostream>

using namespace std;

int fibo(uint64_t num)
{
  uint64_t prev2 = 0;
  uint64_t prev1 = 1;
  if (num == 0)
    return prev2;
  else if (num == 1)
    return prev1;

  int tmp = 0;
  for (uint64_t i = 2; i < num + 2; ++i)
  {
    tmp = prev1;
    prev1 = prev2 + prev1;
    prev2 = tmp;
  }
  return prev2;
}

int fibo_even(uint64_t max)
{
  uint64_t prev2 = 0;
  uint64_t prev1 = 1;

  uint64_t val = 0;
  uint64_t tmp = 0;
  while (true)
  {
    tmp = prev1;
    prev1 = prev2 + prev1;
    prev2 = tmp;
    if (prev2 > max)
      break;
    if (prev2 % 2 == 0)
      val += prev2;
  }
  return val;
}

int main()
{
  cout << fibo(40) << endl;
  cout << fibo_even(4000000) << endl;
  return 0;
}

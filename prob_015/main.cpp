#include <iostream>

using namespace std;

namespace
{

typedef long long unsigned llu;

llu _walk(int x, int y)
{
  if (x < 0 || y < 0)
    return 0;

  if (x == 0 && y == 0)
    return 1;

  return _walk(x - 1, y) + _walk(x, y - 1);
}

llu walk(int n)
{
  return 2 * _walk(n - 1, n);
}

} // anonymous namespace

int main()
{
  cout << " 1 => " << walk(1) << endl;
  cout << " 2 => " << walk(2) << endl;
  cout << " 3 => " << walk(3) << endl;
  cout << "20 => " << walk(20) << endl;

  return 0;
}

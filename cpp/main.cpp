#include <iostream>
// Extras: If and loop & function

void oddoreven(int num)
{
if(num % 2 == 0)
{
  std::cout<<"Even\n";
}
else
{
  std::cout<<"Odd\n"; 
  }
}

int absolutevalue(int x)
{
    return x * ((x > 0) - (x < 0));
}

int main()
{
  std::cout << "Hello World\n" << std::endl;
  int x = -10;
  std::cout << "The absolute value is " << absolutevalue(x) << '\n';

}
#include <iostream>

a = 5
b = 3
int add(int a , int b){
  int c;
  std::cout << "In func a: " << a << " b: " << b << "/n";
  c = a + b;
  return c;
}

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


int main()
{
  std::cout << "Hello World\n" << std::endl;
}
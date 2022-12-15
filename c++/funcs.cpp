#include <iostream>

// use void as return type if not returning a value
// and use return statement without a value
void print_hello(){
  std::cout << "Hello World/n";
}

int add_two_numbers(int a , int b){
  int c;
  std::cout << "In func a: " << a << " b: " << b << "/n";
  c = a + b;
  return c;
}

int main()
{
  print_hello();
  int result = add_two_numbers(5,8);
  a = 30;
  b = 100;
  result = add_two_numbers(b,a);
  std:cout << "a: " << a << " b: " << b << "/n";
  std::cout<< result << "/n";
  return 0;
}

// loops

int main()
{
  int i;

  i = 0;
  while (i<10){
    // int j = 20
    // std:cout << j ;
    // j is only defined in this loop
    std::cout << i << ", ";
    i=i+1;
  }
  std::cout << std::endl;

  std::string s = "hello";
  for(auto letter : s){
    std::cout << letter << "-" ;
  }
  std::cout << "/n/n";
  // std::cout << "/n/n";
  // char go_again = 'y';
  // while (go_again == 'y'){
  //  std::cout << "Continue? ";
  //  std::cin >> go_again;
  // }
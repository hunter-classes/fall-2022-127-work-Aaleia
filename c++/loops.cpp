#include <iostream>

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

  
  for (int x=0; x<10; ++x){
    std::cut << x << ", ";
  }
  std::cout << std:endl;
  // return 0;
}
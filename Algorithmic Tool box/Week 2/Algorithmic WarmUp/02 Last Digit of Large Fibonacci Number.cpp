
#include<bits/stdc++.h> 
using namespace std; 

int fib(int n) 
{ 
	int a = 0, b = 1, c, i; 
	if( n == 0) 
		return a; 
	for(i = 2; i <= n; i++) 
	{ 
	c = a + b; 
	a = b; 
	b = c; 
	} 
	return b; 
} 


int get_fibonacci_last_digit(long long n) {
    int first = 0;
    int second = 1;

    int res;

    for (int i = 2; i <= n; i++) {
        res = (first + second) % 10;
        first = second;
        second = res;
    }

    return res;
}

int main() {
    int n;
    std::cin >> n;
    int c = get_fibonacci_last_digit(n);
    std::cout << c << '\n';

    return 0;
}


#include<iostream>
#include<bits/stdc++.h>
using namespace std;

int main()
{

	int a[16][16];
	int x,y,sum=0;
	for(int i=0;i<16;i++)
	{
		for(int j=0;j<16;j++)
		{
			cin >> a[i][j];
		}
	}
	for(int i=0;i<16;i++)
	{
		x = *std::max_element(a[i],a[i]+16);
		y = *std::min_element(a[i],a[i]+16);
		sum = sum + (x-y);
		x = 0;
		y = 0;
	}
	cout << sum << endl;
}

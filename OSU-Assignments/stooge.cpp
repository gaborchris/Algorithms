//Stooge Sort
//Christian Gabor
//1/23/18
#include <iostream>
#include <fstream>
#include <string.h>
#include <stdlib.h>
#include <sstream>
using namespace std;

void StoogeSort(int* A, int start, int end);
void Print_Array(int* numbers, int numint);

int main(){
	ifstream myfile;
	myfile.open ("data.txt");
	if(!myfile.is_open()) return 1;

	string myline;
	int numint;
	istringstream iss;
	int value;

	//Clean out insert.out file before use
	ofstream out("stooge.out");
	out.close();

	while(getline(myfile, myline))
	{
		numint = stoi(myline.substr(0, myline.find(" "))); 
		int numbers[numint];

		iss.str(myline);
		iss >> value;

		for(int i = 0; i < numint; i++)
		{
			iss >> value;	
			numbers[i] = value;
		}

		StoogeSort(numbers,0,numint-1);


		Print_Array(numbers, numint);

		iss.clear();
	}
	myfile.close();
	return 0;
}

void StoogeSort(int* A, int start, int end){
	int n = end - start + 1;
	if(n==2 && A[start] > A[end]){
		int swap;
		swap = A[start];
		A[start] = A[end];
		A[end] = swap;
	}
	if(n>2){
		//ceiling is hard to do in C++ with 2/3, better to invert m and substract from end
		int m = n/3;
		StoogeSort(A, start, end-m);
		StoogeSort(A, start+m, end);
		StoogeSort(A, start, end-m);
	}
}

void Print_Array(int* numbers, int numint){
	ofstream out("stooge.out", ios::app);
	for(int i = 0; i < numint; i++)
	{
		out << numbers[i] << " ";
	}
	out << '\n'; 
	out.close();
}
